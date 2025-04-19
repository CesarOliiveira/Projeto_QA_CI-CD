import unittest
from math_utils import add, subtract

class TestMathUtils(unittest.TextCase):
  def test_add(self):
    self.assertEqual(add(5, 5), 10)
    self.assertEqual(add(-1, 1), 0)

  def test_subtract(self):
    self.assertEqual(subtract(10, 5), 5)
    self.assertEqual(subtract(0, 0), 0)

  def test_multiplication(self):
      self.assertEqual(subtract(10, 2), 20)
      self.assertEqual(subtract(4, 2), 8)

if __name__ == '__main__':
  unittest.main()
