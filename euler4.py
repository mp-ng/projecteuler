#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:00:34 2020

@author: ngmingpok
"""
#Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome():
    num = []
    for i in range(100,999):
        for j in range(100,999):
            x = i*j
            x = str(x)
            if len(x) == 5:
                if x[0] == x[4] and x[1] == x[3]:
                    num.append(int(x))
            elif len(x) == 6:
                if x[0] == x[5] and x[1] == x[4] and x[2] == x[3]:
                    num.append(int(x))
    return max(num)
    
print(palindrome())

