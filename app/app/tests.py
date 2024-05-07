"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """
    Test the calc module.
    """

    def test_add_numbers(self):
        res = calc.add(1, 3)

        self.assertEqual(res, 4)

    def test_sub_numbers(self):
        res = calc.sub(3, 1)

        self.assertEqual(res, 2)
    
