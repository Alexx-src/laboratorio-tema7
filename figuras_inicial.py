# figuras_inicial.py
# Versión inicial - código sin refactorizar

def calcular(tipo, a=0, b=0, c=0):
    if tipo == 1:  # cuadrado
        return a * a
    elif tipo == 2:  # rectangulo
        return a * b
    elif tipo == 3:  # triangulo
        return (a * b) / 2
    elif tipo == 4:  # circulo
        return 3.1416 * a * a
    else:
        return 0

# Pruebas rápidas
print("Área cuadrado:", calcular(1, 5))
print("Área rectángulo:", calcular(2, 4, 6))
print("Área triángulo:", calcular(3, 5, 8))
print("Área círculo:", calcular(4, 3))