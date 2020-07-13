import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        print("error! Vectors must have same length")
            
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
        
    return result

def get_row(matrix, row):
    """
        Get full row from a matrix
    """
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Get full column from a matrix
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        determinant = 0
        
        if self.h == 1:
            determinant = self.g[0]
            
            return determinant
        
        if self.h == 2:
            determinant = (self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0])
            
            return determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            trace += self.g[i][i]
            
        return trace
        
        
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        determinant = self.determinant()
        inverse = zeroes(self.h,self.w)
        
        if self.h == 1:
            inverse[0][0] = 1 / self.g[0][0]
            
            return inverse
        
        if self.h == 2 & self.w == 2:
            inverse[0][0] = self.g[1][1] * (1/determinant)
            inverse[0][1] = -self.g[0][1] * (1/determinant)
            inverse[1][0] = -self.g[1][0] * (1/determinant)
            inverse[1][1] = self.g[0][0] * (1/determinant)
            
            return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        Transpose = zeroes(self.w,self.h)
        for i in range(self.h):
            for j in range(self.w):
                Transpose[j][i] = self.g[i][j]
                
        return Transpose
                
            

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        resultadd = []
        for i in range(self.h):
            row =[]
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            resultadd.append(row)
        
        return Matrix(resultadd)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        resultneg = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] * -1)
            resultneg.append(row)
        
        return Matrix(resultneg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        resultsub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            resultsub.append(row)
        
        return Matrix(resultsub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        m_rows = self.h
        p_columns = other.w
        
        # empty list that will hold the product of AxB
        resultmul = []
                    
        for i in range(m_rows):
            row_result = []
            for j in range(p_columns):
                row_result.append(dot_product(get_row(self.g,i),get_column(other.g,j)))
            resultmul.append(row_result)
            
        return Matrix(resultmul)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            resultrmul = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.g[i][j] * other)
                resultrmul.append(row)
        
            return Matrix(resultrmul)