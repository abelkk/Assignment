name =input("what is your name?  ")
age = int(input("How old are you? "))
if (age >= 18):
    print(f"{name} you are an adult")
else:
    print(f"{name}you are a minor")

grade = int(input("what mark did you score? "))
if (grade >= 90):
    print("you had an A") 
elif(grade>=75):
    print("you scored a B")
elif(grade>=50):
    print("you had a C")
else:
    print("you failed!")