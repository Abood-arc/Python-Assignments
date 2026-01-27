

    
print("This is Assignment 4")
print("PRESS 1 FOR QUESTION 1 Create a program that: Opens a file names.txt in write mode Writes 5 names (one per line) entered by the user Then opens the same file in read mode and prints all names")
print("Press 2 for question 2 Create a program that: Opens a file log.txt in append modeAdds a new log entry (e.g., Program run successfully Opens the file in read mode and prints all logs")
print("Press 3 Create a program that:Has a list of numbers:[5, 10, 15, 20, 25] Uses a list comprehension to create a new list with only numbers greater than 15Prints the new list for question 3")
print("Press 4 for question 4 Create a Python dictionary of 3 cities and their populations. Save it to cities.json.\nLoad the JSON file and print each city with its population\nAsk the user for a new city and its population\nUpdate this information in the JSON file")
print("Press 5 for question 5 Write a program that tries to open data.txt in read mode.If the file does not exist, catch the exception and print:File not found!")
choice=int(input("ENTER YOUR CHOICE "))
match(choice):
    case 1:
        f=open("names.txt","w")
        f.writelines(["Abood\n","khaled\n","sabhee\n","omar\n","ahmed\n"])
        f.close()
        f=open("names.txt","r")
        names=f.readlines()
        for name in names:
            print(name)
        f.close()
    case 2:
        with open("log.txt","a") as f:
            f.write("program runs successfully")
        with open("log.txt","r") as f:
            logs=f.readlines()
            for log in logs:
                print(log)
            f.close()
    case 3:
        list1=[5,10,15,20,25,30,35,40]
        list2=[num for num in list1 if num >15]
        print(list2)
    case 4:
     import json
     dict={"Lahore":"13 million","karachi":"18 million","Islamabad":"1 million"}
     with open("cities.json","w") as f:
      json.dump(dict,f)
     with open("cities.json","r") as f:
      dic2=json.load(f)
      for city,population in dic2.items():
       print(f"{city}:{population}")
      city=input("enter new city")
      pop=input("enter population")
      dic2[city]=pop
      with open("cities.json","w") as f:
       json.dump(dic2,f)
       print("City information updated successfully.")
    case 5:
        try:
            f=open("data.txt","r")
        except FileNotFoundError:
            print("File not found!")              
              
           
      