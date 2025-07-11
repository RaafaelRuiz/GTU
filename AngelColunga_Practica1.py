import math

x1, y1 = 10, 17
x2, y2 = 8, 16

distancia_manhattan = abs(x1 - x2) + abs(y1 - y2)

distancia_euclidiana = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print("Punto 1: (", x1, ",", y1, ")")
print("Punto 2: (", x2, ",", y2, ")")
print("Distancia Manhattan:", distancia_manhattan)
print("Distancia Euclidiana:", distancia_euclidiana)
