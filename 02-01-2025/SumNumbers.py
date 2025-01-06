'''
1. Create a Rectangle class with attributes length and width. Use the constructor to initialize these attributes.
2. Create a class SumNumbers that contains two attributes num1 and num2, and a method sum() that returns the sum of these two numbers.
3. Create a class Calculator with methods add(), subtract(), multiply(), and divide() to perform basic arithmetic operations.

'''

class SumNumbers:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2
    
num1 = 5
num2 = 6
sum = SumNumbers(num1,num2)
print(f"Addition of {sum.num1} and {sum.num2} is {sum.sum(num1,num2)}")




        




        