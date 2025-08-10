##numero 8
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print("El número mayor es:", mayor)
##numero 9
numero = input("Ingresa un número entero: ")
suma = 0
for digito in numero:
    suma += int(digito)

print("La suma de los dígitos es:", suma)
##numero10
frase = input("Ingresa una frase: ")
contador = 1 if frase.strip() != "" else 0

for caracter in frase:
    if caracter == " ":
        contador += 1

print("Número de palabras:", contador)
##numero11
lista = list(range(1, 11))
lista.reverse()
print("Lista inversa:", lista)
##numero12
import random

numeros = []
while len(numeros) < 5:
    n = random.randint(1, 20)
    if n not in numeros:
        numeros.append(n)

print("Números aleatorios:", numeros)
##numero13
import random
secreto = random.randint(1, 10)
intentos = 3

while intentos > 0:
    intento = int(input("Adivina el número entre 1 y 10: "))
    
    if intento == secreto:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < secreto:
        print("Pista: el número es mayor.")
    else:
        print("Pista: el número es menor.")
    
    intentos -= 1

if intentos == 0:
    print("Se acabaron los intentos. El número era:", secreto)
##numero14
lista = []
for i in range(1, 61):
    if i % 3 == 0:
        lista.append(i)

print("Múltiplos de 3 entre 1 y 60:", lista)
