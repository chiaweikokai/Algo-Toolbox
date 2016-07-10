# Uses python3
import sys


def get_fibonaccihuge(n, m):

    pre1 = 1
    pre2 = 1
    if n == 0: return 0
    if n == 1: return pre1 % m
    if n == 2: return pre2 % m
    res = 0
    for i in range(3, n + 1):
        res = (pre1 + pre2) % m
        pre2 = pre1 % m
        pre1 = res

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
