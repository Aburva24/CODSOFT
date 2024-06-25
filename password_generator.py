# Generate  Random Password
import random
import string
lower= list(string.ascii_lowercase)
upper= list(string.ascii_uppercase)
digits = list(string.digits)
symbols= list(string.punctuation)
char=""
password=[]
length=int(input("Enter the length of the password:"))
if(length>=8):
    choice=input("Enter your choice(Strong/Normal)=").lower()
    if(choice=="normal"):
        for i in range(length):
            char+=string.ascii_letters
            char+=string.digits
        for i in range(length):
            randomchar=random.choice(char)
            password.append(randomchar)
        print("Your password is" +"".join(password))
    elif(choice=="strong"):
        for i in range(length):
            char+=string.ascii_lowercase
            char+=string.ascii_uppercase
            char+=string.digits
            char+=string.punctuation
        for i in range(length):
            randomchar=random.choice(char)
            password.append(randomchar)
        print("Your password is "+"".join(password))
else:
    print("The length of the password should be greater than 8")
#Output
# Enter the length of the password: 7
# The length of the password should be greater than 8
# Enter the length of the password: 8
#  Enter your choice (Strong/Normal)=normal Your password is KsSsPQmf
# Enter the length of the password:9
# Enter your choice (Strong/Normal)=strong Your password is B[^c/g,*@
