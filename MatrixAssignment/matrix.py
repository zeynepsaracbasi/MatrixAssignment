from copy import deepcopy
import math
class Matrix:

    def __init__(self,matrix):
        self.set_matrix(matrix)

    def get_matrix(self):
        return self.matrix

    def set_matrix(self,matrix):
        self.matrix=matrix
        return

    def scaler_multiplication(self, value):
        rows, columns = len(self.matrix), len(self.matrix[0])
        matrix = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                matrix[i][j] = (self.matrix[i][j] * value)
        return matrix

    def trace(self):
        rows, columns = len(self.matrix), len(self.matrix[0])
        sum=0
        for i in range(rows):
            for j in range(columns):
                sum = sum+(self.matrix[i][j])
        return sum

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed_matrix


    def matrix_multiplication(self, matrix2):
        if len(self.matrix[0])==len(matrix2.matrix):
            rows, columns = len(self.matrix), len(matrix2.matrix[0])
            matrix = [[0] * columns for _ in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    matrix[i][j] = sum(matrix1.matrix[i][k] * matrix2.matrix[k][j] for k in range(len(matrix2.matrix)))
            return matrix
        else:
            return ("Column number of First Matrix must be equal to row number of Second Matrix")


    def matrix_determinant(self,total=0):
        try:
            rows = list(range(len(self.matrix)))
            if len((self.matrix)) == 2 and len((self.matrix[0])) == 2:
                val = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
                return val
            # define submatrix for focus column and
            for column in rows:  # for each  column,find the submatrix
                Acopy = deepcopy(self.matrix)
                Acopy = Acopy[1:]
                copyrows = len(Acopy)
                for i in range(copyrows):
                    # for each remaining row of submatrix ,remove the j column elements
                    Acopy[i] = Acopy[i][0:column] + Acopy[i][column + 1:]
                Acopy = Matrix(Acopy)
                sign = math.pow(-1, (1 + column + 1))  # F)
                det_A1j = Acopy.matrix_determinant()
                total += sign * self.matrix[0][column] * det_A1j
            return total
        except :
            return ("Dimensions must be NxN to find determinant of matrix!")


    def matrix_inverse(self):
        try:
            determinant = self.matrix_determinant()
            if len(self.matrix) == 2:
                return [[self.matrix[1][1] / determinant, -1 * self.matrix[0][1] / determinant],
                        [-1 * self.matrix[1][0] / determinant, self.matrix[0][0] / determinant]]
            # find matrix of cofactors
            cfactors = []
            for r in range(len(self.matrix)):
                Row = []
                for c in range(len(self.matrix)):
                    minor = [row[:c] + row[c + 1:] for row in (self.matrix[:r] + self.matrix[r + 1:])]
                    minor = Matrix(minor)
                    Row.append(((-1) ** (r + c)) * minor.matrix_determinant())
                cfactors.append(Row)
            cfactors = Matrix(cfactors)
            cfactors = cfactors.transpose()
            for row in range(len(cfactors)):
                for column in range(len(cfactors)):
                    cfactors[row][column] = cfactors[row][column] / determinant
            return cfactors
        except:
            return ("Matrix dimension must be NxN for inversion!")



