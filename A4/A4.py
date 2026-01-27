class BankAccount :
    def __init__(self,name,balance,number):
     self.name=name
     self.number=number
     self.balance = balance
    def Deposit(self,amount):
     self.balance+=amount
     print("AMOUNT DEPOSIT SUCCESSFULLY.YOUR CURRUNT BALANCE IS :",self.balance)
    def Withdrawl(self,amount):
     self.balance-=amount
     print("AMOUNT withdraws SUCCESSFULLY.YOUR CURRUNT BALANCE IS :",self.balance)
    def CheckBalance(self):
     print(f"BALANCE : {self.balance}")

class book :
    reviews=[]
    author="Robert T. Kiyosaki"
    title="RICH DAD Poor Dad"
    def __init__(self,name):
     self.name=name
    def add_review(self,review):
     self.review=review
     book.reviews.append(self.review)
    @classmethod
    def count_review(cls):
     print("TOTAL REVIEWS :",len(cls.reviews))
    @classmethod
    def display(cls):
     for val in cls.reviews:
      print(val)    
class Student:
 def __init__(self,name,rollno,marks):
  self.set_name(name)
  self.set_rollno(rollno)
  self.set_marks(marks)
 def set_name(self,name):
  if name.isalpha():
   self.__name=name
  else :
      print("enter your name correctly")
 def set_rollno(self,rollno):
  if(rollno>1 and rollno<100):
    self.__rollno=rollno
  else:
    print("enter your rollno correctly")
 def set_marks(self,marks):
  if(marks<=0):
   print("INVALID")
  else:
     self.__marks=marks
 def get_name(self):
    return self.__name
 def get_rollno(self):
    return self.__rollno
 def get_marks(self):
    return self.__marks
 def display(self):
  print("Name",self.get_name())
  print("rollno",self.get_rollno())
  print("marks",self.get_marks())

class Shape:
 def area(self):
   print("override")
 
class Circle(Shape):
 def area(self):
  print("Boleto circle")
class Rectangle(Shape):
 def area(self):
    print("Boleto Rectangle")

class Triangle(Shape):
 def area(self):
       print("Boleto Triangle")

def shape(entity):
 entity.area()
class Vehicle:
   
 def __init__(self,brand,model):
   self.brand=brand
   self.model=model
 def display(self):
  print("Parent class")
class car(Vehicle):
    def __init__(self,seats,cc,brand,model):
     super().__init__(brand,model)
     self.cc=cc
     self.seats=seats
    def display(self):
     print(f"Brand:{self.brand} MODEL:{self.model} ENGINE:{self.cc}NOOFSEATS{self.seats}")
class bike(Vehicle):
    def __init__(self,brand,model,cc):
     super().__init__(brand,model)
     self.cc=cc
    def display(self):
     print(self.brand,self.model,self.cc)

from abc import ABC, abstractmethod

class Employee:
    def __init__(self,name):
     self.name=name
    @abstractmethod
    def salary():
     pass
 
class intern(Employee):
    def __init__ (self,name,noofdays,fulltime):
        super().__init__(name)
        self.noofdays=noofdays
        self.fulltime=fulltime
      
    def salary(self):
        if(self.fulltime==True):
            print(f"{self.name}! YOUR SALARY IS {self.noofdays*20} USD")
        else:
            print(f"{self.name}! YOUR SALARY IS {self.noofdays*10} USD")

class pmntjob(Employee):
    def __init__ (self,name,noofdays):
        super().__init__(name)
        self.noofdays=noofdays
    def salary(self):
        print(f"{self.name}! YOUR SALARY IS {self.noofdays*30} USD")
class cntjob(Employee):
    def __init__ (self,name,contract):
          super().__init__(name)
          self.contract=contract
    def salary(self):
          print(f"{self.name}! YOUR CONTRACT  IS of {self.contract} WITH PAYMENT OF {self.contract*200} USD")  

class person :
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
     print(self.name)

     if self.age is not None:
        print(self.age)

     if self.address is not None:
        print(self.address)

class Player:
    player_count=0
    def __init__(cls,self,name,level):
     self.name=name
     self.level=level
     cls.player_count+=1
    @classmethod
    def display(cls):
     print(f"{cls.player_count} players were created")




 
class herbivore:
    def __init__(self,herbi_species):
     self.herbi_species=herbi_species
    def herbi(self):
      print("i am a herbivore class")
        
    
class carnivore:
    def __init__(self,carni_species):
      self.carni_species=carni_species
    def carni(self):
      print("i am a carnivore class")
     
    
class omnivore:
    def __init__(self,omni_species):
       self.omni_species=omni_species
    def omni(self):
     print("i am a omnivore class")
    

class bear(herbivore,carnivore,omnivore):
   def __init__(self,name,place,herbi_species,carni_species,omni_species):
      self.name=name
      self.place=place
      herbivore.__init__(self,herbi_species)
      carnivore.__init__(self,carni_species)
      omnivore.__init__(self ,omni_species)

#question 1
p1=BankAccount("Abood",1234,1000)
print(p1.name,p1.number,p1.balance)
p1.Deposit(1000)
p1.Withdrawl(1000)
p1.CheckBalance()
print("PRESS 1 FOR DEPOSIT ")
print("PRESS 2 FOR withdraw")
print("PRESS 3 FOR BALANCE ")
print("PRESS 4 TO EXIT ")
while True:
     flag=int(input("ENTER YOUR CHOICE"))
     if(flag==1):
      amount=int(input("ENTER AMOUNT "))
      p1.Deposit(amount)
     elif(flag==2):
      amount=int(input("ENTER AMOUNT "))
      p1.Withdrawl(amount)
     elif(flag==3):
      p1.CheckBalance()
     else :
      break
#question 2
s1=book("abood")
s2=book("maaz")
s3=book("mohd")
s1.add_review("absolutely love it")
s1.add_review("changed my life")
s1.add_review("Higly recommended")
book.count_review()
book.display()
#question 3
s1=Student("Abood",27,68)
s2=Student("sabhee",47,55)
s3=Student("maaz",87,70)
s1.display()
s2.display()
s3.display()
#question 4
s=Shape()
c=Circle()
r=Rectangle()
t=Triangle()

for val in [s,c,r,t]:
 shape(val)
 
 #question 5
c=car(5,"600cc","corolla",'gli')
b=bike("kawasaki","ninja2301","450cc")
c.display()
b.display()
 
 #question 6
e1=intern("sabhee",20,False)
e2=pmntjob("sabhee",20)
e3=cntjob("sabhee",20)
e1.salary()
e2.salary()
e3.salary()



#Queston 7    
p1=person("abood")
p2=person("abood",22)
p3=person("abood",22,"Muttrah")
p1.display()  
p2.display()  
p3.display()  

#question 8
     
p1=Player("Abood",1)
p2=Player("Abood",2)
p3=Player("Abood",3)
p4=Player("Abood",4)
p5=Player("Abood",5)
Player.display()

#question 9
class herbivore:
    def __init__(self,herbi_species):
     self.herbi_species=herbi_species
    def herbi(self):
      print("i am a herbivore class")
        
    
class carnivore:
    def __init__(self,carni_species):
      self.carni_species=carni_species
    def carni(self):
      print("i am a carnivore class")
        
    
class omnivore:
    def __init__(self,omni_species):
       self.omni_species=omni_species
    def omni(self):
     print("i am a omnivore class")
    

class bear(herbivore,carnivore,omnivore):
   def __init__(self,name,place,herbi_species,carni_species,omni_species):
      self.name=name
      self.place=place
      herbivore.__init__(self,herbi_species)
      carnivore.__init__(self,carni_species)
      omnivore.__init__(self ,omni_species)
      
b1=bear("grizzly bear","deosai national park","63%","32%","9%")
b1.herbi()
b1.carni()
b1.omni()




