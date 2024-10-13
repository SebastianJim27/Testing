import unittest

class CalculadoraLogica:
    def calcular(self, expression):
        try:
            return eval(expression)
        except Exception:
            return "Error"

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = CalculadoraLogica()

    def test_suma(self):
        self.assertEqual(self.calc.calcular("2+3"), 5)

    def test_resta(self):
        self.assertEqual(self.calc.calcular("10-4"), 6)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.calcular("2*3"), 6)

    def test_division(self):
        self.assertEqual(self.calc.calcular("8/2"), 4)

    def test_error(self):
        self.assertEqual(self.calc.calcular("8/0"), "Error")

if __name__ == '__main__':
    unittest.main()
