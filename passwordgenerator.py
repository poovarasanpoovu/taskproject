import random

print("Password create project".title().center(30,"*"),"\n")

number = "123456789"
char = "abcdefghi"
special_char = "!@#$%^&*_+"

all_char = number+char+special_char

length = int(input("Enter Password length : "))

password ="".join(random.sample(all_char,length))

print("The Password is : %s"% password)
