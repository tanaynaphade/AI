def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def n_queen(board, row, n):
    if row >= n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if n_queen(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def main():
    n = int(input("Enter number of Queens: "))
    board = [[0 ] * n for _ in range(n)]
    if n_queen(board, 0, n):
        for row in board:
            for cell in row:
                print(cell, end=" ")
            print()
    else:
        print("Solution does not exist!")

if __name__ == "__main__":
    main()
