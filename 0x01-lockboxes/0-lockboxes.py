#!/usr/bin/python3
"""_summary_
    """


def canUnlockAll(boxes):
    """_summary_

    Args:
        boxes (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(boxes) == 1:
        return True

    opened = [False] * len(boxes)
    opened[0] = True

    for i, keys in enumerate(boxes):
        if not opened[i]:
            continue
        for key in keys:
            if key < len(boxes) and not opened[key]:
                opened[key] = True

    return all(opened)
