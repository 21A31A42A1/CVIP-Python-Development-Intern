import random
sym = "!@#$%^&*_/?"
lcase="abcdefghijklmnopqrstuvwxyz"
ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
str = sym+lcase+ucase+num
len = int(input("Enter length of the password:"))
password = "".join(random.sample(str,len))
print(password)
