# ----------------------------------------------
# TUPLAS: Coleccion de elementos inmutables y ordenados
# ----------------------------------------------

'''IMPORTANTE: Para que sea una tupla, siempre debo tener un elemento con una coma. Es decir, si solo tengo un elemento sin ninguna coma, python lee que el tipo de dato es un string, no una tupla'''

# frutas = ("Mango", "Banano", "Cereza")
# print(frutas)

# numeros = (1,2,3)
# booleanos = (True, True, False)
# mixto = (1,2,True, "Mango")

# # Usando el constructor
# animales = tuple( ("Perro", "Gato") )
# print(animales)

# ----------------------------------------------
# ITEMS DE LAS TUPLAS
# ----------------------------------------------

# Se accede igual que con las listas
# frutas = ("Mango", "Banano", "Cereza", "Mandarina", "Aguacate", "Kiwi")
# print(frutas[0:3])

# if "Mandarina" in frutas:
#     print("Hay mandarinas entre mis frutas")

# ----------------------------------------------
# Actualizacion de una tupla
# ----------------------------------------------

# frutas = ("Mango", "Banano", "Cereza", "Mandarina", "Aguacate", "Kiwi")

'''Sabemos que una tupla es inmutable, por lo que no podremos cambiar un item como lo haciamos con las listas, por ejemplo:'''

# frutas[1] = "Anana"
# TypeError: 'tuple' object does not support item assignment

'''Pero podemos hacer otra vuelta para poder asignar un nuevo elemento:'''

# frutas2 = list(frutas) # Convierto la tupla en lista asignandola a otra variable

# frutas2[1] = "Coco" # Modifico la lista

# frutas = tuple(frutas2) # reconvierto la lista a tupla y la reasigno a la variable original

# print(frutas)

'''De la misma manera va a funcionar si quiero agregar un item a la tupla'''

# tupla_frutas = ("Mango", "Banano", "Cereza", "Mandarina", "Aguacate", "Kiwi")
# lista_frutas = list(tupla_frutas)
# lista_frutas.append("Coco")
# tupla_frutas = tuple(lista_frutas)
# print(tupla_frutas)

'''Podremos agregar una tupla a una tupla?'''

# tupla_verdura = ("Ajo", "Papa", "Tomate")
# tupla_frutas += tupla_verdura # OJO QUE ES +=, NO COMO LA LISTA QUE SOLO ES +
# print(tupla_frutas)

'''Para eliminar un elemento se usan los mismos pasos que para hacer el append, pero usando el metodo REMOVE()'''

'''Para eliminar una tupla'''

# del(tupla_verdura)
# print(tupla_verdura)

# NameError: name 'tupla_verdura' is not defined
# Esto porque se elimina del espacio de memoria

# ----------------------------------------------
# DESEMPAQUETADO DE TUPLAS
# ----------------------------------------------

# frutas = ("Mango", "Banano", "Cereza", "Mandarina", "Aguacate", "Kiwi")

# # Asignar estos elementos a variables
# '''El número de variables a la izquierda del = debe coincidir con el número de elementos en la secuencia. Si no coinciden, Python lanzará un error. Los datos se asignan en el mismo orden de la secuencia'''

# (a, b, c, d, e, f) = frutas
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# '''Si solo te interesan algunos elementos, puedes usar * para capturar el resto en una lista.'''

# (a, b, c, *resto) = frutas
# print(a)
# print(b)
# print(c)
# print(resto)

# ''' Si requiero solo la primera y la ultima, pongo el * en el centro o donde lo necesite'''

# (a, *b, c) = frutas
# print(a)
# print(b)
# print(c)

# ----------------------------------------------
# Bucles en tuplas
# ----------------------------------------------

# frutas = ("Mango", "Banano", "Cereza", "Mandarina", "Aguacate", "Kiwi")

# for fruta in frutas:
#     print(fruta)

# # Para imprimir con el indice
# for i in range(len(frutas)):
#     print("Indice:", i, frutas[i])

# # While
# i = 0

# while i < len(frutas):
#     print(frutas[i])
#     i += 1

# ----------------------------------------------
# JUNTAR, CONTAR Y VER INDICES
# ----------------------------------------------

frutas1 = ("Mandarina", "Aguacate", "Kiwi")
frutas2 = ("Mango", "Banano", "Cereza",)

frutas = frutas1 + frutas2
print(frutas)

# Asi duplica la info
frutas = frutas1 * 2 + frutas2
print(frutas)
print(frutas.count("Kiwi"))

# A que indice pertenece...
print(frutas1.index("Mandarina"))