import random
from typing import List, Tuple, Optional


def create_board(size: int) -> List[List[int]]:
    return [[0] * size for _ in range(size)]


def add_random_tile(
    board: List[List[int]], values: List[int] = [2, 4]
) -> List[List[int]]:
    # Add a random tile (2 or 4)
    empty_cells = [
        (i, j)
        for i in range(len(board))
        for j in range(len(board[0]))
        if board[i][j] == 0
    ]
    if not empty_cells:
        return board
    i, j = random.choice(empty_cells)
    new_board = [row[:] for row in board]  # Immutable copy
    new_board[i][j] = random.choice(values)
    return new_board


def initialize_game(size: int) -> Tuple[List[List[int]], int]:
    # start the game with a board and two random tiles.
    board = create_board(size)
    board = add_random_tile(board)
    board = add_random_tile(board)
    return board, 0  # Board and initial score


def compress_row(row: List[int]) -> Tuple[List[int], int]:
    non_zero = [x for x in row if x != 0]
    score = 0
    result = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            result.append(2 * non_zero[i])
            score += 2 * non_zero[i]
            i += 2
        else:
            result.append(non_zero[i])
            i += 1
    return result + [0] * (len(row) - len(result)), score


def move_left(board: List[List[int]]) -> Tuple[List[List[int]], int]:
    new_board = []
    total_score = 0
    for row in board:
        new_row, score = compress_row(row)
        new_board.append(new_row)
        total_score += score
    return new_board, total_score


def rotate_board(board: List[List[int]], times: int) -> List[List[int]]:
    result = board
    for _ in range(times):
        result = [list(row) for row in zip(*result[::-1])]
    return result


def move(board: List[List[int]], direction: str) -> Tuple[List[List[int]], int]:
    rotations = {"up": 1, "right": 2, "down": 3, "left": 0}
    n = rotations[direction]
    rotated = rotate_board(board, n)
    moved, score = move_left(rotated)
    result = rotate_board(moved, 4 - n)  # Rotate back
    return result, score


def is_game_over(board: List[List[int]]) -> bool:
    # Check if no more moves are possible.
    if any(0 in row for row in board):
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (j + 1 < len(board[0]) and board[i][j] == board[i][j + 1]) or (
                i + 1 < len(board) and board[i][j] == board[i + 1][j]
            ):
                return False
    return True


def has_won(board: List[List[int]], target: int = 2048) -> bool:
    # Check if the target tile (2048) is present.
    return any(target in row for row in board)
