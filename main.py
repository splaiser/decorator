import inspect
from inspect import signature
from datetime import date, datetime
import os


def logger(old_function):
    def new_function(*args, **kwargs):
        logfile = "logfile.txt"
        result = old_function(*args, **kwargs)
        with open(logfile, "a", encoding="utf-8") as f:
            f.write(
                f"Дата:{datetime.now()}, Имя файла: {old_function.__name__}, Аргументы: {args, kwargs},"
                f"Возвращаемое значение: {result}, ЛОГ: {os.path.abspath(logfile)} \n")
        return result

    return new_function
