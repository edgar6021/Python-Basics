# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
# Verificar si el número es impar.
 if number % 2 == 1:
# Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
else:
# Incrementar el contador de números pares even_numbers.
        even_numbers += 1
# Leer el siguiente número.
number = int(input("Introduce un número o escribe 0 para detener: "))
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

