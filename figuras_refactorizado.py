# figuras_refactorizado.py
# Versión refactorizada - código limpio y modular

class FiguraGeometrica:
    """Clase base para figuras geometricas"""
    
    def calcular_area(self):
        raise NotImplementedError("Este metodo debe ser implementado por las subclases")


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)


# ----- Uso del código refactorizado -----
if __name__ == "__main__":
    cuadrado = Cuadrado(5)
    rectangulo = Rectangulo(4, 6)
    triangulo = Triangulo(5, 8)
    circulo = Circulo(3)

    print(f"Area del cuadrado: {cuadrado.calcular_area()}")
    print(f"Area del rectángulo: {rectangulo.calcular_area()}")
    print(f"Area del triángulo: {triangulo.calcular_area()}")
    print(f"Area del círculo: {circulo.calcular_area()}")