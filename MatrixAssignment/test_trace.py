import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix1=Matrix([[9,8],[4,5]])
        matrix3=Matrix([[2,3,5],[4,5,6]])
        self.assertEqual(matrix1.trace(),26 )
        self.assertEqual(matrix3.trace(),25)


if __name__ == '__main__':
    unittest.main()