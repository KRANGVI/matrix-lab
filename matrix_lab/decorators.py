from functools import wraps
from .matrix_utils import validate_matrix
import time
def validate_square(func):
    @wraps(func)
    def obertka(matrix, *args, **kwargs):
        validate_matrix(matrix)
        if len(matrix[0]) != len(matrix):
            raise ValueError('Число столбцов должно совпадать с числом строк')
        a = func(matrix, *args, **kwargs)
        return a
    return obertka

def timer(func):
    @wraps(func)
    def obertka(*args, **kwargs):
        start = time.perf_counter()
        a = func(*args, **kwargs)
        finish = time.perf_counter()
        result = finish - start 
        print(result)
        return a
    return obertka
