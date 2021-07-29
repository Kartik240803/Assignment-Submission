x = input("Enter the number you want to add in list :\n")
list =[int(i) for i in x.split()]
list.sort()
print(list)
y = input("Enter the number you want to remove from list :\n")
newlist = [int(i) for i in y.split()]
for i in newlist:
    list.remove(i)
print(list)
