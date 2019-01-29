while True:
    print('Who are you?')
    name = input()
    if name != 'Nick':
        continue
    print('Hello, Nick. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')
