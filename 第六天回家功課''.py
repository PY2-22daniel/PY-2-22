# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:23:05 2022

@author: 10419
"""

scores = [['Chris', 83],
          ['David', 96],
          ['Bill', 92],
          ['Amy', 59],
          ['James', 77],
          ['happy',88],
          ['daniel',46],
          ['oliver',64],
          ['sunstein',76],
          ['apple',84]]

student_name = [scores[i][0] for i in range(0,len(scores))]
print(student_name)

student_score = [scores[i][1] for i in range(0,len(scores))]
print(student_score)

max_index = student_score.index(max(student_score))
print(f'highest: {student_name[max_index]}, {max(student_score)}')

min_index = student_score.index(min(student_score))
print(f'lowest: {student_name[min_index]}, {min(student_score)}')

total = 0
for i in range(0,len(student_score)):
    total = (total + student_score[i])
print(f'avg: {total/len(student_score)}')

