#with open("datos.csv", "w") as archivo:
#    archivo.write("nombre, edad, ciudad\n")
#    archivo.write("ana, 21, chicago\n")
#    archivo.write("andre, 17, santiago\n")
#    archivo.write("demian, 18, coquimbo")
    
#with open("datos.csv", "r") as archivo:
#    for linea in archivo:
#        valores = linea.strip().split(",")
#        print(valores)

#with open("datos.csv", "r") as archivo:
#    lineas = archivo.readlines()
    
#for linea in lineas[1:]:
#    nombre, edad, ciudad = linea.strip().split(",")

#    print(f"{nombre} tiene {edad} años y vive en {ciudad}. ")

#personas = "las personas precentes en la base de datos son: \n"

#for linea in lineas[1:]:
#    registroActual = linea.strip().split(",")
#    personas += registroActual[0]
#    personas += "\n"
#print(personas)

#productos = [
#    ("producto", "precio"),
#    ("salchipapa", "500"),
#    ("maruchan", "600"),
#    ("pan", "300")
#]

#with open("productos.csv", "w") as archivo:
#    for fila in productos:
#        archivo.write(";". join(fila) + "\n")

#with open("productos.csv", "r") as archivo:
#    print(archivo.read())

import csv

#with open("datos.csv", "r") as archivo:
#    lector = csv.reader(archivo)
#    for fila in lector:
#        print(fila)
