# calculator.py

"""
Ce module contient des fonctions de base pour effectuer des opérations arithmétiques simples
comme l'addition, la soustraction, la multiplication et la division. Il fournit également un 
exemple d'utilisation avec des affichages.
"""

def addiction(a, b):
    """Additionne deux nombres."""
    return a + b

def soustraction(a, b):
    """Soustrait le second nombre du premier."""
    return a - b

def multiplication(a, b):
    """Multiplie deux nombres."""
    return a * b

def division(a, b):
    """Divise le premier nombre par le second."""
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b

# Exemple d'utilisation (démonstration)
print("Bienvenue dans le calculateur !")
print("Exemple d'utilisation :")
print(f"Addition : 4 + 5 = {addiction(4, 5)}")
print(f"Soustraction : 9 - 2 = {soustraction(9, 2)}")
print(f"Multiplication : 3 * 3 = {multiplication(3, 3)}")
print(f"Division : 8 / 2 = {division(8, 2)}")