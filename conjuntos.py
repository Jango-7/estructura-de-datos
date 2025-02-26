# ----------------------------------------------
# CONJUNTO (SET) [Coleccion no ordenada y mutable de elementos unicos]
# ----------------------------------------------

# El booleano True es igual a 1
# El booleano False es igual a 0

# # Asi creo un set
# frutas = {"Manzana", "Platano", "Pera", "Manzana"}
# print(frutas)

# # Me va a decir que tengo 3 items en la longitud, porque los conjuntos no se repiten.
# longitud = len(frutas)
# print(longitud)

# # Tambien lo podemos hacer con el constructor
# animales = set(("Perro", "Gato", "Cangrejo"))
# print(animales)

# ----------------------------------------------
# Acceder, agregar y eliminar Items en Set
# ----------------------------------------------

# '''No puedo acceder a un conjunto a traves del indice ya que es una coleccion NO ORDENADA'''

# frutas = {"Manzana", "Platano", "Pera"}
# #print(frutas[1])
# # TypeError: 'set' object is not subscriptable

# '''Asi accedemos:'''
# for fruta in frutas:
#     print(fruta)

# '''Tambien puedo preguntar si esta algun item dentro del conjunto'''
# print("Manzana" in frutas)
# # True

# '''Como agregar mas conjuntos al set'''
# frutas.add("Mango")
# print(frutas)
# # {'Manzana', 'Mango', 'Platano', 'Pera'}

# '''Podemos agregar mas sets'''
# frutas_tropicales = {"Piña", "Maracuya", "Guanabana"}

# frutas.update(frutas_tropicales)
# print(frutas)
# # {'Maracuya', 'Guanabana', 'Manzana', 'Mango', 'Pera', 'Piña', 'Platano'}

# ''' Con .update() tambien se puede agregar otro tipo de estructuras'''
# lista_frutas2 = ["Arandano", "Pera"]

# frutas.update(lista_frutas2)
# print(frutas)
# # {'Pera', 'Manzana', 'Platano', 'Piña', 'Guanabana', 'Mango', 'Maracuya', 'Arandano'}

# ''' Como borrar elementos'''
# frutas.remove("Piña")
# print(fruta)

# frutas.discard("Pera")
# print(fruta)

# frutas.pop() # Elimina un elemento aleatorio
# print(fruta)

# frutas.clear()
# print(fruta) # Devuelve el set vacio

# del frutas
# # Para borrar de la memoria


# ----------------------------------------------
# Juntar conjuntos y bucles en conjuntos
# ----------------------------------------------


letras = {"a", "b", "c"}
numeros = {1,2,3}

# Union para unir sets
union = letras.union(numeros)
print(union)

# En Python 3.9+, el pipe (|) se puede usar para unir conjuntos.
union = letras | numeros
print(union)
# {'c', 1, 2, 'a', 3, 'b'}

# Tambien se usa el update()
letras.update(numeros)
print(letras)

# ------------------------------
''' Para definir las intersecciones que hay entre dos conjuntos (objetos en comun) '''

set_tecnologias_harvard = {"Python", "Javascript", "AWS"}
set_tecnologias_oxford = {"Python", "Typescript", "GoogleCloud"}

set3 = set_tecnologias_harvard.intersection(set_tecnologias_oxford)
print(set3)
# Salida: {'Python'}

''' Tambien se puede usar para el mismo objetivo, el ampersand "&" '''
set4 = set_tecnologias_harvard & set_tecnologias_oxford
print(set4)
# Salida: {'Python'}

'''Tambien puedo actualizarlo con intersetion_update()'''
set_tecnologias_harvard.intersection_update(set_tecnologias_oxford)
print(set_tecnologias_harvard)
# Salida: {'Python'}

'''Si quiero hacer la diferencia de un set en vez de la interseccion'''
set5 = set_tecnologias_oxford.difference(set_tecnologias_harvard)
print(set5)

''' Tambien puedo usar el difference_update()'''
set_tecnologias_harvard.difference_update(set_tecnologias_oxford)
print(set_tecnologias_harvard)

''' Abreviatura con el simbolo menos (-)'''
set6 = set_tecnologias_harvard - set_tecnologias_oxford
print(set6)

''' Asi podemos copiar un conjunto'''

copia = set_tecnologias_harvard.copy()
print(copia)

# ----------------------------------------------
# BUCLES
# ----------------------------------------------

'''La unica forma de recorrer un set, es con un bucle for, ya que con el while requerimos del indice'''
frutas = {"Manzana", "Pera", "Banana"}

for fruta in frutas:
    print(fruta)