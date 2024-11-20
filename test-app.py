import unittest

from app import addiction, soustraction, division, multiplication

class TestCalculator(unittest.TestCase):

    def test_addiction(self):
        self.assertEqual(addiction(3, 5), 8)
        self.assertEqual(addiction(-1, 1), 0)
        self.assertEqual(addiction(0, 0), 0)
    
    def test_soustraction(self):
        self.assertEqual(soustraction(10, 5), 5)
        self.assertEqual(soustraction(0, 7), -7)
        self.assertEqual(soustraction(3, 3), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)
        self.assertEqual(multiplication(-1, 8), -8)
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        with self.assertRaises(ValueError):  # Teste la division par zéro
            division(5, 0)

if __name__ == '__main__':
    unittest.main()