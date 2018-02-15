#coding: utf-8

uno = int(input("escriba un numero:"))
dos = int(input("escriba un numero mayor" + str(uno) + ": "))

while dos <= uno:
	print (dos, "no es mayor que", str(uno) + "intentelo de nuevo: ")
	dos = int(input())
	
print ("los numeros que has escrito son", uno, "y", dos)
print ("Programa terminado")



