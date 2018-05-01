ventas=int(input("Ingrese las ventas del empleado: "))
sueldo=float
aumento=float
sueldof=float
sueldo=360.40
if ventas>5000:
	aumento=vent*0.15
	sueldof=aumento+sueldo;
	print("El sueldo final sera de: {0}".format(sueldof))
else:
	if ventas>1000 and vent<=5000:
		aumento=vent*0.10
		sueldof=aumento+sueldo
		print("El sueldo final sera de: {0}".format(sueldof))
	else:
		if ventas>500 and ventas<=1000:
			aumento=vent*0.08
			sueldof=aumento+sueldo
			print("El sueldo final sera de: {0}".format(sueldof))
		else:
			if ventas<=500:
				aumento=ventas*0.05
				sueldof=aumento+sueldo
				print("El sueldo final sera de: {0} $".format(sueldof))