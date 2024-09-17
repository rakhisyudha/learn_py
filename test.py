'''full_name = 'John Smith'
age = 20
is_new = True
'''

input_name = input('Type your name here: ')
name = input_name

if len(name) < 3:
    print('Name must be at least 3 character long')
elif len(name) > 50:
    print('Name can be maximum of 50 character')
else:
    print("You're good to go buddy")