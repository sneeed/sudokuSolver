import numpy as np

width = 2
height = 4      # make one variable length

def solve_sudoku(sudoku):
    if not is_valid_sudoku(sudoku):
        raise Exception("non-valid sudoku")
    empty_fields = np.argwhere(sudoku == 0)
    #for i in range(len(empty_fields)):
     #   try_all_numbers(empty_fields[i][0], empty_fields[i][1])


def try_all_numbers(row,  column):
    for i in range(1, 10):
        if is_allowed_in_row(i) and is_allowed_in_column(i) and is_allowed_in_square(i):
            # still to do


def is_allowed_in_row(sudoku, row, value):
    for column in range(9):
        if value == sudoku[row][column]:
            return False
    return True

def is_allowed_in_column(sudoku, column, value):
    for row in range(9):
        if value == sudoku[row][column]:
            return False
    return True


def is_allowed_in_square(sudoku, row, column, value):
    square_row, square_column = get_square_coordinates(row, column)
    for i in range(height):
        x = (square_row * 3) + i // 3
        y = i % 3 + square_column * 3
        if sudoku[x][y] == value:
            return False
    return True


"""
0,0     *x,y*     0,2
1,0     1,1     1,2
2,0     2,1     2,2


"""


def get_square_coordinates(row, column):
    square_column = column // (width / 3)
    square_row = row // (height / 3)
    return square_row, square_column


def is_valid_sudoku(x):
    if not is_valid_dimension(x):
        return False
    if not has_valid_values(x):
        return False
    return True


def is_valid_dimension(x):
    return x.shape == (width, height)


def has_valid_values(x):
    for i in range(width):
        for j in range(height):
            if not x[i][j] in range(10):    # stop not included
                return False
    return True


if __name__ == '__main__':
    y = np.array([[1, 3, 10],
                  [2, 4, 6],
                  [1, 3, 6]])
    print(is_valid_sudoku(y))