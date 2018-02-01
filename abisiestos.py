#coding: utf-8
def es_bisiesto (anyo):
	if (anyo%4==0 and anyo%100!=0)or anyo%400==0:
		print "el anyo", str(anyo), "es bisiesto"
	else:
		print "el anyo", str(anyo), "no es bisiesto"

print ("iniciando...")
es_bisiesto (2017)
es_bisiesto (1998)
es_bisiesto (1968)
