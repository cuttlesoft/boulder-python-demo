# -*- coding: utf-8 -*-
"""
    __init__.py
    ~~~~~~~~~~~
    a little module
"""


def fibonacci_generator(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b


def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_bruto():
    x = [1, 1]
    for i in range(10):
        x.append(x[-1] + x[-2])
    print(', '.join(str(y) for y in x))
