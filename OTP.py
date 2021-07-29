import random

a = "abcdefghijklmnopqrstuvwxyz"
b = a.upper()
x1 = random.randint(0,9)
x2 =random.choice(a)
x3 =random.choice(b)
c = [x1,x2,x3]
otp=""
print(x3)
for i in range(6):
    otp += str(random.choice(c))

print(f"You One Time password is : {otp}")
