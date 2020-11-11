'''
Práctica 3. Ejercicio 4
Pide al usuario que introduzca 3 calificaciones, y calcule la media de estas.
'''
print('''
¡Calculadora de medias! (Sólo funciona con tres notas por el momento)
''')

nota_1 = float(input('Introduce la primera nota '))
nota_2 = float(input('Introduce la segunda nota '))
nota_3 = float(input('Introduce la tercera nota '))

promedio = (nota_1 + nota_2 + nota_3) / 3

print(f'El promedio de las notas {nota_1}, {nota_2} y {nota_3} es {promedio}')