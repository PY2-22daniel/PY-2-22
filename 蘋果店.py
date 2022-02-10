# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:13:38 2022

@author: 10419
"""
num = 0
sell = 0
sells = []

print('#'*20)
print('Python蘋果店進出系統')
print('#'*20)

while True:
    #功能
    print('\n')
    print('功能=>')
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存顯示')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')
    
    #選項判斷
    if sel == '1': #設定
        num = int(input('輸入蘋果數量：　'))
        price = int(input('輸入蘋果單價：　'))
        print('蘋果目前有',num,'顆')
        print('蘋果一顆',price,'元')
        
    elif sel == '2': #進貨
        numin = int(input('輸入蘋果進貨數量: '))
        num = num + numin
        print('目前有',num,'顆')
        
    elif sel == '3': 
        numout = int(input('輸入出貨數量: '))
        print('應付',numout*price,'元')
        num = num - numout
        sell = sell + numout
        sells.append(numout)
        print('蘋果目前有',num,'顆')
        print('目前每位客人買的數量',sells)
        
    elif sel == '4': #營業額與毛利
        for i in range(len(sells)):
            print(sells[i],'顆',sells[i]*price,'元')
            
    elif sel == '5': #庫存
        print('蘋果目前有',num,'顆')
    elif sel == '6':
        break
    else:
        print('wrong input')