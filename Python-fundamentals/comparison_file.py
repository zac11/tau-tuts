"""Comparison operations"""
print(1 < 1)
print(1<=1)
print(1==1)
print(1>=1)
print(1!=1)

name = input("What is your name")
if(name=='jess'):
    print('Hi I am Jess')

elif name == "Bob":
    print("Hi I am Bob")


else:
    print('Thanks for entering your name'+name)

name = input("Enter your name please")
if name == "jessica":
    print("Hello, nice to see you {}".format(name))

elif name == "Danielle":
    print("You're a nice person Danielle")

elif name != "Mariah":
    print("You're not Mariah")

elif name == 'Kingston':
    print("Hi {} , let's have lunch soon".format(name))

else:
    print("Have a nice day")