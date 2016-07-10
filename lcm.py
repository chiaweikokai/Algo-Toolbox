# Uses python3
import sys


def gcd(a, b):
    if b == 0:
        return a
    a %= b
    return gcd(b, a)


def lcm(a, b):
    # write your code here
    k = gcd(a, b)
    return a * b // k

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd(a, b))
    print(lcm(a, b))

