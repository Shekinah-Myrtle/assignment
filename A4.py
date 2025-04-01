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
    
#examples:

a=scalar(2)
b=scalar(3)
print("Addition of two numbers:",a.add(b).value)
print("Power of a number:",b.power(a).value)
    

# #vector functions
# class vector():

# #add
# #cosine
# #sine
# #dot
# #cross
# #size
# #matrix functions
# class matrix():

# #add
# #sub
# #mult
# #size

# #advanced functions
# #trace of a matrix
# #transpose of a matrix
# #svd of a matrix