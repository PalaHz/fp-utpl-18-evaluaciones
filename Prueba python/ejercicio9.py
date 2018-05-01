
l1=int(input("Ingrese el lado 1 del triangulo 1 : "))
l2=int(input("Ingrese el lado 2 del triangulo 1 : "))
l3=int(input("Ingrese el lado 3 del triangulo 1 : "))
l4=int(input("Ingrese el lado 1 del triangulo 2 : "))
l5=int(input("Ingrese el lado 2 del triangulo 2 : "))
l6=int(input("Ingrese el lado 3 del triangulo 2 : "))

a1=int(input("Ingrese el angulo 1 del triangulo 1 : "))
a2=int(input("Ingrese el angulo 2 del triangulo 1 : "))
a3=int(input("Ingrese el angulo 3 del triangulo 1 : "))
a4=int(input("Ingrese el angulo 1 del triangulo 2 : "))
a5=int(input("Ingrese el angulo 2 del triangulo 2 : "))
a6=int(input("Ingrese el angulo 3 del triangulo 2 : "))


if a1 ==a4 and a2==a5 and a3==a6 and l1==l4 and l2==l5 and l3==l6:
	print("Son congruentes")
else:
	print("No son congruentes")