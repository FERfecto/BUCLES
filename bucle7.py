#coding: utf-8

minim = int(input("Escriba un número: "))
maxim = int(input("Escriba un número mayor que " + str(minim) + ": "))

while minim >= maxim:
	maxim = int(input(str(maxim) + " no es mayor que " + str(minim) + ".Inténtelo de nuevo: "))

num = float(input("Escriba un número entre " + str(minim) + " y " + str(maxim) + ": "))
contador = 0

while minim <= num <= maxim:
	contador += 1
	num = float(input("Escriba un número entre " + str(minim) + " y " + str(maxim) + ": "))

print()
if contador == 0:
    	print("No ha escrito ningún número entre", minim, "y", str(maxim) + ".")
elif contador == 1:
    	print("Ha escrito 1 número entre", minim, "y", str(maxim) + ".")
else:
    	print "Ha escrito", contador, "números entre", minim, "y", str(maxim) + "."
	print ("Programa terminado")
