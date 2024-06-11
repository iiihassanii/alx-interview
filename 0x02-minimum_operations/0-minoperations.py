#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
 Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n: int) -> int:
    """_summary_"""
    if n <= 1 or type(n) is not int:
        return 0

    counter = 2
    copy = "H"
    string = "HH"
    flag = 0
    while len(string) != n:
        if n % len(string) == 0:
            copy = string
            string += copy
            counter += 2
            flag = 1
        elif flag == 1:
            string += copy
            counter += 1
        else:
            string = string + copy
            counter += 1
    return counter
