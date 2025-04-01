#construct linear algebra library
import numpy as np

#scalar class
class scalar:
    def __init__(self,value):
        self.value=value
    
    def add(self,value_1):
        addition=scalar(self.value+value_1.value)
        return addition
    
    def subtract(self,value_1):
        subtraction=scalar(self.value-value_1.value)
        return subtraction

    def multiply(self,value_1):
        multiply=scalar(self.value*value_1.value)
        return multiply
    
    def power(self,exponent):
        power= scalar(self.value**exponent.value)
        return power
    
    def exponent(self):
        exponent=scalar(np.exp(self.value))
        return exponent
    
    def size(self):
        size=abs(self.value)
        return size
    
    def __str__(self): #returns value of scalar directly
        return str(self.value)
#examples:

a=scalar(2)
b=scalar(3)
print("Addition of two numbers:",a.add(b))
print("Power of a number:",b.power(a))
    

# #vector functions
class vector:
    def __init__(self,value):
        self.value=np.array(value)


# #add
    def add(self,value_1):
        if len(self.value)==len(value_1.value):
            sum=vector(self.value+value_1.value)
            return sum
        else:
            print("vectors must be of same dimension")
            return None
# #cosine
    def cosine(self):
        cos=vector(np.cos(self.value))
        return cos

# #sine
    def sine(self):
        sine=vector(np.sin(self.value))
        return sine

# #dot
    def dot(self,value_1):
        if len(self.value)==len(value_1.value):
            dot_product=np.dot(self.value,value_1.value)
            return (dot_product)
        else:
            print("should be in same dimension")

# #cross
    def cross(self,value_1):
        if len(self.value)==3 and len(value_1.value)==3:
            cross_product=np.cross(self.value,value_1.value)
            return vector(cross_product)
        else:
            print("only for 3D vectors")
            return None

# #size
    def size(self):
        size=np.sqrt(np.sum(self.value**2))
        return size
    
    def __str__(self):
        return str(self.value)
        
#example:
v1=vector([1,2,3])
v2=vector([3,4,5])
print("magnitude",v1.size())
print("dot product", v1.dot(v2))
# #matrix functions

class matrix:
    def __init__(self,value):
        self.value=np.array(value)


# #add
    def add(self,matrix_1):
        if self.value.shape==matrix_1.value.shape:
            result=matrix(self.value+matrix_1.value)
            return result
        else:
            print("should be same dimensions")
            return None
        
    # #sub
    def sub(self,matrix_1):
        if self.value.shape==matrix_1.value.shape:
            result=matrix(self.value-matrix_1.value)
            return result
        else:
            print("should be same dimensions")
            return None

    # #multiply
    def mult(self,matrix_1):
        if self.value.shape==matrix_1.value.shape:
            result=matrix(self.value*matrix_1.value)
            return result
        else:
            print("should be same dimensions")
            return None
        
    # #size
    def size(self):
        return self.value.shape


    # #advanced functions
    # #trace of a matrix
    def trace(self):
        if self.value.shape[0]==self.value.shape[1]:
            return np.trace(self.value)
        else:
            print("matric not square")
            return None
        
    # #transpose of a matrix
    def transpose(self):
        return matrix(self.value.T)

    # #svd of a matrix
    def svd(self):#A^t*A
        ATA=np.dot(self.value.T,self.value)
        

        eigenvalues,eigenvectors=self._eigen_decomposition(ATA)
        
        singular_values=np.sqrt(eigenvalues)
        #normalise
        left=np.dot(self.value,eigenvectors)
        for i in range(left.shape[1]):
            left[:,i]=left[:,i]/singular_values[i]
        return left, singular_values, eigenvectors

    def eigen_decomposition(self,matrix):
        eigval=np.zeros(matrix.shape[0])
        eigvec=np.zeros((matrix.shape[0],matrix.shape[0]))

        for i in range(matrix.shape[0]):
            eigvecs=np.random.rand(matrix.shape[0])


    def __str__(self):
        return str(self.value)
#example:
m1=matrix([[1,2],[3,4]])
m2=matrix([[5,6],[7,8]])
print("matrix 1:", m1)
print("matrix 2:", m2)
print("matrix 1 size:", m1.size())
m3=m1.transpose()
print("matrix transpose",m3)
