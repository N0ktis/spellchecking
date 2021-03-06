# Теоретическая часть
## Условие задачи

*Напишите программу проверки орфографии с помощью BK-дерева*
## Подход к решению задачи

Решение данной задачи включает в себя два этапа: предварительное построение дерева поиска и выполнение поисковых запросов

### Этап 1: Построение дерева поиска
Согласно условию задачи для реализации проверки орфографии должна быть использована структура данных BK-tree.

Википедия:
> BK-дерево является метрикой дерева предложенного Walter Austin Буркхардом и Роберт М. Келлером , специально адаптированным к дискретным метрическим пространствам.


То есть при построении нашего дерева должно быть выполнено основное свойство метрики: 
$`\rho(x,z)\leqslant\rho(x,y)+\rho(y,z)`$
$`x,y,z \in X`$
где $`X`$ — множество слов, $`\rho`$ — метрика(расстояние)

В интернете было найдено две метрики, позволяющие реализовать BK-tree:
 - расстояние Левенштейна
 - расстояние Дамерау — Левенштейна
#### Расстояние Левенштейна
Википедия:
> **Расстояние Левенштейна**  — метрика, измеряющая разность между двумя последовательностями символов. Она определяется как минимальное количество односимвольных операций (а именно вставки, удаления, замены), необходимых для превращения одной последовательности символов в другую.

Пусть $`S_1`$ и $`S_2`$ — две строки (длиной $`M`$ и $`N`$ соответственно) над некоторым алфавитом, тогда расстояние Левенштейна $`d(S_1,S_2)`$ можно посчитать по следующей рекуррентной формуле $`d(S_1,S_2)=D(M,N)`$, где

![](source/img/levenshtein.svg)

где $`m(a,b)`$ равно нулю, если $`a=b`$ и 1 в противном случае.

Сложность по памяти: $`O(min(M,N))`$

Сложность по времени: $`O(M\cdot N)`$ (можно свести к $`O(k\cdot min(M, N))`$, если находить не более $`k`$ различий в словах)


#### Расстояние Дамерау — Левенштейна
Википедия:
> **Расстояние Дамерау — Левенштейна** — это мера разницы двух строк символов, определяемая как минимальное количество операций вставки, удаления, замены и транспозиции (перестановки двух соседних символов), необходимых для перевода одной строки в другую.


Расстояние Дамерау — Левенштейна между двумя строками $`a`$ в $`b`$ определяется функцией $`d_{a,b}(|a|,|b|)`$ как:

![](source/img/damerau-levensthein.svg)

где $`1_{(a_i \ne b_j)}`$ — это индикаторная функция, равная нулю при $`a_i = b_j`$  и 1 в противном случае.

Каждый рекурсивный вызов соответствует одному из случаев:

 - $`d_{a,b}(i-1,j)+1`$ соответствует удалению символа (из $`a`$ в $`b`$)
 - $`d_{a,b}(i,j-1)+1`$ соответствует вставке символа (из $`a`$ в $`b`$)
 - $`d_{a,b}(i-1,j-1)+1`$ соответствие или несоответствие, в зависимости от совпадения символов
 - $`d_{a,b}(i-2,j-2)+1`$ в случае перестановки двух последовательных символов

Сложность по памяти: $`O(min(M,N))`$

Сложность по времени: $`O(M\cdot N)`$ (можно свести к $`O(k\cdot min(M, N))`$, если находить не более $`k`$ различий в словах)

Вне зависимости от выбранной метрики и алгоритма её реализации стоит учитывать некоторые моменты, связанные с построением BK-tree:
 - для решения задачи необходим заранее заготовленный словарь слов, следовательно всегда будет затрачена память на хранение данного словаря
 - для считывания словаря нам потребуется $`O(n)`$ времени, где $`n`$ — мощность словаря(количество слов)
 - будем считать, что мощность словаря заранее известна и является константой
 - средняя длина слова в словаре L — тоже константа


#### Алгоритм построения BK-tree
Алгоритм построения дерева выполнен в виде рекурсивного алгоритма:
 1. Берётся слово из словаря
 2. Считается метрика между ним и текущей вершиной поддерева.  
 3. Если среди потомков вершины нет вершин с нашей метрикой, то наше слово становится новым потомком. Конец алгоритма.
 4. Иначе: текущей вершиной дерева становится вершина с такой же метрикой; перейти на п.2 




### Этап 2: Выполнение поисковых запросов

Введём **предел допуска** $`k=3`$. 
**Предел допуска** - это максимальное расстояние редактирования от слова с ошибкой до правильных слов в нашем словаре. Это значит, что мы допускаем, что пользователь допустил не более $`k`$ ошибок при написании слова. Следовательно, теперь вместо перебора всех его дочерних элементов мы будем перебирать только дочерние элементы, у которых метрика в диапазоне  $`[dist-k, dist + k]`$, где $`dist`$ — расстояние редактирования между словом в текущем узле и словом с ошибкой
Увеличение данного предела приведёт к увеличению времени работы программы, так как алгоритм будет обходить большее количество вершин в дереве.

Алгоритм поиска правильных слов похож на обход DFS(Depth-first search) по дереву с выборочным посещением дочерних узлов, вес ребер которых лежит в диапазоне $`[dist-k, dist + k]`$:
 1. Вычисляем расстояние редактирования $`dist`$. 
 2. Если $`dist=0`$, то алгоритм можно досрочно завершить, так как было найдено точное совпадение, значит на вход было изначально подано правильное слово
 3. Если $`dist\leqslant k`$, то добавляем слово в текущем узле в список правильных слов
 4. Перебираем все дочерние элементы, имеющие расстояние редактирования в диапазоне $`[dist-k, dist + k]`$


#### Временная сложность
Так как алгоритм построения BK-дерева не обеспечивает его сбалансированности, то сложность поиска в худшем: $`O(k\cdot min(L,L_0)\cdot n)`$, где $`L_0`$ — длина слова с ошибкой

#### Сложность по памяти
Для работы алгоритма поиска требуется столько же памяти, сколько и для вычисления метрики.
Сложность по памяти: $`O(min(L,L_0))`$
### Выбор алгоритма
В рамках данной задачи предоставляется выбор метрики, используемой при построении дерева и выполнении поиска. 
Если исходить из оценок сложности алгоритмов, то оба варианта являются одинаковыми. Однако на практике более 80% ошибок при наборе текста — это транспозиция, следовательно более точные результаты будет выдавать алгоритм, использующий расстояние Дамерау — Левенштейна.

