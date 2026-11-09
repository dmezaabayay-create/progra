with open("diario.txt", "r", encoding= "utf-8") as archivo_diario:
    contenido = archivo_diario.read()

with open("copia.txt", "w", encoding= "utf-8") as archivo_copia:
    archivo_copia.write(contenido)
    
print("el contenido se ha copiado exitosamente a copia.txt.")