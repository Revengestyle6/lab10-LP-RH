# GitHub Link: https://github.com/Revengestyle6/lab10-LP-RH.git
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b): # Performing b / a
    if a == 0:
        raise ZeroDivisionError

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        result = math.log(b, a)

def exp(a, b):
    return a ** b






import math

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b

def logarithm(a, b):# use math library/raise ValueError
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(b,a)
def exponent(a, b):
    return a ** b



