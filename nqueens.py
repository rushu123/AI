def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, N):
    if col >= N:
        return True
    
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            
            if solve_n_queens_util(board, col + 1, N):
                return True
            
            board[i][col] = 0
    
    return False

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False
    
    print("Solution:", end=' ')
    for i in range(N):
        for j in range(N):
            if board[j][i] == 1:
                print(j, end=' ')
    print("\nThe Matrix Representation:")
    print_solution(board)
    return True

def print_solution(board):
    N = len(board)
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

# Example usage
N = int(input("Enter N Queens Problem: "))
solve_n_queens(N)
