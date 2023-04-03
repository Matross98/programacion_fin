# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:35:51 2023

@author: dell inspirion
"""
def ENTERO_A_BINARIO (codigo,numero):
    
    
    if numero % 2 == 0:
        codigo.append('0')
    else:
        codigo.append('1')
    
    if numero - 1 != 0:        
        
        ENTERO_A_BINARIO (codigo,int(numero/2))
    
    else:
        print(codigo)
    
POSICION=0    
NUMERO=int(input('introduzca un número entero '))    
CODIGO=[]        
ENTERO_A_BINARIO (CODIGO,NUMERO)