# figuras_solid.py
# Aplicación de principios SOLID (SRP + OCP)

from abc import ABC, abstractmethod
import math


# ===== Abstracción (OCP + SRP) =====
class FiguraGeometrica(ABC):
    """
    Clase base abstracta.
    Responsabilidad única: definir el contrato de una figura.
    """
    @abstractmethod
    def calcular_area(self) -> float:
        pass

    @abstractmethod
    def nombre(self) -> str:
        pass


# ===== Figuras concretas (cada una con una sola responsabilidad) =====
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def nombre(self) -> str:
        return "Cuadrado"


class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def nombre(self) -> str:
        return "Rectangulo"


class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def nombre(self) -> str:
        return "Triángulo"


class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio ** 2)

    def nombre(self) -> str:
        return "Circulo"


# ===== Nueva figura agregada SIN modificar el código anterior (OCP) =====
class Pentagono(FiguraGeometrica):
    """
    Nueva figura agregada sin tocar las clases existentes.
    Esto demuestra el principio Open/Closed.
    """
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        # Formula del area de un pentagono regular
        return (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.lado ** 2)

    def nombre(self) -> str:
        return "Pentagono"


# ===== Cliente que usa las figuras (no necesita modificarse) =====
def mostrar_area(figura: FiguraGeometrica):
    """
    Esta función trabaja con cualquier figura que cumpla el contrato.
    No se modifica al agregar nuevas figuras.
    """
    print(f"El área del {figura.nombre()} es: {figura.calcular_area():.2f}")


# ===== Demostración =====
if __name__ == "__main__":
    figuras = [
        Cuadrado(5),
        Rectangulo(4, 6),
        Triangulo(5, 8),
        Circulo(3),
        Pentagono(4)          # ← Nueva figura agregada sin modificar nada más
    ]

    print("=== Cálculo de áreas con principios SOLID ===\n")
    for figura in figuras:
        mostrar_area(figura)