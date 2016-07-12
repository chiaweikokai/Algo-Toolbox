# Uses python3
import sys


def get_change(m):
    """
    To find the minimum number of coins needed to change the input value
    (an integer) inti coins with denominations 1, 5, and 10
    :param m: input value
    :return: number of coins
    """
    count = 0
    while m > 0:
        if m >= 10:
            m -= 10
            count += 1
        elif m >= 5:
            m -= 5
            count += 1
        else:
            m -= 1
            count += 1

    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
