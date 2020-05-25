#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:40:56 2020

@author: ngmingpok
"""
#Find the sum of even-valued Fibonacci terms that do not exceed 4 million.
def fib():
    x = 1
    y = 2
    z = 3
    result = 2
    while z < 4000000:
        z = x+y
        if z%2 == 0:
            result += z
        x = y
        y = z
    return result

print (fib())
        