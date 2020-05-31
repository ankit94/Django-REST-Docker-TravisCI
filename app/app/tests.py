from django.test import TestCase
from app.app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test to add two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test to subtract two numbers"""
        self.assertEqual(subtract(8, 3), 5)
