#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:49:00 2023

@author: mac15
"""

class myarray():
    '''Esta clase sirve para operar matrices'''
    
    def __init__(self,lista,r,c,by_row):
        self.lista = lista
        self.r = r
        self.c = c
        self.by_row = by_row
    
    def get_pos(self,j,k):
        '''
        Esta funcion recibe una coordenada de la matriz y devuelve 
        la posicion equivalente en la lista
        
        j = fila solicitada
        k = columna solicitada
        m = posicion en la lista solicitada
        
        '''
        if j>self.r or k>self.c or k < 0 or j < 0:
            m ='No hay tal posicion en la matriz'
            
        else:
            if self.by_row == True:
                ''' multiplico la fila solicitada por la de columnas lo cual me deja
                en la ultima posicion de dicha fila y luego resto la diferencia entre 
                la columna solicitada y la de la totalidad de columnas para terminar
                en la columna correcta'''
                
                m = j * self.c - 1 + k - self.c                
            else:                 
                m = k * self.r - 1 + j - self.r
            
        return m
    
    def get_coords(self,m):
        '''
        esta funcion recibe m y devuelve las coordenadas correspondientes 
        en la matriz
            
        m = posicion en la lista

        '''
            
        if self.by_row == True:
            ''' si divido como entero a m por la cantidad de columnas me va a dar
            la fila a la que corresponde y, como ya sabemos el valor de j, k
            la calculamos despejando la formula con la que sacamos m'''
            
            j = m // self.c + 1
            k = m - j * self.c + 1 + self.c
            salida = (j,k) 
            
        return salida
    
    def switch(self):
        ''' esta funcion cambia el orden de la lista, si es por fila o columna
        
        s_matriz = matriz cambiada
        i = es un contador'''
        
        i=0
        s_matriz=[]
        if self.by_row == True:
            self.by_row = False
            while i < self.c :
                s_matriz = s_matriz + (self.lista[i::self.c])
                i = i + 1
                           
        else:
            self.by_row = True
            while i < self.r:
                s_matriz = s_matriz + (self.lista[i::self.r])
                i = i +1
                
        self.lista = s_matriz
        
        return s_matriz

    def get_row(self,j):
        ''' Esta funcion devuelve la fila entera solicitada 
        j= numero de fila solicitada
        row= fila solicitada
        '''
        
        if j > self.r:
            row = f'La fila {j} no existe'
        else:    
            if self.by_row == True:
                row = self.lista[(j-1)*self.c:(j-1)*self.c+self.c]
            else:
                row= self.lista[j-1::self.r]
        
        return row
    
    def get_col (self,k):
        '''
        Esta funcion recibe un numero de columna y devuelve la 
        columna entera en formato de lista
        
        k= numero de columna solicitada
        col= columna solicitada


        '''
        
        if k > self.c or k < 0:
            col = f'La columna {k} no existe'
        else:    
            if self.by_row== True:
                col = self.lista[(k-1)::self.c]
            else:
                col= self.lista[(k-1)*self.r:(k-1)*self.r+self.r]
        
        return col
    
    def get_elem(self,j,k):
        ''' Esta funcion toma una posicion en la matriz y devuelve
        el elemento correspondiente
        
        j= numero de fila
        k= numero de columna
        elem= elemento solicitado
        
        '''
        
        elem = self.lista[self.get_pos(j,k)]
        
        return elem
    
    def del_row (self,j):
        
        lista_el = self.lista
        
        del lista_el[(j-1)*self.c:self.c*j]
        
        return lista_el
    
    def del_col (self,k):
        '''Esta funcion toma una columna y la elimina de la matriz
        
        lista_el= nueva matriz con la columna eliminada
        k= numero de columna a eliminar
        
        '''
        lista_el = self.lista
        
        if len(lista_el)  > self.r*self.c - self.r:
            del lista_el [k-1]
            print(lista_el)
            k= k + self.c -1
            self.del_col(k)
        
        else:
            return lista_el
        '''no se porque devuelve none'''
        
    def swap_rows(self,j,k):
        ''' esta funcion intercambia la fila k con la fila j'''
        if j > k or k == j or j> self.r or k>self.r:
            print('error uno o mas de los valores es invalido')
        
        elif self.by_row is False:
            change_row = self.swap_cols(j,k)
        
        else:
            change_row= self.lista
            row_j = self.get_row(j)
            row_k = self.get_row(k)
            
            del change_row[(j-1)*self.c:(j-1)*self.c+self.c]
            del change_row[(k-2)*self.c:(k-2)*self.c+self.c]

            for i in range(0,self.c):
                change_row.insert((j-1)*self.c+i,(row_k[i]))
                change_row.insert((k-1)*self.c+i,(row_j[i]))
                
        return change_row
    
    def swap_cols(self,l,m):
        ''' esta funcion recibe dos numeros de columnas y las
        intercambia de lugar
        
        l= primer numero de columna a cambiar
        m= segundo numero de columna a cambiar
        change_col= matriz con la columna cambiada
        col_l = la columna l
        col_m = la columna m
        '''
        if l == m or l > self.c or m>self.c:
            print('error uno o mas de los valores es invalido')
            
        elif self.by_row == False:
            change_col=self.swap_rows(l,m)
            
        else:    
            change_col=self.lista
            col_l= self.get_col(l)
            col_m= self.get_col(m)
            
            for i in range(0,self.r):
                change_col[self.get_pos(i+1,l)] = col_m[i]                
                change_col[self.get_pos(i+1,m)] = col_l[i]                
            
        return change_col
        
#    scale_row(self,j,x), scale_col(self,k,y)
    def scale_row(self,j,x):
        ''' multiplica una fila j por un valor x
        mx_multiplied = matriz con la fila j multiplicada
        j= numero de fila'''
        if j > self.c or j<0:
            print(f'la fila {j} no existe en la matriz')
        
        else:            
            mx_multiplied = self.lista
            
            for i in range(0,self.c):
                mx_multiplied[self.get_pos(j,i+1)]= mx_multiplied[self.get_pos(j,i+1)] * x
                
            return mx_multiplied
    
    def scale_col(self,k,y):
        ''' multiplica una columna k por un valor y 
        k= numero de columna
        y= multiplicador
        mx_multiplied= lista con la columna multiplicada
        
        '''
        if k > self.c or k < 0:
          print('k no es un numero de columna valido para esta matriz')  
        
        else:
            
            mx_multiplied = self.lista
            
            for i in range(0,self.r):
                
                mx_multiplied[self.get_pos(i+1,k)]= mx_multiplied[self.get_pos(i+1,k)] * y
            
            return mx_multiplied
    
    def transpose(self):
        
        a=self.switch()
        
        return a
        
#    def det (self):
#        if self.r != self.c:
 #           print('La matriz no es cuadrada')
 #       else:
 #           determinante = 
    def add(self,b):
        '''
        suma un valor b a la matriz
        
        mx_add = matriz sumada
        b = valor a sumar'''
        
        mx_add = self.lista
        
        if type(b) == int:            
            posicion = 0            
            for elemento in mx_add:
                mx_add[posicion] = elemento + b
                posicion += 1
                print(mx_add)
        elif type(b) == list and len(b) == len(mx_add):
            
            for posicion in range(0,len(b)):
                mx_add[posicion] = mx_add[posicion]+b[posicion]
        
        else:
            mx_add='El valor ingresado es invalido, tiene que ser list o int'
            
        return mx_add
    
    def sub (self,b):
        '''resta la matriz por un valor b
        
        mx_sub= la matriz restada
        b= valor a restar
        
        '''
        if type(b) == int:
            mx_sub = self.add(-b)
        elif type(b) == list:
            posicion = 0        
            for elemento in b:
                b[posicion]= - elemento
                posicion = posicion + 1

            mx_sub = self.add(b)
        else:
            mx_sub = 'El valor b no es valido'
        
        return mx_sub
    
    def rprod(self,b):
        
        mx_multiplied = []
        
        if type(b) == int:
            
            for posicion in range(0,len(self.lista)):
                mx_multiplied = mx_multiplied[posicion] * b
        
        elif type(b) == list:
            
            for position in range(0,self.r):                
                row = self.get_row(position)
                col_b = b[(position)::2] 
                'asumo una matriz de 3x2'                
                for pos_element in range(0,self.c):
                    mx_multiplied += row[pos_element] * col_b[pos_element] 
        else:
            mx_multiplied = 'El elemento ingresado no es valido'
        
        return mx_multiplied     
            
            
elems=[1,2,3,4,5,6]
BY_ROW = True
R=2
C=3
x=myarray(elems,R,C,BY_ROW)
#print(x.get_pos(2,1))
#print(x.get_coords(5))
#print(x.switch())
#print(x.get_row(3))
#print(x.get_col(2))
#print(x.get_elem(3,3))
#print(x.del_row(3))
#print(x.del_col(3))   
#print(x.swap_rows(1,4))
#print(x.swap_cols(1,3))
#print(x.scale_row(1,2))
#print(x.scale_col(2,2))
#print(x.transpose())
#print(x.add([1,2,3,4,5,6]))
#print(x.sub([1,2,3,4,5,6]))
print(x.rprod([1,2,3,4,5,6]))
   