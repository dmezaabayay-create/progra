nombre_archivo = "uwu.txt"

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    
total_lineas = len(lineas)
total_caracteres = len(contenido)
total_palabras = len(contenido.split())

print(f"total de lineas: {total_lineas}")
print(f"total de caracteres: {total_caracteres}")
print(f"total de palabras: {total_palabras}")
archivo.close()