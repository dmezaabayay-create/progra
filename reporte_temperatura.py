def crearReporte(temperaturas):
    # Abrimos el archivo 'informe.txt' en modo escritura ('w') con codificación utf-8
    with open("informe.txt", "w", encoding="utf-8") as archivo:
        # Recorremos el diccionario obteniendo la ciudad y la tupla (minima, maxima)
        for ciudad, (minima, maxima) in temperaturas.items():
            # Escribimos en el archivo respetando el formato exacto del ejemplo
            archivo.write(f"{ciudad}: max {maxima}°, min {minima}°\n")

# Diccionario
temp = {
    "Viña del Mar": (9, 26),
    "Valparaiso": (10, 24),
    "Quilpue": (7, 30),
    "Quintero": (4, 22)
}

# Llamamos a la función
crearReporte(temp)