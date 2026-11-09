from datetime import datetime

archivo = open("diario.txt","a")
entrada = input("¿que quieres?: ")

archivo.write(str(datetime.today()))
archivo.write(entrada)


print(str(datetime.today().strftime("%D")))

archivo.close()