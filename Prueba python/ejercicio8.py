letra1=input("Ingrese la primera letra: ")
letra2=input("Ingrese la segunda letra: ")
letra3=input("Ingrese la tercera letra: ")
if letra1<letra2 and letra1<letra3:
	print("La primera letra en el abecedario es: \n {0}".format(letra1))
else:
	if letra2<letra1 and letra2<letra3:
		print("La primera letra en el abecedario es: \n {0}".format(letra2))
	else:
		if letra3<letra1 and letra3<letra2:
			print("La primera letra en el abecedario es: \n {0}".format(letra3))