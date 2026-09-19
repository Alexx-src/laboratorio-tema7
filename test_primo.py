# test_primo.py
# Test unitario - escrito PRIMERO (TDD)

import unittest
from primo import es_primo   # importamos la función que todavía no existe


class TestNumeroPrimo(unittest.TestCase):

    def test_numero_primo(self):
        """Debe devolver True para números primos"""
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(11))
        self.assertTrue(es_primo(13))

    def test_numero_no_primo(self):
        """Debe devolver False para números que no son primos"""
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(8))
        self.assertFalse(es_primo(9))
        self.assertFalse(es_primo(15))

    def test_numeros_negativos_y_cero(self):
        """Debe devolver False para 0 y números negativos"""
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(-3))
        self.assertFalse(es_primo(-7))


if __name__ == "__main__":
    unittest.main()