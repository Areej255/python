import math

class Calculator:
    #constructor
    def __init__(self):
        pass
        
    def sum(self,num1,num2):
        return num1 + num2
          
    def subtract(self,num1,num2):
        return num1 - num2
       
    def multiply(self,num1,num2):
        return num1 * num2
        
    def divide(self,num1,num2):
        try:
            return num1 / num2    
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
    
    def remainder(self,num1,num2):  
        return num1 % num2
    
    def power(self,num1,num2):
        return math.pow(num1,num2)
    
    def gcd(self,num1,num2):
        return math.gcd(int(num1),int(num2))
    
    def sin(self,num):
        return math.sin(num)
    
    def cos(self,num):
        return math.cos(num)

    def tan(self,num):
        return math.tan(num)

    def exponential(self,num):
        return math.exp(num)
    
    def factorial(self,num):
        return math.factorial(int(num))
    
    def log10(self,num):
        return math.log10(num)

    def log2(self,num):
        return math.log2(num)

    def square_root(self,num):
        return math.sqrt(num)    
    print("""\nSelect an Operation:
              1.Addition
              2.Subtraction
              3.Multiplication
              4.Division
              5.Remainder
              6.Power
              7.GCD
              8.Sin
              9.Cos
              10.tan
              11.Exponential
              12.Factorial
              13.Log10
              14.log2
              15.SquareRoot
              16.Exit 
              """)  
def main():
    while True:
        
        
        user_input = input("Enter Your Choice(1/2/3/4/5//6//7/8/9/10/11/12/13/14/15/16):")
        if user_input in ("1","2","3","4","5","6","7"):
            try:
                num1 = float(input("Enter First Number:"))
                num2 = float(input("Enter Second Number:"))
            except ValueError:
                print("Invalid Input: Please Enter Numbers Only.")
                continue
            calculator = Calculator()

            if user_input == "1":
                result = calculator.sum(num1,num2)
            elif user_input == "2":
                result = calculator.subtract(num1,num2)
            elif user_input == "3":
                result = calculator.multiply(num1,num2)
            elif user_input == "4":
                result = calculator.divide(num1,num2)
            elif user_input == "5":
                result = calculator.remainder(num1,num2)
            elif user_input == "6":
                result = calculator.power(num1,num2)
            elif user_input == "7":
                result = calculator.gcd(num1,num2)
            if result is not None:
                print(f"Result: {result}")
        
        elif user_input in ("8","9","10","11","12","13","14","15"):
            try:
                num = float(input("Enter Number:"))
            except ValueError:
                print("Invalid Input: Please Enter Numbers Only.")
                continue
            calculator = Calculator()
            
            if user_input == "8":
                result = calculator.sin(num)
            elif user_input == "9":
                result = calculator.cos(num)
            elif user_input == "10":
                result = calculator.tan(num)
            elif user_input == "11":
                result = calculator.exponential(num)
            elif user_input == "12":
                result = calculator.factorial(num)
            elif user_input == "13":
                result = calculator.log10(num)
            elif user_input == "14":
                result = calculator.log2(num)
            elif user_input == "15":
                result = calculator.square_root(num)
            
            if result is not None:
                print(f"Result: {result}")

        elif user_input == "16":
            break
        else:
            print("Invalid Input!")

main()
