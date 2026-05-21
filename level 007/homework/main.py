# 1) მომხმარებელს შემოაყვანინეთ 3 რიცხვი, პირველი start - ი, მეორე end - ი, მესამე step - ი, შემდგომ for loop - ში ჩასვით ეს რიცხვები სათანადო ადგილას და ტერმინალში გამოიტანეთ თითოეული რიცხვი start - სა და end - ს შორის.
startnum = int(input('enter start num: '))
endnum = int(input('enter end num: '))
stepnum = int(input('enter step num: '))

for i in range(startnum, endnum, stepnum):
    print(i)
# 2) მომხმარებელმა შეიყვანოს ასაკი და ქვეყანა. თუ ასაკი 18-ზე მეტია და ქვეყანა არის "Georgia" — დაბეჭდოს "Access granted", სხვა შემთხვევაში — "Access denied".
age = int(input('enter your age: '))
country = input('enter your country: ')
if age > 18 and country == 'Georgia':
    print('access granted')
else:
    print('access denied')
# 3) მომხმარებელმა შეიყვანოს რიცხვი. while ციკლით დაითვალეთ ამ რიცხვის ციფრების ჯამი. თუ ჯამი 10-ზე მეტია — დაბეჭდეთ "Big sum", სხვა შემთხვევაში — "Small sum".
number = int(input('enter any number: '))
i = 0
total = 0
if number > 10:
        print('big sum')
else:
    while i <= number:
        total += i
        i+= 1
    print(total)
# 4) მომხმარებელმა შეიყვანოს რიცხვი. while ციკლით დაბეჭდეთ მისი გამრავლების ტაბულა 1-დან 10-მდე.
num = int(input('Enter a number: '))

i = 1

while i <= 10:
    print(f'{num} x {i} = {num * i}')
    i += 1