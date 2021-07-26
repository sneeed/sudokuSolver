import numpy as np

length = 9


def solve_sudoku(sudoku):
    if not is_valid_sudoku(sudoku):
        raise Exception("non-valid sudoku")
    solution = sudoku
    empty_fields = np.argwhere(sudoku == 0)
    for i in range(len(empty_fields)):
        print("Debug: Now testing row %s, column %s" % (empty_fields[i][0], empty_fields[i][1]))
        solution[empty_fields[i][0]][empty_fields[i][1]] = \
            try_all_numbers(sudoku, empty_fields[i][0], empty_fields[i][1])


def try_all_numbers(sudoku, row,  column):
    for number in range(1, length + 1):
        if is_allowed_in_row(sudoku, row, number) \
                and is_allowed_in_column(sudoku, column, number) \
                and is_allowed_in_square(sudoku, row, column, number):
            print("Debug: Solution: row: " + str(row) + ", column: " + str(column) + " is: " + str(number))
            return number
    raise Exception("unsolvable sudoku")


def is_allowed_in_row(sudoku, row, value):
    for column in range(length):
        if value == sudoku[row][column]:
            return False
    print("Debug: number " + str(value) + " is allowed_in_row.")
    return True


def is_allowed_in_column(sudoku, column, value):
    for row in range(length):
        if value == sudoku[row][column]:
            return False
    print("Debug: number " + str(value) + " is allowed_in_column.")
    return True


def is_allowed_in_square(sudoku, row, column, value):
    square_row, square_column = get_square_coordinates(row, column)
    for i in range(length):
        x = int((square_row * 3) + i // 3)
        y = int(i % 3 + square_column * 3)
        row_content = sudoku[y]
        if sudoku[x][y] == value:
            return False
    print("Debug: number " + str(value) + " is allowed_in_square.")
    return True


def get_square_coordinates(row, column):
    square_column = column // (length / 3)
    square_row = row // (length / 3)
    return square_row, square_column


def is_valid_sudoku(x):
    if not is_valid_dimension(x):
        raise Exception("non-valid dimension")
    if not has_valid_values(x):
        raise Exception("non-valid values")
    return True


def is_valid_dimension(x):
    return x.shape == (length, length)


def has_valid_values(x):
    for i in range(length):
        for j in range(length):
            if not x[i][j] in range(10):
                return False
    return True


if __name__ == '__main__':
    s = np.array([[2, 0, 6, 0, 5, 0, 1, 9, 0],
                  [0, 8, 0, 4, 0, 0, 0, 0, 0],
                  [9, 0, 0, 2, 0, 6, 0, 4, 7],
                  [1, 0, 0, 0, 4, 0, 0, 0, 6],
                  [7, 9, 8, 6, 0, 0, 0, 0, 5],
                  [0, 5, 0, 0, 0, 8, 9, 2, 3],
                  [0, 0, 0, 0, 1, 3, 0, 0, 4],
                  [4, 0, 3, 8, 0, 9, 5, 6, 0],
                  [5, 2, 1, 7, 0, 0, 8, 0, 0]
                  ])
    print("is_valid_sudoku?")
    print(is_valid_sudoku(s))
    solve_sudoku(s)