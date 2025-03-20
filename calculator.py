import functools
import operator

def summ(*args):
    return functools.reduce(operator.add, args)

def mull(*args):
    return functools.reduce(operator.mul, args)

def fac(x: int):
    return functools.reduce(operator.mul, [i for i in range(1, x+1)])
