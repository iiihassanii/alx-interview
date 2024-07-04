#!/usr/bin/python3
"""_summary_

        Returns:
            _type_: _description_
        """
import sys


def print_usage():
    """_summary_
        """
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error():
    """_summary_
    """
    print("N must be a number")
    sys.exit(1)


def print_minimum_error():
    """_summary_
    """
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col, N):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_
        N (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N, solutions):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        N (_type_): _description_
        solutions (_type_): _description_
    """
    if row >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N):
    """_summary_

    Args:
        N (_type_): _description_
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error()

    if N < 4:
        print_minimum_error()

    nqueens(N)
