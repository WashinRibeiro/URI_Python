from math import sqrt

valores1 = input().split(" ")
valores2 = input().split(" ")
x1, y1 = valores1
x2, y2 = valores2

distancia = sqrt(((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2))
print(f'{distancia:.4f}')
