import unittest
from unittest.mock import Mock
from CartePizzeria import CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()

    def test_is_empty(self):
        self.assertTrue(self.carte.is_empty())

    def test_nb_pizzas(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_add_pizza(self):
        pizza = Mock()
        self.carte.add_pizza(pizza)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza(self):
        pizza = Mock()
        pizza.name = "Margherita"
        self.carte.add_pizza(pizza)
        self.carte.remove_pizza("Margherita")
        self.assertTrue(self.carte.is_empty())

    
if __name__ == '__main__':
    unittest.main()
