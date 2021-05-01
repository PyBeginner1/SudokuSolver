#Step 1: Find empty place which is represented by -1
#Step 2: Make a guess
#Step 3: Check if its a valid guess
#Step 4: recursively call our function
#Step 5: If guess doesnt solve the puzzle
#Step 6: If none of our combinations work, puzzle cant be solved


def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None                   #it means that puzzle is filled


def is_valid(puzzle,guess, row, col):
    #check if guess is valid in row, col, 3x3
    #Step1: row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #Step2: Check col
    col_vals=[puzzle [i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #Step 3: check 3x3--> we need to fid starting index of row & col
    row_start=(row//3) * 3      #1//3 =0 *3 =0, 5//3 = 1 *3 =3, 7//3 = 2 * 3=6.
    col_start=(col//3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def sudoku_solver(puzzle):
    #choose a place on puzzle to make a guess
    row, col= find_next_empty(puzzle)
    #if there is no place left to input then it is valid
    if row is None:
        return True
    #Step2: take a guess from 1 to 9
    for guess in range(1,10):
        #Step3: Check if its valid
        if is_valid(puzzle,guess, row, col):
            #if guess is valid place it in the puzzle
            puzzle[row][col] = guess
            #Step 4: Recursively call your function
            if sudoku_solver(puzzle):
                return True

        #Step 5: backtracking for wrong guess
        puzzle[row][col] = -1               #resetting the value

    #Step 6: puzzle is not solvable after trying every combination of numbers in range
    return False

if __name__ == '__main__':4
    example_board = [
        [-1,  7, -1,   -1, -1, 8,   -1, -1, -1],
        [-1, -1, 2,   -1, -1, -1,   -1,  1, 7],
        [-1, -1, -1,  -1, 5, -1,   -1, -1, -1],

        [-1, 9, -1,   -1, -1, -1,   -1,  6, -1],
        [-1, 2,  7,   -1, -1,  9,    -1, -1, -1],
        [-1, -1, 3,    8, -1,  7,   -1,  5,  9],

        [-1, -1, -1,   1, -1, -1,   -1, -1, 3],
        [-1, -1, -1,   9, -1, -1,   -1, -1, -1],
        [6, 5, -1,    -1, -1, -1,    2,  9, -1]
    ]
    print(sudoku_solver(example_board))
    print(example_board)