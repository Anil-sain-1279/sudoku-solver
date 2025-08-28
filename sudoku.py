def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    for i in range(len(board[0])):
        if board[row][i] == num and i != col:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False
    # Check box
    x = col // 3
    y = row // 3
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True  # Solved
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0

    return False
sudoku_board = [
    [9, 0, 0, 0, 0, 8, 1, 0, 5],
    [0, 8, 5, 0, 2, 0, 0, 7, 0],
    [0, 7, 4, 0, 0, 1, 0, 9, 0],
    [0, 0, 6, 0, 0, 0, 0, 1, 0],
    [2, 0, 8, 0, 0, 5, 9, 0, 6],
    [0, 5, 0, 0, 0, 0, 0, 2, 4],
    [0, 0, 1, 0, 0, 4, 0, 0, 2],
    [6, 0, 0, 0, 0, 0, 3, 8, 0],
    [8, 0, 7, 0, 0, 0, 0, 0, 0]
]

print("Initial Sudoku Board:")
print_board(sudoku_board)

solve(sudoku_board)

print("\nSolved Sudoku Board:")
print_board(sudoku_board)

