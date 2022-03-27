import inspect
from inspect import signature
from datetime import date, datetime
import os


def parametrized_decor(parameter):
    def logger(old_function):
        def new_function(*args, **kwargs):
            path = parameter
            result = old_function(*args, **kwargs)
            with open(path, "a", encoding="utf-8") as f:
                f.write(
                    f"Дата:{datetime.now()}, Имя файла: {old_function.__name__}, Аргументы: {args, kwargs},"
                    f"Возвращаемое значение: {result}, Путь к 'log' файлу: {path} \n")
            return result

        return new_function

    return logger
