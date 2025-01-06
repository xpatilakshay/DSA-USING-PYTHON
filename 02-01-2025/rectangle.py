'''
1. Create a Rectangle class with attributes length and width. Use the constructor to initialize these attributes.
2. Create a class SumNumbers that contains two attributes num1 and num2, and a method sum() that returns the sum of these two numbers.
3. Create a class Calculator with methods add(), subtract(), multiply(), and divide() to perform basic arithmetic operations.

'''

class Rectangle:
    def __init__(self,lenght,width):
        self.length = lenght
        self.width = width

r1 = Rectangle(20,30)
print(f"lenght of Rectangle is : {r1.length}\nWidth of Rectangle is : {r1.width}")