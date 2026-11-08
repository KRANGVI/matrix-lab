from .matrix_utils import validate_matrix, apply_to_matrix
from .decorators import validate_square

OPS_COUNT = 0

def get_stats():
    return OPS_COUNT


def add(a, b):
    validate_matrix(a)
    validate_matrix(b)
    new_matrix = []
    if len(a) != len(b):
        raise ValueError('Размеры матриц должны совпадать')
    for i in range(len(a)):
        new_row = []
        if len(a[i]) != len(b[i]):
            raise ValueError('Размеры матриц должны совпадать')
        for j in range(len(a[i])):
            new_row.append((a[i][j]) + (b[i][j]))
        new_matrix.append(new_row)
    
    global OPS_COUNT
    OPS_COUNT += 1
    return new_matrix  


def subtract(a, b):
    validate_matrix(a)
    validate_matrix(b)
    new_matrix = []
    if len(a) != len(b):
        raise ValueError('Размеры матриц должны совпадать')
    for i in range(len(a)):
        new_row = []
        if len(a[i]) != len(b[i]):
            raise ValueError('Размеры матриц должны совпадать')
        for j in range(len(a[i])):
            new_row.append((a[i][j]) - (b[i][j]))
        new_matrix.append(new_row)

    global OPS_COUNT
    OPS_COUNT += 1

    return new_matrix  


def transpose(matrix):
    validate_matrix(matrix)
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append((matrix[j][i]))
        new_matrix.append(new_row)

    global OPS_COUNT
    OPS_COUNT += 1

    return new_matrix


def transpose_comprehension(matrix):
    validate_matrix(matrix)
    new_matrix = [[matrix[j][i] for j in range (len(matrix))] for i in range(len(matrix[0]))]

    global OPS_COUNT
    OPS_COUNT += 1
    
    return new_matrix


def scalar_multiply(matrix, k):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append((matrix[i][j]) * k)
        new_matrix.append(new_row)

    global OPS_COUNT
    OPS_COUNT += 1

    return new_matrix  


def _multiply(a, b):
    validate_matrix(a)
    validate_matrix(b)
    if len(a[0]) != len(b):
        raise ValueError('Число столбцов должно совпадать с числом строк')
    new_matrix = []
    for i in range(len(a)):
        new_row = []
        for k in range(len(b[0])):
            t = 0
            for j in range(len(a[0])):
                t += a[i][j] * b[j][k]
            new_row.append(t)
        new_matrix.append(new_row)
    return new_matrix


def multiply(a, b):
    result = _multiply(a, b)
    
    global OPS_COUNT
    OPS_COUNT += 1

    return result


def _identity(n):
    if n <= 0:
        raise ValueError('n - положительное число')
    matrix = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    return matrix


def identity(n):
    result = _identity(n)

    global OPS_COUNT
    OPS_COUNT += 1

    return result


@validate_square
def power(matrix, k, *, mod=None):

    def _power(matrix, k, *, mod=None):
        validate_matrix(matrix)

        if type(k) is not int:
            raise ValueError('k только целое число')

        if k < 0:
            raise ValueError('k требуется больше или равно нулю')
        
        if len(matrix[0]) != len(matrix):
            raise ValueError('Число столбцов должно совпадать с числом строк')

        if mod == 0:
            raise ValueError("модуль не может быть равен нулю")

        if k == 0:
            if mod is not None:
                return apply_to_matrix(_identity(len(matrix)), lambda x: x % mod)
            else:
                return _identity(len(matrix))
        
        if k == 1:
            if mod is not None:
                return apply_to_matrix(matrix, lambda x: x % mod)
            else:
                return matrix

        
        if mod is not None:
            matrix = apply_to_matrix(matrix, lambda x: x % mod)

        half_k = k // 2
        half_matrix = _power(matrix, half_k, mod=mod)
        half_matrix = _multiply(half_matrix, half_matrix)

        if mod is not None:
            half_matrix = apply_to_matrix(half_matrix, lambda x: x % mod)

        if k % 2 != 0:
            half_matrix = _multiply(half_matrix, matrix)
            if mod is not None:
                half_matrix = apply_to_matrix(half_matrix, lambda x: x % mod)

        return half_matrix
    result = _power(matrix, k, mod=mod)
    
    global OPS_COUNT
    OPS_COUNT += 1

    return result


def _determinant(matrix):
    validate_matrix(matrix)

    if len(matrix[0]) != len(matrix):
        raise ValueError('Число столбцов должно совпадать с числом строк')

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    minors = []
    for col in range(len(matrix)):
        new_matrix = []
        for i in range(1, len(matrix)):
            new_row = []
            for j in range(len(matrix[0])):
                if j != col:
                    new_row.append(matrix[i][j])
            new_matrix.append(new_row)
    
        minors.append((matrix[0][col]) * _determinant(new_matrix) * ((-1)**(col)))

    return sum(minors)


def determinant(matrix):
    result = _determinant(matrix)
    
    global OPS_COUNT
    OPS_COUNT += 1

    return result
