import sys
def validate_matrix(matrix):
    if len(matrix) == 0:
        raise ValueError('Матрица пустая')
    if len(matrix[0]) == 0:
        raise ValueError('Строка пустая')
    matrix_len_example = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != matrix_len_example:
            raise ValueError('Строки разной длинны')
    return

def apply_to_matrix(matrix, func):
    validate_matrix(matrix)
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(func(matrix[i][j]))
        new_matrix.append(new_row)
    return new_matrix

def read_matrix_from_console():
    n, m = map(int, sys.stdin.readline().split())
    if n <= 0 or m <=0:
        raise ValueError('вводные данные должны быть больше нуля')
    matrix = []
    for i in range(n):
        row = list(map(float, sys.stdin.readline().split()))
        if len(row) != m:
            raise ValueError('Количество элементов в строке не совпадает с заданным')
        else:
            matrix.append(row)
    return matrix


def read_matrix_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        n, m = map(int, file.readline().split())
        if n <= 0 or m <=0:
            raise ValueError('вводные данные должны быть больше нуля')
        matrix = []
        for i in range(n):
            row = list(map(float, file.readline().split()))
            if len(row) != m:
                raise ValueError('Количество элементов в строке не совпадает с заданным')
            else:
                matrix.append(row)
    return matrix

def print_matrix(matrix):
    from .matrix_io import flatten
    validate_matrix(matrix)
    width = 0
    for value in flatten(matrix):
        width = max(len(str(value)), width)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(str(matrix[i][j]).rjust(width), end=" ")
        print()


def write_matrix_to_file(matrix, filename):
    from .matrix_io import flatten
    validate_matrix(matrix)
    width = 0
    for value in flatten(matrix):
        width = max(len(str(value)), width)
    with open(filename, "w", encoding="utf-8") as file:
        n = len(matrix)
        m = len(matrix[0])
        if n <= 0 or m <=0:
            raise ValueError('вводные данные должны быть больше нуля')
        file.write(f'{n} {m}\n')
        
        for i in range(n):
            if len(matrix[i]) != m:
                raise ValueError('Количество элементов в строке не совпадает с заданным')
            else:
                a = []
                for j in range(m):
                    a.append((str(matrix[i][j]).rjust(width)))
            
                file.write((' '.join(a)))
                file.write(f'\n')

def matrix_stats(matrix):
    from .matrix_io import flatten
    a = list(flatten(matrix))
    min_matrix = min(a)
    max_matrix = max(a)
    sum_matrix = sum(a)
    unique = len(set(a))
    max_count = 0
    for i in range(len(a)):
        count = 0
        for j in range(i, len(a) - 1):
            if a[i] == a[j + 1]:
                count += 1
        if count >= max_count:
            max_count = count
            most_common = a[i]
    return {"min": min_matrix, "max": max_matrix, "sum": sum_matrix, "unique_count": unique, "most_common": most_common}


def min_max_positions(matrix):
    validate_matrix(matrix)
    minimum = []
    maximum = []
    for i in range(len(matrix)):
        minimum.append(min(matrix[i]))

    for i in range(len(matrix)):
        maximum.append(max(matrix[i]))

    new_matrix = []
    x = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min(minimum) and x == 0:
                new_matrix.append((i, j))
                x += 1 

    y = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == max(maximum) and y == 0:
                new_matrix.append((i, j))
                y += 1

    return tuple(new_matrix)
