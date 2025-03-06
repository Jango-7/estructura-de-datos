
# cursos = ["IA", "Big Data", "SQL", "Python", "SEO"]
# for curso in cursos:
#   print(curso)

#--------------------------------------------------
#--------------------------------------------------

# numeros = []

# for n in range(0,20):
#   numeros.append(n)
#   print(numeros)

# ----------------------------------------------
# ----------------------------------------------

'''
Ejercicio: Contar vocales en una cadena

Escribe un programa que cuente cuántas vocales (a, e, i, o, u) hay en una cadena de texto ingresada por el usuario. Usa un bucle for para recorrer la cadena y verificar cada carácter.

Requisitos:
- Pide al usuario que ingrese una cadena de texto.
- Usa un bucle for para recorrer cada carácter de la cadena.
- Verifica si el carácter es una vocal (minúscula o mayúscula).
- Mantén un contador para cada vocal.
- Al final, imprime el total de vocales encontradas.
'''

# texto = input('Ingresa una frase: ').lower()
# contador = 0
# vocals = ["a", "e", "i", "o", "u"]

# for letra in texto:
#   if letra in vocals:
#     contador += 1

# print(f'Cantidad de vocales: {contador}')

# ----------------------------------------------
# ----------------------------------------------

'''
Escribe un programa que solicite al usuario un número entero positivo n. Luego, el programa debe imprimir todos los números pares desde 0 hasta n (inclusive), pero solo si el número es divisible por 4.
'''

# numeros = int(input("Ingresa un numero entero positivo: "))

# for numero in range(numeros + 1):
#     if numero % 4 == 0:
#         print(numero)

# ----------------------------------------------
# ----------------------------------------------

'''Escribe un programa que solicite al usuario una palabra (cadena de texto). Luego, el programa debe imprimir cada letra de la palabra junto con su posición (índice) en la palabra.

PISTAS:
* Puedes usar la función range() junto con len() para obtener los índices de la palabra.
* Recuerda que las cadenas de texto en Python son iterables, por lo que puedes acceder a cada letra usando su índice.'''

# palabra = input('Ingresa una palabra: ')

# for i in range(len(palabra)):
#     print(f'indice: {i}: {palabra[i]}')

'''Escribe un programa que solicite al usuario un número entero positivo n. Luego, el programa debe calcular la suma de todos los números impares desde 1 hasta n (inclusive) y mostrar el resultado.

Por ejemplo, si el usuario ingresa 10, el programa debería calcular la suma de los números impares 1 + 3 + 5 + 7 + 9 y mostrar:

Pistas:
* Usa un ciclo for para iterar sobre los números desde 1 hasta n.
* Usa una variable para acumular la suma de los números impares.
* Recuerda que un número es impar si el residuo de dividirlo entre 2 no es cero (numero % 2 != 0).'''


numero = int(input("Ingresa un numero entero: "))
suma_impar = 0

for n in range(1, numero + 1):
    if n % 2 != 0:
        suma_impar += n

print(suma_impar)