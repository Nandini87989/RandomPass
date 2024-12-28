import string
import random
print("HELLO,WELCOME TO RANDOM PASSWORD GENERATOR")
#taking the input from the user
length = int(input("Enter the length of password: "))
# defining data
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols="!@#$%^&*`~(),.:?"
#combine the data
all=lower + upper + num + symbols
#using random
temp=random.sample(all,length)
#creating the password
password="".join(temp)
print(password)