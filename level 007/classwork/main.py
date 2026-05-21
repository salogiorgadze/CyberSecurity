# 1) შექმენით ორი ცვლადი password_input და registered_password, while ციკლის პირობაში შეამოწმეთ არ უდრის თუ არა რეგისტრეირებული ამჟამად შემოტანილ [პაროლს.

# მომხმარებელმა პაროლი იქამდე უნდა შემოიტანოს სანამ სწორი არ იქნება პაროლი.

registered_password = 'python'
password_input = input('enter password: ')

while password_input != registered_password:
    print('incorrect try again')
    password_input = input('enter password: ')
print('access granted')

# 2) მომხმარებელს შემოატანინეთ რიცხვი, შემდგომ if else დახმარებით შეამოწმეთ, ეს რიცხვი თუ ლუწია გამოიტანეთ ტერმინალში "Even", თუ კენტი "Odd".

number = int(input('enter any number: '))
if number % 2 == 0:
    print('even')
else:
    print('odd')

# 3) მომხმარებელს შემოატანინეთ რიცხვი და შეამოწმეთ, თუ რიცხვი დადებითია და ლუწია მაშინ გამოიტანეთ რიცხვები 0 - იდან მომხმარებლის რიცხვის ჩათვლით, თუ პირობა არ შესრულდა მაშინ გამოიტანეთ error ი.
number = int(input('enter any number: '))
if number > 0:
    print('positive')
else:
    print('negative')
# 4) მომხმარებელს მოსთხოვეთ მისი ასაკი, შემდგომ შეამოწმეთ: თუ ასაკი ნაკლებია 13 - ზე და მეტია 0 - ზე მაშინ გამოუტანეთ ტერმინალში "Child", თუ 13 - ზე მეტია და ნაკლებია 18 - ზე მაშინ "Teen", თუ მეტია 18 - ზე და ნაკლებია 59 - ზე მაშინ "Adult" ყველა სხვა შემთხვევაში "Senior" (გამოიყენეთ if, elif და else)
age = int(input('enter your age: '))
if age < 13 and age > 0:
    print('Child')
elif age > 13 and age < 18:
    print('Teen')
elif age >= 18 and age < 59:
    print('Adult')
else:
    print('Senior')