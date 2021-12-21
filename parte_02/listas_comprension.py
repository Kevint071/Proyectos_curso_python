numeros = [8, 2, 3, 5, 12, 10, 13, 19, 7, 11, 6, 1]

print(f"\nLista: {numeros}\n")

tipo_dato = str(type(numeros))
tipo_dato = tipo_dato.strip("<>clas")
tipo_dato = tipo_dato.strip(" '")

print(f"Tipo de dato: {tipo_dato}")
print(f"Cantidad de elementos: {len(numeros)} \n")

numeros_filtrados = list(filter(lambda x: True if x % 2 == 0 else False, numeros))
numeros_triplicados = list(map(lambda x: x * 3, numeros_filtrados))
