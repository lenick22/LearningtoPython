print('This program will tell me if you are allowed through the door.')
print('First tell me what is your name')
name = input()

if name == 'Nick':
    print('Great your name is ' + name)
else:
    print('You are not who I am looking for please go away')


print('Now what is your age?')
age = int(input())
if age == int(20):
    print('You are are of the correct age')
elif age < int(20):
    print('You are far too young.')
elif age > int(20):
    print('You are far too old')





