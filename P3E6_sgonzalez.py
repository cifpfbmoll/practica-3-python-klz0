#Práctica 3 - Introducción a Python
#P3E6_sgonzalez
#PIDA AL USUARIO EL PRECIO DE UN PRODUCTO Y EL NOMBRE DEL PRODUCTO
#Y MUESTRE EL MENSAJE CON EL PRECIO DEL IVA (21%) POR EJEMPLO: "TU
# BICICLETA VALE 100 EUROS Y CON EL 21% DE IVA SE QUEDA EN 121 EUROS"

producto=input("Introduce el producto que quieres comprar ")
precio=float(input("Introduce el precio del producto "))
iva=(precio*0.21)

print ("El precio de tu", producto,"es de", precio,"y con el 21% de \
IVA se queda en", (precio+iva))

print ("FIN.")




