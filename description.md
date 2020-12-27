# Описание программы
## Файлы проекта
### Файл [Word.py](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/Word.py)
Содержит описание и реализацию класса Word.

Класс отвечает за хранение строки в узле BK-дерева и данных о его детях.

**Атрибуты объекта класса Word:**
- `self.word` - строка(слово), хранимая в узле BK-дерева;
- `self.children` - словарь потомков текущего узла (key - дистанция редактирования от атрибута `self.word` текущего узла, до атрибута `self.word` потомка; value - ссылка на объект класса Word);


### Файл [BK_tree.py](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/BK_tree.py)
Содержит реализацию стуктуры BK-дерева.

Класс отвечает за создание структуры BK-дерева и поиска по нему.

**Атрибуты объекта класса BK_tree:**
- `self.__root` - содержит указатель на объект класса Word, который явлется корнем BK-дерева;

**Функции класса BK_tree:**
- `def insert_word(self, word: str, vertex=None) -> None` - функция рекурсивно добавляет новую вершину в BK-дерево;
- `def autocorrection(self, incorrect_word: str, k=3) -> list` - функция определяет набор слов из BK-дерева, правописание которых схоже со входным словом; возвращает список слов, правописание которых похоже на входное; если входное слово написано правильно - возвращает "ok", если не удалось найти похожие слова - возвращает - "?";
- `def __damerau_levenshtein(word1: str, word2: str) -> int` - статическая функция, определяет расстояние Дамерау-Левенштейна между двумя строками; используется корректный(не упрощённый) алгоритм расчёта; возвращает расстояние редактирования между `word1` и `word2`;

### Файл [log_config.py](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/log_config.py)
Содержит настройки для осуществления логгирования. 

**Функции:**
- `def logger_decorator_maker(id=None)` - функция является фабрикой декораторов; декораторы генерируются в зависимости от переданного значения id;


### Файл [main.py](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/main.py)


**Функции:**
- `def init_bk_tree(dict_file_path: str)` - функция создаёт объект класса BK_tree на основе переданного словаря; возвращает объект класса BK_tree;
- `def check_word(bk_tree, word: str, k: int) -> list` - функция вызывает метод autocorrection у объекта класса BK_tree; возвращает то же самое, что и функция autocorrection;
- `def check_words(bk_tree, check_file_path: str, result_file_path: str, k_arg=None)` - Функция считывает из файла со словами для проверки значение и отправлет его в функцию check_word; полученный результат печатеся в выходной файл(если он не существет - создаётся);
- `def print_word(word: str, answer: list, out_file)` - функция печатает переданные параметры в установленном формате;

Каждая функция обёрнута в генератор декораторов `logger_decorator_maker()`:
- `def init_bk_tree(dict_file_path: str)` - id='init';
- `def check_word(bk_tree, word: str, k: int) -> list` - id='check word';
- `def check_words(bk_tree, check_file_path: str, result_file_path: str, k_arg=None)` - id='check file';
- `def print_word(word: str, answer: list, out_file)` - id='print word result';

## Оценка сложности работы алгоритма поиска
### Время
Так как BK-дерево не является самобалансирующимся деревом, то в худшем случае вставка и поиск будут производиться за $`O(n)`$, а в среднем за $`O(\log n)`$

Временная сложность вычисления расстояния Дамерау-Левенштейна: $`O(M\cdot N)`$, где $`M`$ и $`N`$ - длины поданных строк

**Итог:** $`O(n+M\cdot N)`$

### Дополнительная память
Память, необходимая для хранения $`n`$ слов в BK-дереве: $`O(n)`$

Память, необходимая для вычисления расстояния Дамерау-Левенштейна: $`O(M\cdot N)`$, где $`M`$ и $`N`$ - длины поданных строк

Память, необходимая для рекурсивного добавления в дерево: $`O(h)`$, где $`h`$ - глубина дерева

**Итог:** $`O(n+M\cdot N+h)`$