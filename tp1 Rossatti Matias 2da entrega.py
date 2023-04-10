#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:49:00 2023

@author: mac15
"""

class myarray():
    '''Esta clase sirve para operar matrices
    
    sus funciones son:
        
    get_pos = Recibe una coordenada de la matriz y devuelve 
    la posicion equivalente en la lista
    
    get_coords = Recibe m y devuelve las coordenadas correspondientes 
    en la matriz    
        
    switch = esta funcion cambia el orden de la lista, si es por fila o columna

    get_row = recibe un numero de fila y la devuelve en forma de lista 
    
    get_col = recibe un numero de columna y la devuelve en forma de lista
    
    get_elem = toma una posicion en la matriz y devuelve
    el elemento correspondiente
    
    swap_rows = recibe dos numeros de filas y las
    intercambia de lugar
    
    swap_cols = recibe dos numeros de columnas y las
    intercambia de lugar    
        
    del_row(self,j) = elimina una fila
    
    del_col(self,k) = toma una columna y la elimina de la matriz
        
    scale_row = multiplica una fila j por un valor x
        
    scale_col = multiplica una columna k por un valor y 
        
    transpose = crea la matriz transpuesta usando la funcion switch para intercambiar filas por columnas
        
    det = calcula el determinante de la matriz con la formula de cofactores
        
    add = suma un valor b a la matriz
        
    sub = resta la matriz por un valor b
        
    rprod = multiplica por derecha a la matriz por matrices o escalares
    
    eye = arma una matriz identidad con el tamaño de la
        matriz original
    
        '''
    
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
    
    def get_col(self,k):
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
    
    def del_row(self,j):
        ''' elimina una fila
             
        j = numero de fila a eliminar
        lista_el = nueva matriz con la fila eliminada
        '''
        
        lista_el = self.lista
        
        del lista_el[(j-1)*self.c:self.c*j]
        
        return lista_el
    
    def del_col(self,k):
        '''Esta funcion toma una columna y la elimina de la matriz
        
        lista_el= nueva matriz con la columna eliminada
        k= numero de columna a eliminar
        
        '''
        
        
        if len(self.lista)  > self.r*self.c - self.r:
            del self.lista [k-1]
            
            k= k + self.c -1            
            self.del_col(k)
        else:

            return self.lista
        '''no se porque devuelve none'''
        
    def swap_rows(self,j,k):
        ''' esta funcion intercambia la fila k con la fila j'''
        if j > k or k == j or j> self.r or k>self.r:
            print('error uno o mas de los valores es invalido')
        
        elif self.by_row is False:
            change_row = self.swap_cols(j,k)
        
        else:
            change_row = self.lista
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
        
    def scale_row(self,j,x):
        ''' multiplica una fila j por un valor x
        mx_mult = matriz con la fila j multiplicada
        j= numero de fila'''
        if j > self.c or j<0:
            print(f'la fila {j} no existe en la matriz')
        
        else:            
            mx_mult = self.lista
            
            for i in range(0,self.c):
                mx_mult[self.get_pos(j,i+1)]= mx_mult[self.get_pos(j,i+1)] * x
                
            return mx_mult
    
    def scale_col(self,k,y):
        ''' multiplica una columna k por un valor y 
        k= numero de columna
        y= multiplicador
        mx_mult= lista con la columna multiplicada
        
        '''
        if k > self.c or k < 0:
          print('k no es un numero de columna valido para esta matriz')  
        
        else:
            
            mx_mult = self.lista
            
            for i in range(0,self.r):
                
                mx_mult[self.get_pos(i+1,k)]= mx_mult[self.get_pos(i+1,k)] * y
            
            return mx_mult
    
    def transpose(self):
        '''hace la matriz transpuesta usando la funcion switch para intercambiar filas por columnas
        a= la matriz transpuesta'''
        
        a=self.switch()
        
        return a
        
    def det(self): 
        
        '''calcula el determinante de la matriz con la formula de cofactores'''
        mx = self.lista
        det = 0
        size = self.r
        def sub_mx(mx,det,size):
            
            if len(mx)== 1:            
                det = mx    
            
            elif len(mx) == 2:
                det = mx[0] * mx[3] - mx[1] * mx[2]
                
            else:
                
                submatrix = []
                for i in range(size):
                    ''' i va desde 0 hasta la cantidad de filas de mx - 1,
                    es un contador de filas'''
                    submatrix = [mx[indice] for indice in range(len(mx)) if indice != (i) and indice//size != 0]
                    '''indice va tomando la posicion en la lista de todos los
                    elementos de la matriz
                    si indice no es el primer elemento de la lista
                    y indice dividido de forma entera con el numero de fila
                    es distinto a 0'''
                    
                    signo = (-1)**i
                    size -= 1
                    print(det)
                    print (submatrix)
                    det += signo * mx[i] * sub_mx(submatrix,det,size)
            return det
            
        if self.r != self.c:
            det='La matriz no es cuadrada'
        
        else:
            det = sub_mx(mx,det,size)
            
        return det

            
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
    
    def sub(self,b):
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
        '''
        multiplica por derecha a la matriz original
        
        mx_mult = la matriz resultante de la multiplicacion
        
        num_row = numero de filas de la matriz b
        num_col = numero de columnas de la matriz b
        mx_mult2 = matriz b
        
        l,i = numero de columna de b, numero de fila de elems
        r = numero de elemento en la matriz resultante
        
        row = fila de elems
        col_b = columna de b
        
         
        '''
        
        mx_mult = self.lista
        
        if type(b) == int:
            
            for position in range(0,len(mx_mult)):
                mx_mult [position] = mx_mult[position] * b
                
        elif type(b) == list:
            
            num_row,num_col = self.c,int(len(b)/self.c)
            '''consigo el numero de columnas y filas de la matriz multiplicadora'''
            mx_mult = [0] * (num_col*self.r)
            '''matriz de ceros'''
            mx_mult2 = myarray(b,num_row,num_col,True) 
            ''' convierto la lista b en un elemento tipo myarray'''
            
            l = 1
            i = 1
            r = 0
            while r != num_col*self.r:                
                
                if l > num_col:
                    l -= (num_col)
                    i += 1
                
                row = self.get_row(i)
                col_b = mx_mult2.get_col(l)
                
                for pos_element in range(0,self.c):
                    mx_mult[r] += row[pos_element] * col_b[pos_element]                        
                r+= 1
                l+= 1 
                
        else:
            mx_mult = 'El elemento ingresado no es valido'
        
        return mx_mult
    
    def lprod (self,b):
        '''
        multiplica a la matriz original por izquierda

        Parameters
        ----------
        b : matriz multiplicadora

        Returns
        -------
        mx_mult : matriz multiplicada

        '''
        mx_mult = self.lista
        
        if type(b) == int:
            
            for position in range(0,len(mx_mult)):
                mx_mult [position] = mx_mult[position] * b
                
        elif type(b) == list:
            
            num_row,num_col = self.c,int(len(b)/self.c)
            '''consigo el numero de columnas y filas de la matriz multiplicadora'''
            mx_mult = [0] * (num_col*self.r)
            '''matriz de ceros'''
            mx_mult2 = myarray(b,num_row,num_col,True) 
            ''' convierto la lista b en un elemento tipo myarray'''
            
            l = 1
            i = 1
            r = 0
            while r != num_row*self.c:                
                
                if l > self.c:
                    l -= (self.c)
                    i += 1
                
                row_b = mx_mult2.get_row(i)
                col = self.get_col(l)                
                
                for pos_element in range(0,num_col):
                    mx_mult[r] += row_b[pos_element] * col[pos_element] 
                    
                    
                r+= 1
                l+= 1 
        else:
            mx_mult = 'El elemento ingresado no es valido'
        
        return mx_mult
    
    def eye(self):
        ''' arma una matriz identidad con el tamaño de la
        matriz original
        
        mx_id = matriz identidad
        i = un contador que se va marcando la posicion donde van los 1
        '''
        
        if self.r != self.c:
            mx_id ='la matriz no es cuadrada'
        else:
            mx_id = [0] * (len(self.lista))
            i=0
            while i < len(self.lista):
                mx_id[i] = 1
                i += self.c+1
        return mx_id
    
    def pow_mx(self,potencia):
        '''esta funcion calcula la potencia de una matriz
        
        potencia = escalar
        mx = matriz
        '''
        mx = self.lista
        
        for i in range(potencia):
            mx = self.rprod(self.lista)

            
        return mx
    
    def swap_rows_id(self,j,k):
        ''' intercambia la fila j con la fila k usando el metodo
        de la matriz identidad
        
        eye = matriz identidad
        row1 = fila j
        row2 = fila k
        '''
                
        eye = myarray(self.eye(),self.r,self.c,self.by_row)
               
        row1 = eye.get_row(j)                
        row2 = eye.get_row(k)
        eye = self.eye() 
        for i in range(self.r):
            eye [i + j*self.c - self.c] = row2[i]
            eye [i + k*self.c - self.c] = row1[i]            
        
        return (self.lprod(eye))
    
    def swap_cols_id (self,l,m):
         
        eye = myarray(self.eye(),self.r,self.c,self.by_row)
               
        row1 = eye.get_row(l)                
        row2 = eye.get_row(m)
        eye = self.eye() 
        for i in range(self.r):
            eye [i + l*self.c - self.c] = row2[i]
            eye [i + m*self.c - self.c] = row1[i]            
        
        return (self.rprod(eye))
            
    def del_row_id(self,row):
        
        eye = self.eye()
        
        for i in range(self.r):
            eye[i + row*self.c - self.c] = 0
            
        return self.lprod(eye)    
        
    def del_col_id(self,col):
        
        eye = self.eye()
        
        for i in range(self.r):
            eye[i + col*self.c - self.c] = 0
            
        return self.rprod(eye)
    
elems=[1,2,3,4,5,6,7,8,9]
BY_ROW = True
R=3
C=3
x=myarray(elems,R,C,BY_ROW)
print(x.get_pos(2,1))
print(x.get_coords(5))
print(x.switch())
print(x.get_row(3))
print(x.get_col(2))
print(x.get_elem(3,3))
print(x.del_row(3))
#print(x.del_col(1)) devuelve none 
print(x.swap_rows(1,4))
print(x.swap_cols(1,3))
print(x.scale_row(1,2))
print(x.scale_col(2,2))
print(x.transpose())
print(x.add([1,2,3,4,5,6]))
print(x.sub([1,2,3,4,5,6]))
print(x.rprod([1,2,3,4,5,6,7,8,9]))
print(x.rprod([1,2,3,4,5,6,7,8,9]))
#print(x.det()) no esta terminado
print(x.eye())
print(x.pow_mx(2))
print(x.swap_rows_id(1,2))
print(x.swap_cols_id(1,3))
print(x.del_row_id(2))
print(x.del_col_id(3))