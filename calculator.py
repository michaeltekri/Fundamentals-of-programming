a=float(input("Enter a value for a:"))
b=float(input("Enter a value for b:"))

def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)



print("Select operator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice=input("Enter choice (1/2/3/4):")
    if choice=='1':
        print(add(a,b))
    if choice=='2':
        print(subtract(a,b))
    if choice=='3':
        print(multiply(a,b))
    if choice=='4':
        print(divide(a,b))
