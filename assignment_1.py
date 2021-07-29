x = input("Enter the numbers: \n")
list = [int(i) for i in x.split()]
print(f"You enterd :{list}")
list.sort()
list.reverse()
print(f"List in Decreasaing manner :{list}")