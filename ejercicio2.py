#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos 
#impares de una lista pasada por parámetro con filter y realizará una suma de todos estos 
#elementos obtenidos mediante reduce.

from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def miFuncion(x):
    if x % 2:
        return True
    return False 
def suma(a, b):
    print(f'a={a}, b={b}')
    return a+b
resultado = filter (miFuncion, lista)
mvp = reduce(suma, resultado)
print(mvp)