import json, pickle, pathlib as pl

datos = {}

datos["programadores"] = []

edwar = {"id": 1001, "nombre": "Edwar", "apellido": "Ortiz", "especialidad": "Front-end", "lenguaje": "Javascript", "e-mail": "edward@mail.co"}

oliva = {"id": 1002, "nombre": "Oliva", "apellido": "Ortiz", "especialidad": "Back-end", "lenguaje": "Java", "e-mail": "oliva@mail.co"}

juan = {"id": 1003, "nombre": "Juan", "apellido": "Urbano", "especialidad": "Front-end", "lenguaje": "Javascript", "e-mail": "Juan@mail.co"}

datos["programadores"].append(edwar)
datos["programadores"].append(oliva)
datos["programadores"].append(juan)

print("Cantidad de datos en el diccionario: ", len(datos["programadores"]))

#En esta parte se escriben los archivos json

directorio_actual = pl.Path().absolute()
directorio_actual = str(directorio_actual)

if directorio_actual[-1] == "n":
    directorio_archivo = "venv/parte_01/programadores.json"

elif directorio_actual[-1] == "v":
    directorio_archivo = "parte_01/programadores.json"

else:
    directorio_archivo = "programadores.json"

with open(directorio_archivo, "w") as f:
    json.dump(datos, f)

with open(directorio_archivo, "r") as f:
    datos_programadores = json.load(f)
    f.close()
print("Cantidad de datos en el diccionario con json: ", len(datos_programadores["programadores"]))

print("\nDatos de programadores con json\n")

for p in datos_programadores["programadores"]:
    print("ID: %i" % p["id"])
    print("Nombre: %s"% p["nombre"])
    print("Apellido: %s"% p["apellido"])
    print("Especialidad: %s"% p["especialidad"])
    print("Lenguaje: %s"% p["lenguaje"])
    print("E-mail: %s"% p["e-mail"])
    print()

# Persistencia de un archivo binario:

directorio_archivo = directorio_archivo.replace("json", "pkl")

with open(directorio_archivo, "wb") as f:
    pickle.dump(datos, f, protocol=pickle.HIGHEST_PROTOCOL)

# Lectura de un archivo binario

with open(directorio_archivo, "rb") as f:
    datos_deserializados = pickle.load(f)
    f.close()

print("Datos de programadores co pickle\n")

for p in datos_deserializados["programadores"]:
    print("ID: %i" % p["id"])
    print("Nombre: %s"% p["nombre"])
    print("Apellido: %s"% p["apellido"])
    print("Especialidad: %s"% p["especialidad"])
    print("Lenguaje: %s"% p["lenguaje"])
    print("E-mail: %s"% p["e-mail"])
    print(datos_deserializados["programadores"][-1]["e-mail"])
    if p == datos_deserializados["programadores"][-1]:
        break
    else:
        print()

