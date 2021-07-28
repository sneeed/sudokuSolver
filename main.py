import numpy as np

SIZE = 9


def solve_sudoku(sudoku):
    if not is_valid_sudoku(sudoku):
        raise Exception("non-valid sudoku")
    empty_fields = np.argwhere(sudoku == 0)
    print(empty_fields)
    candidates = np.zeros((SIZE, SIZE), dtype=list)
    for i in range(len(empty_fields)):
        row = empty_fields[i][0]
        column = empty_fields[i][1]
        print("Debug: Now testing row %s, column %s with value %s (must be 0)" % (row, column, sudoku[row][column]))
        # candidates = np.array
        # try_all_numbers(sudoku, row, column)
        candidates[row][column] = try_all_numbers(sudoku, row, column)
        # print("Debug: After retrieving one solution, sudoku is updated to:")
        # print_sudoku(sudoku)
        # print(candidates[0][1])

    # we have now our candidates, now we brute force a valid combination of all candidates
    indices_of_candidates = np.ones(len(empty_fields), dtype=int)
    # print(indices_of_candidates)
    for i in range(len(empty_fields)):
        for j in range(SIZE):
            (indices_of_candidates[i])++
            if is_valid_combination(sudoku, empty_fields, candidates, indices_of_candidates)
                solution = np.array(sudoku, copy=True)

                # fill solution with candidates
                for i in range(len(indices_of_candidates)):
                    row = empty_fields[i][0]
                    column = empty_fields[i][1]
                    solution[row][column] = candidates[row][column][indices_of_candidates[i]]

                print_sudoku(solution)



def is_valid_combination(sudoku, empty_fields, candidates, indices_of_candidates):
    solution = np.array(sudoku, copy=True)
    for i in range(len(indices_of_candidates)):
        row = empty_fields[i][0]
        column = empty_fields[i][1]
        solution[row][column] = candidates[row][column][indices_of_candidates[i]]
        if is_valid_solution(solution):
            return True
    return False

def is_valid_solution(sudoku):
    for row in range(SIZE):
        for column in range(SIZE):
            if is_allowed_in_row(sudoku, row, sudoku[row][column]) \
                and is_allowed_in_column(sudoku, column, sudoku[row][column]) \
                and is_allowed_in_square(sudoku, row, column, sudoku[row][column]):
                return True
    return False

def try_all_numbers(sudoku, row,  column):
    possibles = []
    for number in range(1, SIZE + 1):
        if is_allowed_in_row(sudoku, row, number) \
                and is_allowed_in_column(sudoku, column, number) \
                and is_allowed_in_square(sudoku, row, column, number):
            print("Debug: One possible solution: row: " + str(row) + ", column: " + str(column) + " is: " + str(number))
            possibles.append(number)
    if len(possibles) == 0:
        raise Exception("unsolvable sudoku")
    return possibles


def is_allowed_in_row(sudoku, row, value):
    for column in range(SIZE):
        if value == sudoku[row][column]:
            print("Debug: number " + str(value) + " is NOT allowed_in_row. " + str(value) + " already in row " + str(row) + ", column " + str(column))
            return False
    print("Debug: number " + str(value) + " is allowed_in_row.")
    return True


def is_allowed_in_column(sudoku, column, value):
    for row in range(SIZE):
        if value == sudoku[row][column]:
            print("Debug: number " + str(value) + " is NOT allowed_in_column. " + str(value) + " already in row " + str(row) + ", column " + str(column))
            return False
    print("Debug: number " + str(value) + " is allowed_in_column.")
    return True


def is_allowed_in_square(sudoku, row, column, value):    # this could be done more elegant with slices of
    # multi-dimensional subarrays
    square_row, square_column = get_square_coordinates(row, column)
    for i in range(SIZE):
        x = int((square_row * 3) + i // 3)
        y = int(i % 3 + square_column * 3)
        row_content = sudoku[y]
        if sudoku[x][y] == value:
            print("Debug: number " + str(value) + " is NOT allowed_in_square. " + str(value) + " already in row " + str(row) + ", column " + str(column))
            return False
    print("Debug: number " + str(value) + " is allowed_in_square.")
    return True


def get_square_coordinates(row, column):
    square_column = column // (SIZE / 3)
    square_row = row // (SIZE / 3)
    return square_row, square_column


def is_valid_sudoku(x):
    if not is_valid_dimension(x):
        raise Exception("non-valid dimension")
    if not has_valid_values(x):
        raise Exception("non-valid values")
    return True


def is_valid_dimension(x):
    return x.shape == (SIZE, SIZE)


def has_valid_values(x):
    for i in range(SIZE):
        for j in range(SIZE):
            if not x[i][j] in range(10):
                return False
    return True


def print_sudoku(sudoku):
    for i in range (SIZE):
        print("[", end='')
        for j in range(SIZE):
            if j < SIZE - 1:
                print(sudoku[i][j], ', ', end='', sep='')
            else:
                print(sudoku[i][j], end='', sep='')
        print("],")


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
    print_sudoku(s)
    print("is_valid_sudoku?")
    print(is_valid_sudoku(s))
    solve_sudoku(s)