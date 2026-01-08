print("My first package!")
def Q1():
    print ("Enter your name")
    name =input()
    print("ENTER YOUR AGE")
    age=input()
    print("hello "+name +" your age is "+age)
def Q2():
    print("ENTER FIRST NUMBER ")
    num1=int(input())
    print("ENTER SECOND NUMBER")
    num2=int(input())
    print("SUM: "+str(num1+num2) )
    print("DIFFERENCE: "+str(num1-num2) )
    print("PRODUCT: "+str(num1*num2) )
    print("QUOTIENT: "+str(num1/num2) )

def Q3():
    print("ENTER TWO INTEGERS AND ONE FLOAT")
    int1=int(input())
    int2=int(input())
    flt3=float(input())
    flt1=float(int1)
    flt2=float(int2)
    avg=(flt1+flt2+flt3/3)
    print("THE AVERAGE IS :"+avg)
def Q4():
    print("ENTER A NUMBER ")
    num=(input())
    print(type(num))
    num=int(num)
    print(type(num))
    num=float(num)
    print(type(num))
    num=str(num)
    print(type(num))
def Q5():
    x=10+3*2**2
    print(x+" dfkjd")
def Q6():
    print("ENTER FIRST NUMBER ")
    num1=input()
    print("ENTER SECOND NUMBER")
    num2=input()
    num3=num1
    num1=num2
    num2=num3
    print("FIRST NUMBER IS :"+num1)
    print("SECOND NUMBER IS :"+num2)    
def Q7():
    print("ENTER A TEMPERATURE IN CELCIUS ")
    celsius=float(input())
    fahrenheit=(celsius*9/5)+32
    print("TEMPERATURE IN FAHRENHEIT IS :"+str(fahrenheit))
    
def Q8():
    print("ENTER RADIUS")
    x=float(input())
    area=3.14*x**x
    print ("area is :"+str(area))
    
    
def Q9():
    print("ENTER PRINCIPLE ,RATE AND TIME")
    p=float(input())
    r=float(input())
    t=float(input())
    si=(p*r*t)/100
    print("SIMPLE INTEREST IS :"+str(si))
def Q10():
    print("ENTER A DECIMAL NUMNER")
    num=float(input())
    num1=int(num)
    num2=num-num1
    print("INTEGER PART IS :"+str(num1))
    print("FRACTIONAL PART IS :"+str(num2))
    
    
print("ENTER QUESTION NUMBER TO EXECUTE")

QUESTIONS=input()
match QUESTIONS:
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
    case 'Q10':
        Q10()
    
    