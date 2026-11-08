from .matrix_ops import transpose, transpose_comprehension, multiply,power, determinant
from .matrix_io import diagonal, spiral
from .matrix_utils import read_matrix_from_file, read_matrix_from_console, write_matrix_to_file
from .decorators import timer

matrix = None

timer_determinant = timer(determinant)

while True:
    a = input(f'1       ← выбрать ввод матрицы\n2       ← выбрать матрицу из файла\n3       ← транспонирование\n4       ← умножение\n5       ← возведение матрицы в степень\n6       ← Вычислить определитель\n7       ← главная диагональ\n8       ← спираль\n9       ← Записать матрицу в файл\n33       ← демонстрация power с mod\n10      ← выход\n')
    
    if a == '10':
        print("Выход")
        break
    
    if a == '1':
        print(f"Ввод матрицы, введите размеры, а затем строки матрицы\n")
        try:
            matrix = read_matrix_from_console()
            print(matrix)
        except ValueError as error:
            print('Ошибка ввода')
    
    if a == '2':
        try:
            filename = input(f"Введите путь до матрицы:\n")
            matrix = read_matrix_from_file(filename)
            print(matrix)
        except FileNotFoundError:
            print("файл не найден")
        except OSError as error:
            print(f"Ошибка чтения файла: {error}")
        except ValueError as error:
            print(f"Ошибка в данных матрицы: {error}")

    if a == '3':
        if matrix is None:
            print('нет матрицы')

        else:
            b = input("Какой способ транспонирования? 1 - циклы 2 - списочное выражение\n")
            if b == '1':
                matrix = transpose(matrix)
                print(matrix)
            elif b == '2':
                matrix = transpose_comprehension(matrix)
                print(matrix)
            else:
                print("Способ выбран неверно\n")

    if a == '4':
        if matrix is None:
            print('Нет матрицы')

        else:
            #точно ли пользователю вводить вторую матрицу исключительно из консоли? Может разбить варианты? хорошо, оставлю как напоминание
            print('Введите матрицу:\n')
            try:
                second_matrix = read_matrix_from_console()
                matrix = multiply(matrix, second_matrix)
                print(matrix)
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")

    if a == '5':
        if matrix is None:
            print('Нет матрицы')

        else:
            try:
                k = int(input('Введите степень возведения:\n'))
                matrix = power(matrix, k)
                print(matrix)
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")

    if a == '6':
        if matrix is None:
            print('Нет матрицы')

        else:
            try:
                result = timer_determinant(matrix)
                print(result)
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")

    if a == '7':
        if matrix is None:
            print('Нет матрицы')

        else:
            try:
                result = list(diagonal(matrix))
                print(result)
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")

    if a == '8':
        if matrix is None:
            print('Нет матрицы')

        else:
            try:
                result = list(spiral(matrix))
                print(result)
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")

    if a == '9':
        if matrix is None:
            print('Нет матрицы')

        else:
            try:
                filename = input(f"Введите путь для вывода:\n")
                write_matrix_to_file(matrix, filename)
                print(read_matrix_from_file(filename))
                print('Матрица выше была успешно записана в файл')
            except ValueError as error:
                print(f"Ошибка в данных матрицы: {error}")            
            except OSError as error:
                print(f"Ошибка в записи матрицы: {error}")

    if a == '33':
        print(power([[2]], k=3, mod=5))

    if a not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '33'):
        print("Пункт меню введен неверно")

