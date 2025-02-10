import math

def prime(x):
    if x<2:
        return False
    for n in range(2,int(math.sqrt(x)) +1):
        if x % n==0:
            return False
        return True
    value=int(input())



