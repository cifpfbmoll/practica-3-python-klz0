#Práctica 3 - Introducción a Python
#P3E5_sgonzalez 
#PIDA UN NÚMERO QUE COMO MÁXIMO TENGA 3 CIFRAS. SI EL USUARIO INTRODUCE
#UN NÚMERO DE MÁS DE TRES CIFRAS DEBE INFORMAR CON UN MENSAJE DE ERROR
#COMO ESTE "ERROR:EL NÚMERO 1005 TIENE MÁS DE 3 CIFRAS".


numero=int(input("Introduzca un número de 3 cifras "))

if (numero<1000):
    print ("El número que ha elegido es el ", numero)
else:
    print ("ERROR: El número ", numero," tiene más de tres cifras.")
    numero=int(input("Introduzca un número correcto de 3 cifras "))

print ("FIN.")



