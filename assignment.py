#A program to check whether a year is a leap year or not
from email.charset import add_alias
from operator import countOf

first=2016
second=2026
number=second
if number%4==0:
    print("Leap year is",number)
else:
    print("Normal year is",number)


#A program to check whether a letter is a consonant or a vowel
letter="a"
letter=letter.lower()
if letter in ["a","e","o","i","u"]:
    print(letter,"is a vowel")
elif letter.isalpha():
    print(letter,"is a consonant")
else:
    print("Error!! Invalid input")
