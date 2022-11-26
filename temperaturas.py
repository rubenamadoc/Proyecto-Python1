# La junta de andalucía quiere hacer un estudio de como está afectando
# el cambio climático en Parque Natural de Doñana.
# Se tiene que hace un script, donde se recoja las temperaturas hasta que se pulse 100
# y recogerá esa información y hará un informe. Por último creará una tupla 
# con las termperaturas de cada día.

import time #Importa librerias de fecha y hora
import os #Importa la libreria del sistema
temperaturas = [] #De esta manera inicializo una tarea
while True:
    temp = float(input("Introduce la temperatura:"))
    if temp == 100:
        break;
    temperaturas.append(temp)
#Bucle que va a recoger las temraturas y las añade a la lista hasta que pulse 100.
os.system ("clear")#Limpia la pantalla
print("Informe de temperaturas del Parque Natural de Doñana:")
print("Fecha:",time.strftime('%d-%m-%Y'))#Muestra la fecha del sistema
print("Hora:",time.strftime ('%H:%M:%S'))#Muestra la hora del sistema
print("Numero de muestras:", len(temperaturas))#Muestra numero total de elementos
print("Temperaturas tomadas:", temperaturas)#Muestra todos los elementos
print("Temperatura maxima:", max(temperaturas))#Muestra el valor maximo
print("Temperatura maxima:", min(temperaturas))#Muestra el valor minimo
media = sum(temperaturas) / len(temperaturas)#Realiza una media
print("Temperatura media", round(media, 1))#Redondea la media a un decimal
ar_temp = (time.strftime('%d-%m-%Y'),time.strftime ('%H:%M:%S'),temperaturas)#Guarda la fecha, hora y temperaturas en una tupla
lista = list(ar_temp)#Convierte la tupla en lista para que pueda ser escrito en fichero txt
file = open("temperaturas.txt", "a")#Crea o abre si ya existe un fichero en modo append (escribe sin borrar el contenido anterior)
file.write('temperaturas = %s' % lista + '\n' )#Escribe la informacion de la tupla convirtiendola en cadena
file.close()#Cierra el fichero (Necesario, porque si no el programa seguiria esperando mas informacion y no guardaria el fichero)