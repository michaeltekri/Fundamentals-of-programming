#Built-in functions/Standard Library functions

y=max(67,43,89,90,23)
print("The maximum value is",y)

x=min(15,3,20,78)
print("The minimum value is",x)

#User defined functions
def name():
    print("Michael")
name() #Calling a function

def multiply():
    x=10
    y=2
    print(x*y)
multiply()


#Parameter/Variable and Argument/Value
def add(a,b):
    print(a+b)
add(3,6)
add(9,6)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)
employee("Mark","Male","CEO",560000,67)
employee("John","Male","Managing director",200000,67)

#A program that displays details of five students
#Use a user designed function with the parameter and argument
#Fullname,age,course,gender
def student(fullname,age,course,gender):
    print(fullname,age,course,gender)
student("Miles Njoroge",22,"MIT","Male")
student("Wilson Matheu",19,"Android","Male")
student("Emily Wasiu",20,"Cybersecurity","Female")
student("Kiki Thon",17,"Datascience","Female")
student("Mark Macharia",26,"Web development","Male")
