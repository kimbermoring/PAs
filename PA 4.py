# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:06:45 2024

@author: KLMoring
"""
user_input = input('Please enter a list of numbers 0-10 separated by commas without any spaces between: ')

values = [values for values in user_input.split(',')] 

numbers_dict = {'zero': 0,
           'one': 1,
           'two': 2,
           'three': 3, 
           'four': 4, 
           'five': 5, 
           'six': 6, 
           'seven': 7, 
           'eight': 8, 
           'nine': 9, 
           'ten': 10}

my_list = []
for num in values: 
    num = num.lower()
    if num.isdigit(): 
        num = int(num)
        if 0 <= num <= 10: 
            my_list.append(num)
    elif num in numbers_dict:
        my_list.append(numbers_dict[num])

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

sorted_list = bubbleSort(my_list)

min_val = sorted_list[0]
max_val = sorted_list[-1]

print(f'The sorted list is: {sorted_list}\nThe maximum value is: {max_val}\nThe minimum value is: {min_val}')

