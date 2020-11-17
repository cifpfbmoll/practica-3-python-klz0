#Práctica 3 - Introducción a Python
#P3E2_sgonzalez
#PIDA AL USUARIO EL ESPACIO RECORRIDO POR UN COCHE Y EL TIEMPO QUE HA 
#TARDADO EN HORAS Y QUE CALCULE A QUÉ VELOCIDAD MEDIA HABÍA REALIZADO
#EL RECORRIDO.

print ("Vamos a calcular la velocidad media de tu trayecto...")
espacio=int(input("Dime cuántos kilómetros has recorrido "))
minutos=int(input("Dime cuántos minutos has tardado "))
tiempo=float(minutos/60)
vmedia=(espacio/tiempo)
print ("Has tardado", tiempo,"horas en recorrer", espacio, "por lo que \
tu velocidad media ha sido de", int(vmedia))
print ("FIN.")



