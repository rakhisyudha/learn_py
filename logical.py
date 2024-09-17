user_input = input('Enter income: ')
user_input2 = input('Enter salary: ')
user_input3 = input('Have Criminal issue? yes or no: ')
try:
    income = int(user_input)
    salary = int(user_input2)
    criminal_issues = (user_input3 == 'yes')
except ValueError:
    print('Enter Valid Integer')
else:
    if income > 100000 and salary > 5000 and criminal_issues == False :
        print('Eligible for loan')
    else:
        print('Not Eligible for loan')