import random as a
a1=input('write an option.')
a2=input('write an option.')
a3=input('write an option.')
a4=input('write an option.')
print('Enter for changing the number.')
while True:
    list=[a1,a2,a3,a4]
    b=a.randint(0,3)
    c=input(list[b])
    if c=='break':
        break
