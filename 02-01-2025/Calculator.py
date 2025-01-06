'''
1. Create a Rectangle class with attributes length and width. Use the constructor to initialize these attributes.
2. Create a class SumNumbers that contains two attributes num1 and num2, and a method sum() that returns the sum of these two numbers.
3. Create a class Calculator with methods add(), subtract(), multiply(), and divide() to perform basic arithmetic operations.

'''

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
 
    def add(self):
        return self.num1 + self.num2
        
    def subtract(self):
        return self.num1 - self.num2
        
    def multiply(self):
        return self.num1 * self.num2
        
    def divide(self):
        return self.num1 / self.num2
    

num1 = 9
num2 = 2

calculator = Calculator(num1,num2)
add = calculator.add()
print(add)

sub = calculator.subtract()
print(sub)

mul = calculator.multiply()
print(mul)

div = calculator.divide()
print(div)