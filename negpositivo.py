#coding: utf-8

num = int(input("escribe un numero: "))
suma=0

while num > 0:
	suma+= num
	num = int(input("escriba otro numero: "))
	
print "La suma de los numeros positivos es", str(suma) + "."

