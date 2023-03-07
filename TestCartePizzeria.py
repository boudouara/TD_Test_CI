import unittest

from CartePizzeria import CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
     
    def test_is_empty(self):
        carte = CartePizzeria()
        self.assertTrue(self.carte.is_empty())
        carte.add_pizza({'name': 'Margherita', 'price': 10})
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas(self):
        carte = CartePizzeria()
        self.assertEqual(carte.nb_pizzas(), 0)
        carte.add_pizza({'name': 'Margherita', 'price': 10})
        self.assertEqual(carte.nb_pizzas(), 1)
    
    def test_add_pizza(self):
        carte = CartePizzeria()
        carte.add_pizza({'name': 'Margherita', 'price': 10})
        self.assertEqual(carte.nb_pizzas(), 1)

    
    def test_remove_pizza(self):
        carte = CartePizzeria()
        carte.add_pizza({'name': 'Margherita', 'price': 10})
        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 0)
    
if __name__ == "__main__":
    unittest.main() 