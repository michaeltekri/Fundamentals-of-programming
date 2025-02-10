#A program to check whether a year is a leap year or not

first=2016
second=2026
number=second
if number%4==0:
    print("Leap year is",number)
else:
    print("Normal year is",number)


#A program to check whether a letter is a consonant or a vowel
letter="b"
letter=letter.lower()
if letter in ["a","e","o","i","u"]:
    print(letter,"is a vowel")
elif letter.isalpha():
    print(letter,"is a consonant")
else:
    print("Error!! Invalid input")

ltr='t'
if ltr=='a'or ltr=='e'or ltr=='o'or ltr=='i'or ltr=='u':
    print("vowel")
else:
    print("consonant")