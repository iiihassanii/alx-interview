#!/usr/bin/python3
"""
0-main
"""


def row(tr):
    """_summary_

    Args:
        tr (_type_): _description_

    Returns:
        _type_: _description_
    """
    result = []
    for i in range(len(tr)):
        if i != 0:
            result.append(tr[i] + tr[i-1])
        else:
            result.append(1)
    result.append(1)
    return result


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    trianle = []
    tmp = [1]
    if n == 0:
        return trianle
    elif n == 1:
        trianle.append(tmp)
        return trianle

    trianle.append(tmp)
    i = 2
    for i in range(n - 1):
        tmp = row(tmp)
        trianle.append(tmp)

    return trianle
