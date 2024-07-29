#!/usr/bin/python3

"""
    Island Perimeter
"""


def island_perimeter(grid):
    """
    Island Perimeter
    """

    length = len(grid)
    counter = 0

    for row in range(length):
        for col in range(length):
            if grid[row][col]:
                if row > 0 and grid[row - 1][col] == 0:
                    counter += 1
                if row < length and grid[row + 1][col] == 0:
                    counter += 1
                # check sides
                if col > 0 and grid[row][col - 1] == 0:
                    counter += 1
                if col < length and grid[row][col + 1] == 0:
                    counter += 1
    return counter
