#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:15:57 2020

@author: ngmingpok
"""
#Find the sum of all the multiples of 3 or 5 below 1000.
def f():
    x = 0
    for i in range (1000):
        if i%3 == 0:
            x += i
        elif i%5 == 0:
            x += i
    return x
        
def g():
    return sum(i for i in range(1000) if i%3 == 0 or i%5 == 0)

def h(): #0 and 1 gives 0, 0 and 0 gives 0
    return sum(i for i in range(1000) if not (i%3 and i%5))
            
print(f())
print(g())
print(h())

