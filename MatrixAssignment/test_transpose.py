import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix2 = Matrix([[36, 32], [16, 20]])
        matrix3 = Matrix([[2, 3, 5], [4, 5, 6]])
        self.assertEqual(matrix2.transpose(),[[36, 16], [32, 20]] )
        self.assertEqual(matrix3.transpose(),[[2, 4], [3, 5], [5, 6]])


if __name__ == '__main__':
    unittest.main()