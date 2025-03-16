from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cash_dict = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if args in cash_dict:
            print("Getting from cache")
            return cash_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cash_dict[args] = result
            return result
    return wrapper
