import random
import math

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
cantidad = int(input("Ingrese la cantidad de puntos: "))

puntos_elipse = 0
puntos_interseccion = 0

for i in range(cantidad):
    x = random.uniform(-a, a)
    y = random.uniform(-b, b)

    if x**2 / a**2 + y**2 / b**2 <= 1:
        puntos_elipse += 1
        if x**2 / c**2 - y**2 / d**2 >= 1:
            puntos_interseccion += 1

area_elipse = math.pi * a * b
area_interseccion = 0
if puntos_elipse > 0:
    area_interseccion = area_elipse * puntos_interseccion / puntos_elipse

print("Puntos dentro de la elipse:", puntos_elipse)
print("Puntos en la interseccion:", puntos_interseccion)
print("Area aproximada de la interseccion:", area_interseccion)
