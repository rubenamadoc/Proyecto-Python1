import time
import random
import string
vcovid=str("ccucggcgggca")#Creo la variable con la cadena del virus conocida.
cod=input("Identifiquese:")#Recogo el código del paciente.
cadena=string.ascii_lowercase#Defino la variable de cadena.
print("Informe de Virus COVID:")
print("Fecha:",time.strftime('%d-%m-%Y'))
print("Hora:",time.strftime ('%H:%M:%S'))
print("Código del paciente:",cod)
print("Resultado:")
cadenaf="".join(random.choices(cadena,k=50))#Genero una cadena variable de longitud 50 y letras minusculas
print(cadenaf)#Muestro la cadena creada
if vcovid in cadenaf:
    print("Positivo: Sí se encunetran restos de la variante COVID.")
    resultado="positivo"
else:
    print("Negativo: No se encuentra restos de la variante.")
    resultado="negativo"#Condicional(Cadena vcovid dentro de cadenaf)
resultados=(time.strftime('%d-%m-%Y'),time.strftime ('%H:%M:%S'),cod,resultado)
lista=list(resultados)
file = open("virus.txt","a")
file.write('muestra = %s' % lista + '\n')
file.close()