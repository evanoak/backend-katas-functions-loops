#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Evan Ochs"


def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    # your code here
    count = 0
    if x > 0 and y > 0:
        for num in range(y):
            count = add(count, x)
        return count
    elif x < 0 and y > 0:
        for num in range(y):
            count = add(count, x)
        return count
    elif x > 0 and y < 0:
        for num in range(x):
            count = add(count, y)
        return count
    elif x < 0 and y < 0:
        for num in range(-y):
            count = add(count, -x)
        return count
    elif x == 0 or y == 0:
        return 0


def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    count = n
    answer = 1
    if n > 0 and x > 0:
        while count:
            answer = multiply(x, answer)
            count = count - 1
        return answer
    elif x < 0 and n > 0:
        while count:
            answer = multiply(x, answer)
            count = count - 1
        return answer
    elif x == 0:
        return 0
    elif n == 0:
        return 1


def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    count = x
    answer = 1
    while count:
        answer = multiply(answer, count)
        count = count - 1
    return answer


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    num1 = 0
    num2 = 1
    result = 0

    if n == 1:
        return 1
    else:
        for num in range(1, n):
            result = add(num1, num2)
            num1 = num2
            num2 = result
        return result


if __name__ == '__main__':
    # your code to call functions above
    print(add(2, 4))
    print(multiply(-6, -8))
    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8)) 
