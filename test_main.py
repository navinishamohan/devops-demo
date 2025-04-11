import unittest
from main import Calculator
class TestCalc(unittest.TestCase):
    def test_add(self):
        calc=Calculator()
        self.assertEqual(calc.add(2,3),5)

if __name__=='__main__':
    unittest.main()