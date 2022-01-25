# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:31:46 2022

@author: 10419
"""

math = input("輸入成績 math:")
eng = input("輸入成績 eng:")
 
math = int(math)
eng = int(eng)

if math >= 90 and eng >= 90:
    print('有獎')

elif math < 60 and eng < 60:
    print('挨罰')