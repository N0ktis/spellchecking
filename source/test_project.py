import os
import pytest
from main import init_bk_tree, check_words

DICT_FILE_PATH = 'tests_src\\dict_files\\russian_dict.txt'
METRIC_DICT_FILE_PATH = 'tests_src\\dict_files\\metric_dict.txt'
EMPTY_DICT_FILE_PATH = 'tests_src\\dict_files\\empty_dict.txt'
DICT_WITH_DUPLICATES_FILE_PATH = 'tests_src\\dict_files\\duplicate_dict.txt'
RESULT_FILE_PATH = 'output.txt'
BK_TREE = init_bk_tree(DICT_FILE_PATH)
K_ARG = '1'


@pytest.fixture(scope='function', autouse=False)
def delete_output_file():
    yield
    os.remove(RESULT_FILE_PATH)


@pytest.mark.usefixtures('delete_output_file')
def test_insert_letter():
    check_words(BK_TREE, 'tests_src\\input_files\\input_insert_letter.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_insert_letter.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_replacement_letter():
    check_words(BK_TREE, 'tests_src\\input_files\\input_replacement_letter.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_replacement_letter.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_delete_letter():
    check_words(BK_TREE, 'tests_src\\input_files\\input_delete_letter.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_delete_letter.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_transposition_letter():
    check_words(BK_TREE, 'tests_src\\input_files\\input_transposition_letter.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_transposition_letter.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_metrics():
    bk_tree = init_bk_tree(METRIC_DICT_FILE_PATH)
    check_words(bk_tree, 'tests_src\\input_files\\input_metrics.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_metrics.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_empty_dict():
    bk_tree = init_bk_tree(EMPTY_DICT_FILE_PATH)
    check_words(bk_tree, 'tests_src\\input_files\\input_empty_dict.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_empty_dict.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_dict_with_duplicates():
    bk_tree = init_bk_tree(DICT_WITH_DUPLICATES_FILE_PATH)
    check_words(bk_tree, 'tests_src\\input_files\\input_dict_with_duplicates.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_dict_with_duplicates.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_full_compliance():
    check_words(BK_TREE, 'tests_src\\input_files\\input_full_compliance.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_full_compliance.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_no_match():
    check_words(BK_TREE, 'tests_src\\input_files\\input_no_match.txt', RESULT_FILE_PATH, K_ARG)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_no_match.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_big_k():
    # k=10 является уже большим, так как позволят получить любое слово длины <20, а таких в русском языке большинство
    k_arg = '10'
    check_words(BK_TREE, 'tests_src\\input_files\\input_for_test_k.txt', RESULT_FILE_PATH, k_arg)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_big_k.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_zero_k():
    k_arg = '0'
    check_words(BK_TREE, 'tests_src\\input_files\\input_for_test_k.txt', RESULT_FILE_PATH, k_arg)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_zero_k.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


@pytest.mark.usefixtures('delete_output_file')
def test_default_k():
    check_words(BK_TREE, 'tests_src\\input_files\\input_for_test_k.txt', RESULT_FILE_PATH)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_default_k.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()


def test_negative_k():
    k_arg = '-1'
    try:
        check_words(BK_TREE, 'tests_src\\input_files\\input_for_test_k.txt', RESULT_FILE_PATH, k_arg)
    except TypeError:
        assert True


def test_not_integer_k():
    k_arg = '1.2'
    try:
        check_words(BK_TREE, 'tests_src\\input_files\\input_for_test_k.txt', RESULT_FILE_PATH, k_arg)
    except TypeError:
        assert True


def test_dict_file_not_exist():
    try:
        init_bk_tree('tests_src\\dict_files\\peace_was_never_an_option.txt')
    except FileNotFoundError:
        assert True


def test_input_file_not_exist():
    try:
        check_words(BK_TREE, 'tests_src\\input_files\\may_the_force_be_with_you.txt', RESULT_FILE_PATH, K_ARG)
    except FileNotFoundError:
        assert True


'''
@pytest.mark.usefixtures('delete_output_file')
def stress_test():
    k_arg = '4'
    bk_tree = init_bk_tree('tests_src\\dict_files\\STRESS.txt')
    check_words(bk_tree, 'tests_src\\input_files\\input_stress.txt', RESULT_FILE_PATH, k_arg)
    with open(RESULT_FILE_PATH, encoding='utf-8') as output, \
            open('tests_src\\answer_files\\answer_stress.txt', encoding='utf-8') as answer:
        assert output.read() == answer.read()
'''
