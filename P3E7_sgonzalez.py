#Práctica 3 - Introducción a Python
#P3E7_sgonzalez
#PIDA AL USUARIO TRES NÚMEROS QUE SERÁN EL DÍA, MES Y AÑO. COMPRUEBA 
#QUE LA FECHA INTRODUCIDA ES VÁLIDA.

print ("Introduce una fecha en formato día/mes/año y te diré si es \
correcta")

dia=int(input("Introduce el día "))
mes=int(input("Introduce el mes "))
año=int(input("Introduce el año "))


if ((dia>31)or(dia<=0)or(mes>12)or(mes<=0)or(año<=0)):
    print (dia, "/", mes, "/", año, "no es una fecha correcta.")
elif ((mes==2 and dia>28)or(mes==4 and dia>30)or(mes==6 and dia>30)or\
(mes==9 and dia>30)or(mes==11 and dia>30)):
    print (dia, "/", mes,"/", año, ", no es una fecha correcta")
else:
    print (dia, "/", mes, "/", año, "es una fecha correcta.")

print ("FIN.")





