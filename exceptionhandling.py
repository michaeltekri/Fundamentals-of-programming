try:
    print(number)
except:
    print("An error occurred")
finally:
    print("Bye")


try:
    x = 67
    y = 0
    print(x / y)
except:
    print("ZeroDivision Error occurred")
