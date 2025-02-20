
# lista = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Piña"]
# lista2 = ["Lulo", "Kiwi", "Guanabana"]

# print(lista[0]) # Asi ingreso al indice de la lista
# print(lista[-1]) # Asi ingreso al ultimo indice hacia atras
# print(lista[1:3]) # Asi ingreso a una parte de la lista, segun el indice. El ultimo no incluido.

# # Con el "in" podemos ver si algun elemento esta en la lista
# if "Banana" in lista:
#     print("Esa fruta esta en la lista")
# else:
#     print("Esa fruta no esta en la lista")

# # De esta manera, puedo cambiar un elemento por otro en la lista.
# lista[1] = "Plátano"
# print(lista)

# # De esta manera puedo modificar una parte de la lista (ultimos dos elementos en este caso)
# lista[4:] = ["Frutilla", "Ananá"]
# print(lista)

# # INSERTAR ELEMENTO (indice + item)
# lista.insert(2, "Aguacate")
# print(lista)

# # AGREGAR ITEM AL FINAL
# lista.append("Maracuyá")
# print(lista)

# # UNIR DOS LISTAS (Tambien puedo lista + tupla)
# lista.extend(lista2)
# print(lista)

# # BORRAR UNA ELEMENTO (Borra la primera ocurrencia si hubieran dos)
# lista.remove("Frutilla")
# print(lista)

# # BORRAR POR INDICE O EL ULTIMO INDICE
# lista.pop(2) 
# print(lista)

# del lista[0]
# print(lista)

# # Limpiar toda la lista
# lista.clear()
# print(lista)


# ----------------------------
# BUCLES EN LISTAS
# ----------------------------

# frutas = ["Manzana", "Banana", "Pera", "Mandarina", "Fresa", "Piña"]

# # bucle for -------------
# for fruta in frutas:
#     print(fruta)

# # Shorthand de for
# [print(fruta) for fruta in frutas]

# # Bucle con indice disponible --------
# for i in range(len(frutas)):
#     print(i)
#     print(frutas[i])

# # Bucle while ----------
# i = 0
# while i < len(frutas):
#     print(i)
#     print(frutas[i])
#     i += 1


# ----------------------------
# ABREVIACIONES EN LISTAS
# ----------------------------

frutas = ["Manzana", "banana", "Pera", "Mandarina", "Fresa", "Piña"]

# Quiero hacer una copia de "frutas", pero solo con las frutas que contengan la letra e... -------

# frutas_con_e = []

# for fruta in frutas:
#     if "e" in fruta:
#         frutas_con_e.append(fruta)

# print(frutas_con_e)

# Ahora, como puedo reducir este codigo? ---------------

# frutas_con_e = [fruta for fruta in frutas if "e" in fruta]

# print(frutas_con_e)

# Tambien puedo usarlo para sacar un elemento ---------
# <<Traeme la fruta por cada fruta en la lista de frutas, si la fruta es distinta de mandarina.>>
frutas_con_e = [fruta for fruta in frutas if fruta != "Mandarina"]
print(frutas_con_e)

# Para poner todo en Mayuscula
# << Traeme la fruta en Mayuscula, por cada fruta en la lista de frutas>>
mayusculas = [fruta.upper() for fruta in frutas]
print(mayusculas)

# Quiero que me imprima la fruta si es distinta a PERA, y sino es distinta, que imprima AGUACATE. 
frutas2 = [fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]
print(frutas2)

# ----------------------------
# ORDENAMIENTO DE LISTAS
# ----------------------------

# Voy a ordenar las frutas alfabeticamente
frutas.sort()
print(frutas)

numeros = [9,999,88,1,2,3]
numeros.sort()
print(numeros)

# Ordenar al reves
frutas.sort(reverse=True)
print(frutas)

# Sort es key sensitive, por lo cual si mi lista tiene algunos elementos con mayuscula y otros no, los va ordenar distinto. Para que ordene alfabeticamente independiente de las mayusculas, debo hacer esto:

frutas.sort(key=str.lower)
print(frutas)

# Asi le doy vuelta al orden, de atras para adelante
frutas.reverse()
print(frutas)