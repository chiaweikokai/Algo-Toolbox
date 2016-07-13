# Uses python3
import sys


def min_dot_product(a, b):
    """
    Minimum product value of two array a, b
    :param a: list of n number of integers
    :param b: list of n number of integers
    :return: minimum product value of a, b
    """
    res = 0
    a.sort(reverse=True)
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))

