print("Hola, bienvenido a mi programa")

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo o cero")

contador = 1

while contador <= numero:
    print("Operacion numero:", contador)
    contador += 1