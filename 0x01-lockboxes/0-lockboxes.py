#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked by default
    keys = boxes[0]  # Collecting keys from the first box

    # Iterate through the unlocked boxes until no more new keys are found
    for i in range(n):
        if unlocked[i]:
            for key in boxes[i]:
                if key < n and not unlocked[key]:
                    unlocked[key] = True
                    keys.extend(boxes[key])

    return all(unlocked)


