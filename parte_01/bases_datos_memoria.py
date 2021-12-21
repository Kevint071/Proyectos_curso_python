import sqlite3
import pandas as pd
import pathlib

conexion = sqlite3.connect(":memory:")
cursor = conexion.cursor()

sql_tabla_estudiante = "CREATE TABLE estudiante(carnet TEXT, nombre TEXT, apellido TEXT, carrera TEXT, semestre INT, CONSTRAINT carnet_pk PRIMARY KEY (carnet))"

cursor.execute(sql_tabla_estudiante)

sql_consulta_tablas = "SELECT * FROM SQLite_master WHERE type=\"table\""

cursor.execute(sql_consulta_tablas)

print("Tablas disponibles en la base de datos: ")
tablas = cursor.fetchall()

for i in tablas:
    print(f"El nombre tipo objeto en al base de datos: {i[0]}")
    print(f"El nombre objeto BD: {i[1]}")
    print(f"El nombre tabla: {i[2]}")
    print(f"Sentencia SQL: {i[4]}")

datos = [("1001", "Edwar", "Ortiz", "Informática", 5),
 ("1002", "Daniela", "Ordonez", "Arte", 3),
 ("1003", "Germán", "Meneses", "Programación", 7),
 ("1004", "Oliva", "Urbano", "Música", 5)]

try:
    sql = '''INSERT INTO estudiante (carnet, nombre, apellido, carrera, semestre) VALUES (?, ?, ?, ?, ?)'''
    cursor.executemany(sql, datos)
except sqlite3.IntegrityError as e:
    print(f"Error SQLite: {e.args[0]}")

conexion.commit()

sql = "SELECT * FROM estudiante WHERE carnet = '1004'"
cursor.execute(sql)
resultado = cursor.fetchall()
print(resultado)

print()

#Convertir la informacion de la base de datos en un archivo csv separado por comas

sql = "SELECT * FROM estudiante"
df = pd.read_sql_query(sql, conexion)

#Hallar el directorio dependiendo de en que carpeta esté el usuario

"""
    Aquí se obtiene el directorio del archivo actual:
    directorio = pathlib.Path(__file__).parent.absolute()
"""

# Aquí se obtiene el directorio de la carpeta actual

directorio = pathlib.Path().absolute()
directorio = str(directorio)

lista_directorio = []

for i in directorio:
    lista_directorio.append(i)

if lista_directorio[-1] == "n":
    df.to_csv('venv/parte_01/estudiantes.csv', index=0)
elif lista_directorio[-1] == "v":
    df.to_csv('parte_01/estudiantes.csv', index=0)
else:
    df.to_csv('estudiantes.csv', index=0)