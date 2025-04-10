"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):  # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a
def logarithm(a, b):# use math library/raise ValueError
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(b,a)
def exponent(a, b):
    return a ** b


