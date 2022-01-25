# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:49:49 2022

@author: 10419
"""

grade = input('輸入成績:')

grade = int(grade)

if grade >= 90:
    print('A')

elif grade >= 80:
    print('B')
    
elif grade >= 70:
    print('C')
    
else:
    print('D')