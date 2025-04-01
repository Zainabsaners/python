def add(a,b):
    return a+b
def subtract(a,b):
     return a-b
def multiply(a,b):
     return a*b
def divide(a,b):
     if(b==0):
          return"Error:division by zero"
     return a/b
def exponential(a,b):
     return a**b
def calc():
     while True:
          print("calculator is running...")
          
          print("select operation:")
          print("1.add")
          print("2.subtract")
          print("3.multiply")
          print("4.divide")
          print("5.exponential")
          print("6.Exit")
          choice = input("Enter choice (1/2/3/4/5/6):")
          print(f"you selected option {choice}")
          if choice=='6':
               print("Exiting calculator")
               break
          if choice in ('1','2','3','4','5'):
               try:
                    num1=float(input("Enter first number:"))
                    num2=float(input("Enter second number:"))
               except ValueError:
                    print("invalid input! please enter numbers only" )
          if choice=='1':
               print(f"Result is :{add(num1,num2)}")
          elif choice=='2':
               print(f"Result:{subtract(num1,num2)}")
          elif choice=='3':
               print(f"Result:{multiply(num1,num2)}")
          elif choice=='4':
                print(f"Result:{divide(num1,num2)}")
          elif choice=='5':
               print(f"Result:{exponential(num1,num2)}")
          else:
               print("invalid choice! please select a valid option.")
          
               
               
               
              
              
               
                 