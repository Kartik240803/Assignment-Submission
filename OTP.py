import random
otp =""
for i in range(0,6):
    x= random.randint(0,9)
    otp += str(x)
print(f"You One Time password is : {otp}")