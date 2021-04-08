valor = input().split(" ")
a, b, c = valor
pi = 3.14159

print(f'TRIANGULO: {(float(a) * float(c))/2:.3f}\n'
      f'CIRCULO: {pi * (float(c)* float(c)):.3f}\n'
      f'TRAPEZIO: {float(c) *(float(a) + float(b)) / 2:.3f}\n'
      f'QUADRADO: {float(b) * float(b):.3f}\n'
      f'RETANGULO: {float(a) * float(b):.3f}')