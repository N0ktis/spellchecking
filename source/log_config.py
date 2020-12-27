import logging
from functools import wraps

logger_info = logging.getLogger("spellcheking_log_info")
logger_info.setLevel(logging.INFO)
logger_error = logging.getLogger("spellcheking_log_error")
logger_error.setLevel(logging.ERROR)

formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")

error_logs = logging.FileHandler('error_logs.log', 'a', 'utf-8')
error_logs.setFormatter(formatter)

info_logs = logging.FileHandler('info_logs.log', 'a', 'utf-8')
info_logs.setFormatter(formatter)

logger_info.addHandler(info_logs)
logger_error.addHandler(error_logs)



def proc_dict_logger_decorator(fun):
    @wraps(fun)
    def wrapper(*args):
        logger_info.info("Input dictionary processed successfully. Created BK-tree")
        return

    return wrapper


def check_word_logger_decorator(fun):
    @wraps(fun)
    def wrapper(*args):
        logger_info.info("All words checked and printed successfully")
        return

    return wrapper


def print_words_logger_decorator(fun):
    @wraps(fun)
    def wrapper(*args):
        logger_info.info("Word \"" + args[0] + "\" printed successfully")
        return

    return wrapper


def error_logger_decorator(fun):
    @wraps(fun)
    def wrapper(*args):
        checked_value = None
        try:
            checked_value = fun(*args)
        except TypeError as error:
            logger_error.error(error.args[0])
            raise TypeError(error.args[0])
        except FileNotFoundError as error:
            logger_error.error(error.args[1])
        except Exception as error:
            logger_error.error(error.args[0])
        return checked_value

    return wrapper
