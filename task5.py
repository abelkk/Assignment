student = {
    "name" :"abel",
    "age": 20,
    "marks": 76
     
}
student["marks"] = 90 
student["grade"] = "A"

for key, value in student.items():
    print(key,":",value)