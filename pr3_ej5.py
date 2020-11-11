'''
Práctica 3. Ejercicio 5
Pida un número que como máximo tenga tres cifras 
(por ejemplo serían válidos 1, 99 y 213 pero no 1001).
 Si el usuario introduce un número de más de tres cifras debe 
 un informar con un mensaje de error como este 
 “ERROR: El número 1005 tiene más de tres cifras”.
'''

print('''
Comprobador de longitud de cifras. ¡No intentes introducir un número con más de tres cifras!
''')

numero = input('Ingresa el número aquí: ') 
# Dejo el numero como cadena porque sólo las cadenas tienen la función len

if len(numero) > 3:
    print(f'ERROR: El número {numero} tiene más de tres cifras')