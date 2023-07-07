def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked by default
    keys = set(boxes[0])  # Collecting keys from the first box

    # Iterate through the unlocked boxes until no more new keys are found
    while True:
        new_keys = set()
        for box_num in range(1, n):
            if not unlocked[box_num] and box_num in keys:
                unlocked[box_num] = True
                new_keys.update(boxes[box_num])
        keys.update(new_keys)
        if not new_keys:
            break

    return all(unlocked)


