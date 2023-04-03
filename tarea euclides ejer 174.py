# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:48:34 2023

@author: dell inspirion
"""
def euclides(a,b):
    if b == 0:
        return a
    else:
        d = a%b
        c = a//b
        print(d,c,a,b)
        if d == 0:
            x=b            
            return x
        
        elif d != 0:
            x=euclides(b,d)
            return x
a= int(input("numero 1: "))
b= int(input("numero 2: "))

print("El MCD es", euclides(a,b))