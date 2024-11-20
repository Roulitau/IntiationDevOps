import unittest
from app import addiction, soustraction, division, multiplication

"""
Ce module contient des tests unitaires pour vérifier le bon fonctionnement des fonctions 
arithmétiques définies dans le module 'app'. Il teste l'addition, la soustraction, 
la multiplication et la division.
"""

class TestCalculator(unittest.TestCase):
    """Classe de tests unitaires pour le module 'app'."""

    def test_addiction(self):
        """Teste la fonction d'addition."""
        self.assertEqual(addiction(3, 5), 8)
        self.assertEqual(addiction(-1, 1), 0)
        self.assertEqual(addiction(0, 0), 0)
    
    def test_soustraction(self):
        """Teste la fonction de soustraction."""
        self.assertEqual(soustraction(10, 5), 5)
        self.assertEqual(soustraction(0, 7), -7)
        self.assertEqual(soustraction(3, 3), 0)

    def test_multiplication(self):
        """Teste la fonction de multiplication."""
        self.assertEqual(multiplication(4, 3), 12)
        self.assertEqual(multiplication(-1, 8), -8)
        self.assertEqual(multiplication(0, 5), 0)

    def test_division(self):
        """Teste la fonction de division."""
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        with self.assertRaises(ValueError):  # Teste la division par zéro
            division(5, 0)

if __name__ == '__main__':
    unittest.main()

