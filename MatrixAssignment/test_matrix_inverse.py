import unittest
from matrix import Matrix

class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix1=Matrix([[9,8],[4,5]])
        matrix2=Matrix([[1,4,4],[2,3,5],[4,5,6]])
        matrix3=Matrix([[2,3,5],[4,5,6]])
        self.assertEqual(matrix1.matrix_inverse(),[[0.38461538461538464, -0.6153846153846154], [-0.3076923076923077, 0.6923076923076923]])
        self.assertEqual(matrix2.matrix_inverse(),[[-0.4117647058823529, -0.23529411764705882, 0.47058823529411764], [0.47058823529411764, -0.5882352941176471, 0.17647058823529413], [-0.11764705882352941, 0.6470588235294118, -0.29411764705882354]])
        self.assertRaises(Exception,matrix3.matrix_inverse())

if __name__ == '__main__':
    unittest.main()
