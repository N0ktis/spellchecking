import re
import sys
from BK_tree import BK_tree
from log_config import proc_dict_logger_decorator, check_word_logger_decorator, print_words_logger_decorator, \
    error_logger_decorator


@error_logger_decorator
@proc_dict_logger_decorator
def init_bk_tree(dict_file_path: str):
    """
    Функция создаёт объект класса BK_tree на основе переданного словаря
    :param dict_file_path: пуст к файлу со входным словарём
    :return: объект класса BK_tree
    """
    bk_tree = BK_tree()
    with open(dict_file_path, encoding='utf-8') as dict_file:
        for word in dict_file:
            if word == '\n':
                continue
            bk_tree.insert_word(word[:-1])
    return bk_tree


@error_logger_decorator
@check_word_logger_decorator
def check_words(bk_tree, check_file_path: str, result_file_path: str, k_arg: str):
    """
    Функция считывает из файла со словами для проверки значение и отправлет его в функцию check_word;
    полученный результат печатеся в выходной файл(если он не существет - создаётся)
    :param bk_tree: объект класса BK_tree
    :param check_file_path: путь к файлу со словамти на проверку
    :param result_file_path: путь к файлу для вывода результата работы
    :param k_arg: максимальное расстояние редактирования
    :return: None
    """
    if re.search('^\d+$', k_arg) is not None:
        k = int(k_arg)
    else:
        raise TypeError("Parameter k is not a positive integer")
    with open(check_file_path, encoding='utf-8') as check_file, \
            open(result_file_path, 'a', encoding='utf-8') as result_file:
        for word in check_file:
            if word == '\n':
                continue
            print_word(word[:-1], bk_tree.autocorrection(word, k), result_file)


@print_words_logger_decorator
def print_word(word: str, answer: list, out_file):
    """
    Функция печатает переданные параметры в установленном формате
    :param word: слово, поданное на проверку
    :param answer: список, полученный после выполнения функции autocorrection класса BK_tree
    :param out_file: дескриптор файла для записи
    :return: None
    """
    if len(answer) == 0:
        print(word, '-?', file=out_file)
    else:
        if answer[0] == word:
            print(word, '- ok', file=out_file)
        else:
            answer.sort()
            print(word, '->', ', '.join(answer), file=out_file)


if __name__ == '__main__':
    dict_file_path = sys.argv[1]
    check_file_path = sys.argv[2]
    result_file_path = sys.argv[3]
    bk_tree = init_bk_tree(dict_file_path)
    if len(sys.argv) == 5:
        k_arg = sys.argv[4]
        check_words(bk_tree, check_file_path, result_file_path, k_arg)
    else:
        check_words(bk_tree, check_file_path, result_file_path, '3')  # значение по умолчанию
