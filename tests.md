**Содержание страницы**

[[_TOC_]]

#  Тестирование
[**Файл с тестами**](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/test_project.py)

Тестирование проиходит с использованием модуля PyTest версии 6.2.0


## [Данные для Тестирования](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src)

Все текстовые файлы записаны с применением кодировки utf-8

[**Словари**](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/dict_files)
- `russian_dict.txt` содержит 162.254 слова русского языка, включая имена собственные(среднее время построения BK-дерева по такому словарю - 2 мин)
- `empty_dict.txt` пустой файл для проверки вывода алгоритма в случае пустого словаря
- `duplicate_dict.txt` словарь содержащий дупликаты своих слов
- `metric_dict.txt` словарь со словами, подобранными для тестирования явлется ли BK-дерево метрическим
- `STRESS.txt` содержит 1.532.629 слов русского языка(включая редкоиспользуемые слова, имена собственные, все части речи и термины) во всех возможных речевых формах. Используется только для стресс-теста(среднее время построения BK-дерева по такому словарю - 27 мин). Не рекомендуется для использования на практике, так как может содержать слова, написание которых совпадает с неправильным написанием слов, подразумеваемых пользователем.
**Пример:** _гулят_  (от глагола гу́лить — стадия доречевого развития ребёнка, следующая за криком и предшествующая лепету), хотя пользователь хотел написать _гулять_

[**Исходные данные**](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files)

[**Ответы**](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files)


## Тест: вставка пропущеной буквы в слово
`def test_insert_letter()`

Проверка вывода алгоритма в случае если в словах пропущена какая-либо буква

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_insert_letter.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_insert_letter.txt)

## Тест: замена неправильной буквы в слове
`ddef test_replacement_letter()`

Проверка вывода алгоритма в случае если в словах неправильно написана какая-либо буква

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_replacement_letter.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_replacement_letter.txt)

## Тест: удаление лишней буквы из слова
`def test_delete_letter()`

Проверка вывода алгоритма в случае если в словах добалена какая-либо лишняя буква

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_delete_letter.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_delete_letter.txt)

## Тест: транспозиция букв в слове
`def test_transposition_letter()`

Проверка вывода алгоритма в случае если в словах есть транспозиция смежных букв

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_transposition_letter.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_transposition_letter.txt)

## Тест: явлется ли BK-дерево метрическим
`def test_metrics()`

Проверка соблюдения аксиомы треугольника в BK-дереве с использованием при построении метрики Дамерау-Левенштейна

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/metric_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_metrics.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_metrics.txt)

## Тест: поведение алгоритма при подаче на вход пустого словаря
`def test_empty_dict()`

Проверка вывода алгоритма при пустом BK-дереве.

**Формате вывода:** <слово> -?

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/empty_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_empty_dict.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_empty_dict.txt)

## Тест: поведение алгоритма при подаче на вход словаря с дупликатами
`def test_dict_with_duplicates()`

Проверка вывода алгоритма при подаче на вход словаря с дупликатами. При выводе, если найдена подходящая замена, должно выводиться только одно слово.

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/duplicate_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_dict_with_duplicates.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_dict_with_duplicates.txt)

## Тест: выявление полных совпадений входных слов со словами словаря
`def test_full_compliance()`

Проверка вывода алгоритма при нахождении входного слова в словаре.

**Формат вывода:** <слово> - ok

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_full_compliance.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_full_compliance.txt)

## Тест: отстутвие рекомендации для замены неправильных слов
`def test_no_match()`

Проверка вывода алгоритма при отсутствии в словаре подходящей замены для входного слова.

**Формат вывода:** <слово> -?

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_no_match.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_no_match.txt)

## Тест: вывод алгоритма при большом расстоянии редактирования $`k`$
`def test_big_k()`

При запуске программы в параметрах указывается расстояние редактирования $`k=10`$ (k=10 является уже большим, так как позволят получить любое слово длины <20, а таких в русском языке большинство).

- расстояние редактирования `k=10`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_for_test_k.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_big_k.txt)

## Тест: вывод алгоритма при расстоянии редактирования $`k`$ равном 0
`def test_zero_k()`

При запуске программы в параметрах указывается расстояние редактирования $`k=0`$. При таком расстоянии редактирования алгоритм выдаст только точные совпадения.

- расстояние редактирования `k=0`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_for_test_k.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_zero_k.txt)

## Тест: вывод алгоритма при расстоянии редактирования $`k`$ заданным по умолчанию
`def test_default_k()`

При запуске программы мы не указываем в параметрах расстояние редактирования. По логике программы в таком случае будет использоваться расстояние редактирования $`k=3`$.

- расстояние редактирования `k=3`(задано по умолчанию)
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_for_test_k.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_default_k.txt)

## Тест: поведение программы при отрицательном расстоянии редактирования $`k`$
`def test_negative_k()`

При запуске программы мы указываем в параметрах отрицательное расстояние редактирования. Программа должна завершиться с ошибкой и сделать запись в файл `error_log.log`

- расстояние редактирования `k=-1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_for_test_k.txt)


## Тест: поведение программы при вещественном расстоянии редактирования $`k`$
`def test_not_integer_k()`

При запуске программы мы указываем в параметрах вещественное расстояние редактирования. Программа должна завершиться с ошибкой и сделать запись в файл `error_log.log`

- расстояние редактирования `k=1.2`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_for_test_k.txt)

## Тест: поведение программы в случае неправильно заданного пути до словаря
`def test_dict_file_not_exist()`

При запуске программы мы указываем в параметрах путь до словаря, которого не существет. Программа должна завершиться с ошибкой и сделать запись в файл `error_log.log`

- Указывается какое-либо имя несуществующего текстового файла

## Тест: поведение программы в случае неправильно заданного пути до файла со словами на проверку
`def test_input_file_not_exist()`

При запуске программы мы указываем в параметрах путь до файла со словами для проверки, которого не существет. Программа должна завершиться с ошибкой и сделать запись в файл `error_log.log`

- расстояние редактирования `k=1`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/russian_dict.txt) 
- Указывается какое-либо имя несуществующего текстового файла


## Тест: СТРЕСС-ТЕСТ
`def stress_test()`

**ВНИМАНИЕ!**

**Данный тест рекомендуется запускать только в научных целях.** 

**Тест предназначен только для практической оценки времени работы алгоритма на очень больших объёмах данных. Используется файл со словами на проверку, содержащий 20.000.000 слов с различными вариациями написания (в том числе корректные слова и слова, не содержащиеся в словаре).**

**Рекомендуется использовать мощный компьютер.**


По умолчанию данный тест закомментирован.

- расстояние редактирования `k=4`
- [Словарь](https://bmstu.codes/a.zhurin/spellchecking/-/blob/master/source/tests_src/dict_files/STRESS.txt) 
- [Исходные данные](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/input_files/input_stress.txt)
- [Ответ](https://bmstu.codes/a.zhurin/spellchecking/-/tree/master/source/tests_src/answer_files/answer_stress.txt)

