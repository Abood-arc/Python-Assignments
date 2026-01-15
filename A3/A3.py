def Q1():
    print("ENTER A STRING TO CHECK FOR PALLINDROME")
    s=input()
    rev=s[::-1]
    if(s==rev):
        print("PALLINDROME")
def Q2():
    li=[1,2,3,4,5,6]
    sum=0
    count=0
    for i in li:
     sum+=i
     count+=1
    print(f"the avg of list is {sum/count}")
def Q3():
    lst1=[]
    lst2=[]
    print("ENTER VALUES OF FIRST LIST ")
    n=int(input("How many elements"))
    for i in range(1,n):
     value=int(input("ENTER ELEMENTS "))
     lst1.append(value)
    print("ENTER VALUES OF 2nd LIST ")
    n=int(input("How many elements "))
    for i in range(1,n):
     value=int(input("ENTER ELEMENTS"))
     lst2.append(value)
     
    lst3=lst1+lst2
    print(f"LIST 3: {lst3[0:]}")
    lst3.sort()
    print(f"LIST 3: {lst3[0:]}")
    
def Q4():
    tup=(1,2,3,4,5,6)
    tup1=()
    tup2=()
    for val in tup:
     if (val%2==0):
      tup1=tup1+(val,)
    else :
     tup2=tup2+(val,)
    print(tup1)
    print(tup2)
def Q5():
    choice="none"
    dic={}
    while True :
     print ("PRESS A TO ADD A STUDENT")
     print ("PRESS B TO UPDATE MARKS")
     print ("PRESS C TO SEARCH FOR STUDENT")
     print ("PRESS D TO DISPLAY ALL STUDENTS")
     print ("PRESS E TO EXIT")
     choice=(input())
     if (choice=="A"):
      print("ENTER STUDENT NAME")
      key=input()
      print("ENTER STUDENT MARKS")
      marks=int(input())
      dic[key]=marks
      
     elif (choice=="B"):
          key=input("enter student name to update his/her marks")
          value=input("enter marks")
          dic[key]=value
     elif (choice=="C"):
                key=input("enter student name ")
                print(dic.get(key))
    
     elif (choice=="D"):
          print(dic.items())
     else:
         break
    
def Q6():
    lst=["apple","banana","kiwi","cherry","sabhee"]
    count=0
    dic={}
    for ch in lst:
     string=ch
     length=int(len(string))
     new_item=[(string,length)]
     dic.update(new_item)
    print(dic.items())
    
def Q7():
    print("ENTER A STRING")
    a=input()
    count=0
    for ch in a :
     if(ch==" "):
       count+=1
    print(f"Number of spaces :{count}") 
       
def Q8():

    li1=[]
    n=int(input("ENTER LENGTH OF  1st LIST : "))
    for i in range (0,n):
     val=int(input("ENTER DIGITS"))
     li1.append(val)
    li2=[]
    n=int(input("ENTER LENGTH OF 2ND LIST : "))
    for i in range (0,n):
     val=int(input("ENTER DIGITS"))
     li2.append(val)
    count=0
    print(li1[:])
    print(li2[:])
    st1=set(li1)
    st2=set(li2)
    li3=list(st1.intersection(st2))
    for i in li3:
       count+=1
       print("COMMON ELEMENTS ARE",i)
    if (count==0):
     print("No common elements")

def Q9():
 li=[1,2,2,3,2,4,5,4]
 st=set()
 dublicate=set()
 for i in li:
    if i in st:
        dublicate.add(i)
    else:
     st.add(i)
 print("unique set:",st)
 print("duplicate set:",dublicate)

def Q10():
 print("ENTER A STRING")
 a=input()
 count=0
 for ch in a :
  if(ch==" "):
     count+=1
 print(f"Number of spaces :{count}")

def show_menu():
    print("\n" + "="*50)
    print("PYTHON FUNDAMENTALS - ASSIGNMENT 3")
    print("="*50)
    print("Choose a question to run:")
    print(" 1. Check if a word is a palindrome")
    print(" 2. Calculate average of numbers")
    print(" 3. Merge and sort two lists")
    print(" 4. Separate even and odd numbers")
    print(" 5. Student marks manager")
    print(" 6. Find length of words")
    print(" 7. Count spaces in text")
    print(" 8. Check common elements in lists")
    print(" 9. Find duplicate numbers")
    print("10. Find unique characters")
    print(" 0. Exit program")
    print("="*50)

# Main program
def main():
    print("Welcome to Python Assignment 3!")
    print("This program has solutions to all 10 questions.")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (0-10): ")
        
        if choice == "0":
            print("\nThank you for using the program! Goodbye!")
            break
            
        elif choice == "1":
            Q1()
        elif choice == "2":
            Q2()
        elif choice == "3":
            Q3()
        elif choice == "4":
            Q4()
        elif choice == "5":
            Q5()
        elif choice == "6":
            Q6()
        elif choice == "7":
            Q7()
        elif choice == "8":
            Q8()
        elif choice == "9":
            Q9()
        elif choice == "10":
            Q10()
        else:
            print("Invalid choice! Please enter a number between 0 and 10")
        
        # Pause before showing menu again
        if choice != "0":
            input("\nPress Enter to continue...")
