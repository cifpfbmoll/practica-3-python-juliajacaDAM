'''
Práctica 3. Ejercicio 7
Pida al usuario tres número que serán el día, mes y año. 
Comprueba que la fecha introducida es válida.  Por ejemplo: 
32/01/2017->Fecha incorrecta
29/02/2017->Fecha incorrecta
30/09/2017->Fecha correcta.

'''

from datetime import datetime 
fecha = input('Introduce la fecha a comprobar en formato dd/mm/YYYY ')

try:
    datetime.strptime(fecha, '%d/%m/%Y')
    print(f'{fecha}- fecha correcta')
except ValueError:
    print(f'{fecha}- fecha incorrecta')
