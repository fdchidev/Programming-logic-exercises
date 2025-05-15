# EJERCICIO 1

'''URL del sitio web oficial del
lenguaje de programación que has seleccionado: https: // www.python.org/.'''

# https: // www.python.org/

# EJERCICIO 2
'''Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje(en una línea, varias.
'''
# Comentario de una sola línea, se usa almohadilla.

'''
Este es un comentario
de varias líneas 
en lenguaje de programaciíon
Python
'''

"""
También se puede escribir comentarios con comillas dobles
"""


# EJERCICIO 3

'''
Crea una variable(y una constante si el lenguaje lo soporta).
    
En python para declarar variables simplemente se le da un nombre (al contrario de JS con la palabra reservada "var").
(checar la sintaxis, snake_ case etc)

ej: my_variable:
'''
my_variable = 'Mi variable'
my_variable = 'Nuevo valor de mi variable'

'''
ej: constantes:
En python no hay constantes ('const' en JS), todos son variables. 
Para representar una constante, convención: 

MY_CONSTANT = 'Mi constante'
ej:
'''
MY_CONSTANT = 'Mi constante'  # Por convención


# EJERCICIO 4

'''Crea variables representando todos los tipos de datos primitivos
del lenguaje(cadenas de texto, enteros, booleanos...).

En python los datos primitivos son 4: 

Entero           > Integer  > int
Decimal          > float     > float
Booleano         > Boolean  > bool
Cadena de Texto  > string   > str
'''

my_int = 1
my_float = 3.1416
my_bool = True
my_string = 'Cadena de texto'


# EJERCICIO 5
'''
Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
'''

print('Hola python')

# Tipo de datos con 'type'

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
