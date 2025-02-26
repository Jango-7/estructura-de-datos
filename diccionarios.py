# ----------------------------------------------
# DICCIONARIO: Coleccion no ordenada de pares clave:valor
# ----------------------------------------------

# diccionario = {
#     "nombre" : "Johan",
#     "tecnologias" : ["python", "JS"]
# }

# print(diccionario)
# print(diccionario["nombre"]) # Para acceder a un solo dato 


# '''METODO GET: Para asignarle un dato a una variable'''
# nombre = diccionario.get("nombre")
# print(nombre)


# '''Si quiero acceder solo a las claves'''
# claves = diccionario.keys()
# print(claves)
# # dict_keys(['nombre', 'tecnologias'])

# '''Si quiero cambiar el valor de una clave'''
# diccionario["tecnologias"] = "Ciecia de datos"
# print(diccionario)
# # {'nombre': 'Johan', 'tecnologias': 'Ciecia de datos'}

# '''Tambien puedo agregar informacion al diccionario poniendo una clave:valor que no existia'''
# diccionario["apellido"] = "Garcia"
# print(diccionario)
# # {'nombre': 'Johan', 'tecnologias': 'Ciecia de datos', 'apellido': 'Garcia'}

# ''' Para traer solo los valores'''
# valores = diccionario.values()
# print(valores)
# # dict_values(['Johan', 'Ciecia de datos', 'Garcia'])

# ''' Para traer solo los items '''
# items = diccionario.items() # Esto nos trae una lista de tuplas de clave. valor
# print(items)
# # dict_items([('nombre', 'Johan'), ('tecnologias', 'Ciecia de datos'), ('apellido', 'Garcia')])

# '''Tambien puedo saber si existe una clave, con el condicional'''
# if "nombre" in diccionario:
#     print("Existe!")
# else:
#     print("No existe!")


# ----------------------------------------------
# Cambiar, agregar y eliminar pares clave-valor
# ----------------------------------------------

# diccionario = {
#     "nombre" : "Johan",
#     "apellido" : "Garcia",
#     "tecnologias" : ["python", "JS"]
# }

# diccionario.update({"apellido" : "Osorio", "edad" : 25})
# print(diccionario)
# # {'nombre': 'Johan', 'apellido': 'Osorio', 'tecnologias': ['python', 'JS'], 'edad': 25}

# diccionario["ciudad"] = "Stutgard"
# print(diccionario)


# ''' Para borrar '''

# diccionario.pop("apellido")
# print(diccionario)
# # {'nombre': 'Johan', 'tecnologias': ['python', 'JS'], 'edad': 25, 'ciudad': 'Stutgard'}

# ''' Si quiero borrar el ultimo uso popitem '''
# diccionario.popitem()
# print(diccionario)
# # {'nombre': 'Johan', 'tecnologias': ['python', 'JS'], 'edad': 25}

# '''Tambien podemos usar como en las listas, el del, el clear.'''


# ----------------------------------------------
# Copiar diccionarios y utilización de bucles
# ----------------------------------------------

# '''IMPORTANTE: No puedo hacer una asignacion de un diccionario a una variable, porque no se hara una copia, sino que generara una referencia al mismo diccionario, por lo que puede traer comportamientos inadeacuados. Para copiar uso COPY'''

# copia = diccionario.copy()
# print(copia)

# '''La otra forma es usando el constructor'''
# copia2 = dict(diccionario)
# print(copia2)


# # ----------------------------------------------
# # Bucle
# # ----------------------------------------------

# '''De esta manera puedo acceder a la clave valor.'''
# for clave in diccionario:
#     print(f'{clave}: {diccionario[clave]}')

# ''' Si quiero solamente los valores'''
# for value in diccionario.values():
#     print(value)

# ''' Tambien puedo desempaquetar. "IMPORTANTE" '''
# for x,y in diccionario.items():
#     print(x, y)
# # A las X se le asigna la clave, y a la Y los valores



# ----------------------------------------------
# DICCIONARIOS ANIDADOS
# ----------------------------------------------

familia = {
    "Padre" : {
        "Nombre" : "Raul",
        "Profesion" : "Carpintero"
    },
    "Madre" : {
        "Nombre" : "Patricia",
        "Profesion" : "Abogada"
    },
    "Hijo" : {
        "Nombre" : "Pedro",
        "Profesion" : "Estudiante"
    }
}

''' Acceder a los items internos '''

print(familia["Padre"]["Profesion"])

'''Podemos acceder a traves de un bucle'''

for pariente, data in familia.items():
    print('\n', pariente)

    for clave in data:
        print(f'{clave}: {data[clave]}')