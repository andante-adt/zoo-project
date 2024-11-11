import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_childleft_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_childright_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teenageleft_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_teenageright_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adultleft_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_adultleft_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")

if __name__ == '__main__':
    unittest.main()
