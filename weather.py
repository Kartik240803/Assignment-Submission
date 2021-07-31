print("============Welcome to the Temperature converter============")

print("Select 1 for Celcius to Fahrenheit\nSelect 2 for Fehrenheit to Celcius")
o = int(input())
if o==1:
    wc = int(input("Enter Temperature in degree celcius :\n"))

    wf= (f"Temperature in degree fahrenheit is :\n{(9/5)*wc+32}")
    print(wf)
else:
    wf = float(input("Enter Temperature in degree Fehrenhit :\n"))

    wc= (f"Temperature in degree fahrenheit is :\n{(wf-32)*(5/9)}")
    print(wc)




