# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:59:12 2022

@author: 10419
"""

scores = []

for i in range(3):
    score = int(input('input score:'))
    scores.append(score)

print(scores)

total = 0

highest = 0
lowest = 100

for i in scores:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total = total + i

print('total:',total)
print('highest:',highest)
print('lowest:',lowest)
print('mean:',total / 3)