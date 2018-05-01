
cal1=int(input("Ingrese la calificacion 1: "))
cal2=int(input("Ingrese la calificacion 2: "))
cal3=int(input("Ingrese la calificacion 3: "))
cal4=int(input("Ingrese la calificacion 4: "))

med=int
med=cal1+cal2+cal3+cal4

if med>=90 :
	print("El estudiante con el promedio de calificacion {0} tiene una puntiacion de A".format(med))
else:
	if med>=80 and med<=89 :
		print("El estudiante con el promedio de calificacion {0} tiene una puntuacion de B".format(med))
	else:
		if med>=70 and med<=79 :
			print("El estudiante con el promedio de califiacion {0} tiene una puntuacion de C".format(med))
		else:
			if med<70 :
				print("El estuadiante con el promedio de califiacion {0} tiene una puntuacion de D".format(med))