# Uses python3
import sys


def get_fibonacci_last_digit(n):
    # write your code here
    pre1 = 1
    pre2 = 1
    if n == 0: return 0
    if n == 1: return pre1
    if n == 2: return pre2
    # res = 0
    for i in range(3, n + 1):
        res = (pre1 + pre2) % 10
        pre2 = pre1 % 10
        pre1 = res

    return res

# n = int(input())
# print(get_fibonacci_last_digit(n))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
