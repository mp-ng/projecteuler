#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:37:17 2020

@author: ngmingpok
"""
#Find the smallest positive integer that is evenly divisible by 1-20.
def f():
    integer = 2520
    for divisor in range(2, 21): 
        if integer % divisor != 0: #checks if it is divisible by 1-20
            for multiplier in range(2, 21): 
                if (integer*multiplier) % divisor == 0: 
                    integer *= multiplier 
                    break 
    return integer

print(f())