from .matrix_utils import validate_matrix, read_matrix_from_file
import os

def flatten(matrix):
    validate_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            yield matrix[i][j]


def diagonal(matrix):
    validate_matrix(matrix)
    for i in range(min(len(matrix), len(matrix[0]))):
        yield matrix[i][i] 


def spiral(matrix):
    validate_matrix(matrix)
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            yield (matrix[top][j])
        top += 1

        for k in range(top, bottom + 1):
            yield (matrix[k][right])
        right -= 1

        if top <= bottom and left <= right:
            for j in range(right, left - 1, -1):
                yield (matrix[bottom][j])
            bottom -= 1
        
        if top <= bottom and left <= right:
            for k in range(bottom, top - 1, -1):
                yield (matrix[k][left])
            left += 1


def matrices_generator(folder):
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
    
        if name.endswith(".txt") and os.path.isfile(path):
            yield read_matrix_from_file(path)
