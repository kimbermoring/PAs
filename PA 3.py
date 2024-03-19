# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:43:40 2024

@author: KLMoring
"""

import numpy as np 

#%% Part I
p1 = np.poly1d([2,3,0,1])
print(p1)
print(f'\nFunction evaluated at x = 2 is {np.polyval([2,3,0,1], 2)}.\n')

p2 = np.poly1d([1,0,1])
print(p2)

p2_der = np.polyder(p2)
print(p2_der)

p2_der_x1 = np.polyder(p2)
print(p2_der_x1(1))

#%% Part II
user_input = input('Please enter a polynomial (i.e. 1, -4, 0, 1): ')
x_1 = float(input('Please enter a value for x1 (i.e. 0.5): '))
 
coeffs = [float(values) for values in user_input.split(',')]
poly = np.poly1d(coeffs)
    
def func_xn(poly, x_n):
    f_xn_eval = np.polyval(poly, x_n)
    return f_xn_eval

def func_prime_xn(poly, x_n): 
    f_prime_xn = np.polyder(poly)
    f_prime_xn_eval = f_prime_xn(x_n)
    return f_prime_xn_eval 

def newtons_method(poly, x_n, x_val = 2): 
    fx_n = func_xn(poly, x_n)
    fx_p_n = func_prime_xn(poly,x_n)
    xn_p = x_n - fx_n/fx_p_n
    
    print(f'x_{x_val} = {x_n:.3f}') 
    
    if abs(xn_p - x_n) < 0.001: #base case
        return print(f'\nThe final value with stabilized thousandths place is: {xn_p:.3f}')
    else: 
        return newtons_method(poly, xn_p, x_val + 1) #recursion
    
print(f'x_1 = {x_1}')

newtons_method(poly, x_1)

roots = np.roots(poly)
print(f'\nThe final roots of this polynomial are: {roots}') 
