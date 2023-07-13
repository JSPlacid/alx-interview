#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy
        paste
'''


def minOperations(n):
    '''
    returns the minimum operations to get n H's
    '''
    min_operations = 0

    if n <= 1:
        return min_operations

    ops = [float('inf')] * (n+1)
    ops[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                ops[i] = min(ops[i], ops[j] + (i // j))

    return ops[n] if ops[n] != float('inf') else 0


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for i in range(10):
        n = randint(2, 100)
        print("Min # of operations to reach {} char: {}".
              format(n, minOperations(n)))

    print(f'==> Program completed in {time() - start_time:.3f}s')
