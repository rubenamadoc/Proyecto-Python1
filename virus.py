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
for _ in range(50):
    cadenaf = random.choice(cadena)#Genero la cadena aleatoria.
    cadenafinal=print(cadenaf,end="")
    result=cadenafinal.includes(vcovid)#Condicional. Si la cadena de covid está dentro de la cadena generada, el paciente será positivo.
    if result == True:
        print("Positivo: Sí se encunetran restos de la variante COVID.")
    else:
        print("Negativo: No se encuentra restos de la variante.")
resultados=(time.strftime('%d-%m-%Y'),time.strftime ('%H:%M:%S'),cod,result)