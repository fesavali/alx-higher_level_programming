#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Match bytecode"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)

print(magic_calculation(5,4,6))    