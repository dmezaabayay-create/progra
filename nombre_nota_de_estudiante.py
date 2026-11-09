with open("notas.txt", "r", encoding="utf-8") as entrada, open("informe_notas.txt", "w", encoding="utf-8") as salida:
    for linea in entrada:
        linea = linea.strip() 
        if not linea:
            continue
        
        
        partes = linea.split(":")
        nombre = partes[0]
        
        
        notas = [float(nota) for nota in partes[1:]]
        
      
        promedio = sum(notas) / len(notas)
        
        
        if promedio >= 4.0:
            estado = "aprobado"
        else:
            estado = "reprobado"
            
        
        salida.write(f"{nombre} {estado}\n")

print("El archivo 'informe_notas.txt' se ha generado correctamente.")