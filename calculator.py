# GitHub Link: https://github.com/Revengestyle6/lab10-LP-RH.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): 
    return a + b

def mul(a, b):
    return a * b

def div(a, b): # Performing b / a
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a
def exp(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        raise ValueError
    else:
        math.sqrt(a)# raise ValueError if a < 0
def hypotenuse(a, b):
    math.hypot(a, b) # can have negative nums
def subtract(a, b):
    return a - b
def logarithm(a, b):# use math library/raise ValueError
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(b,a)




