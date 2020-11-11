'''
Práctica 3. Ejercicio 2
Pida al usuario el espacio recorrido por un coche y el tiempo que ha tardado 
en horas y que calcule a qué velocidad media había realizado el recorrido.
'''

print('''
Calculador de velocidades fabuloso
''')

distancia = float(input('Indica los kilómetros recorridos '))
tiempo = float(input('Indica el tiempo en horas '))
velocidad = distancia / tiempo
print(f'Tu velocidad ha sido de {velocidad} km/h')



