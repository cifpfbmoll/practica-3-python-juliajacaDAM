'''
Práctica 3. Ejercicio 6
Pida al usuario el precio de un producto y el nombre del producto y muestre el 
mensaje con el precio del IVA (21%). Por ejemplo: “Tu bicicleta vale 100 euros
 y con el 21 % de IVA se queda en 121 euros en total”.
'''

print('''
Calcula el precio de tu producto favorito con el iva
''')
IVA = 21

producto = input('Introduce el nombre del producto ')
precio_base = float(input('Introduce el precio sin iva '))

precio_iva = precio_base + precio_base * IVA / 100

print(f'''Tu {producto} vale {precio_base} euros y con el {IVA}% de IVA 
se queda en {precio_iva} euros en total ''')

