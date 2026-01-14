import random


def Q1():
    print("ENTER YOUR SALARY")
    salary=float(input())
    if(salary<=30000):
        tax=salary*5/100
        salary=salary-tax
        print("SALARY AFTER TAX IS :"+str(salary))   
    elif(salary>30000 and salary <=70000):
        tax=salary*15/100
        salary=salary-tax
        print("SALARY AFTER TAX IS :"+str(salary))
    elif(salary>70000):
        tax=salary*25/100
        salary=salary-tax
        print("SALARY AFTER TAX IS :"+str(salary))
def Q2():
    print("ENTER FIRST NUMBER :")  
    a=int(input())  
    print("ENTER SECOND NUMBER :")
    b=int(input())
    for i in range(a+1,b+1):
        if(i%2==0):
            print(i)
def Q3():
    print("ENTER A NUMBER TO print its digits :")
    num=int(input())
    while(num>0):
        digit=num%10
        print(digit)
        num=num//10
def Q4():
    print("ENTER A NUMBER TO COUNT ITS DIGITS :")
    num=int(input())
    count=0
    while(num>0):
        count=count+1
        num=num//10
    print("NUMBER OF DIGITS IN THE NUMBER IS :"+str(count))
def Q5():
    print("ENTER A NUMBER TO PRINT SUM OF DIGITS :")
    num=int(input())
    sum=0
    while(num>0):
        REM=num%10
        sum=sum+REM
        num=num//10
    print("SUM OF DIGITS IN THE NUMBER IS :"+str(sum))
def Q6():
    for i in range(1,100):
     if(i%3==0 and i%5==0):
      print(i)
def Q7():
 a="n"
 while(1):
  print("ENTER A NUMBER")
  a=input()
  if (a=="quit" or a=="QUIT"):
     break
  num=int(a)
  if(num>=0):
   print("POSITIVE")
  else:
   print("NEGATIVE")
def Q8():
    print("ENTER A NUMBER TO CHECK PRIME OR NOT :")
    num=int(input())
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    if(flag==0):
        print("PRIME")
    else:
        print("NOT PRIME")
def Q9():
    num=random.randint(1,100)
    while(1):
        print("GUESS A NUMBER BETWEEN 1 AND 100")
        guess=int(input())
        if(guess>num):
            print("TOO HIGH")
        elif(guess<num):
            print("TOO LOW")
            

print("ENTER QUESTION NUMBER TO EXECUTE like Q1,Q2,Q3....Q10")

print("Q:1Write a program that takes salary as input and calculates the final salary after tax based on these rules: salary < 30000 → 5% tax, salary between 30000 and 70000 → 15% tax, salary > 70000 → 25% tax.")

print("Q:2Write a function that takes two integers a and b and prints all even numbers between them (inclusive).")

print("Q:3Write a function that prints the digits of a number n. For example, if n = 312, print 3, 1, and 2.")

print("Q:4Write a function that returns the count of digits in a number n.")

print("Q:5Write a function that returns the sum of digits of a number n.")

print("Q:6Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.")

print("Q:7Write a program that continuously takes a number from the user and prints whether it is positive or negative until the user enters 'Quit'.")

print("Q:8Write a program to create a simple calculator that performs addition, subtraction, multiplication, or division based on the operation parameter.")

print("Q:9Write a function is_prime(n) that returns True if n is a prime number and False otherwise using a loop.")

print("Q:10Write a number guessing game where the user guesses a secret number and the program prints 'Too high', 'Too low', or 'Correct!' based on the guess.")

match input():
    
    case 'Q1':
        Q1()
    case 'Q2':
        Q2()
    case 'Q3':
        Q3()
    case 'Q4':
        Q4()
    case 'Q5':
        Q5()
    case 'Q6':
        Q6()
    case 'Q7':
        Q7()
    case 'Q8':
        Q8()
    case 'Q9':
        Q9()