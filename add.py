
import math
#Newton-Raphson Method:
def squareroot(a):
   if a < 0 :
    return "enter valid number"
   #intial guess for squareroot
   guess=a/2.0
   tolerance=0.000001

   while abs(guess*guess - a)>tolerance:
       # Update guess using the Newton-Raphson formula
      guess=(guess+a/guess)/2.0
      return guess 

#addition
def add(a,b):
   return (a+b)


#multiply
def multiply(a,b):
   return (a*b)

#divide
def divide(a,b):
   if b==0: return 'division by zero'

   return (a/b)

#substraction
def subs(a,b):
   return (a-b)

def showmenu():
   print ("select:operation")
   print ("1:addition")
   print ("2:multiply")
   print ("3:division")
   print ("4:substraction")
   print("5:Squareroot")
   print ("6:Exit")

def calculator():
   while True:
      #show menu
      showmenu()
      choice =input("Enter choice (1/2/3/4/5/6):")
      if choice =="6":
         print("Exiting calculator...")
         break #exit the loop and end the program
      #get the two number from the user 
      if choice in ["1", "2", "3", "4"]:
       try:
         num1=float(input("Enter first number"))
         num2=float(input("Enter second number"))
       except ValueError:
         print("Invalid input ! Please enter numeric values")
         continue #restart the loop if input is invalid
      
       if choice =="1":
         print(f"The result is:{add(num1,num2)}")
       elif choice =="2":
         print (f"The result is:{multiply(num1,num2)}")
       elif choice =="3":
         print (f"The result is:{divide(num1,num2)}")
       elif choice =="4":
         print(f"the result is:{subs(num1,num2)}")

      elif choice =="5":
       try:
         num= float(input("Enter the number to find the square root:"))
       except ValueError:
         print("invalid input please enter a numeric value")
         continue
       print(f"the square root is {squareroot(num)}")
      else:
         print ("Invalid input! Please select a valid operation")

         #ask the use if they want to perform another calculation
      next_calculation=input("Do you want to another calculation? (yes/no):")
      if next_calculation.lower()!='yes':
            print("Exiting Calculator...")
            break
         
         
         
#run the calculator
calculator()
     


   