# 1) შექმენი ცვლადი და დაბეჭდე მისი ტიპი.
name = 'salka'
print(type(name))
# 2) შექმენი ცვლადი და შეამოწმე არის თუ არა str.
print(type(name) == str)
# 3) შექმენი და დაბეჭდე მისი ტიპი.
name = 'salka'
print(type(name))
# 4) მომხმარებელს შემოატანინე მონაცემი და შეამოწმე რა ტიპია.
num = int(input('enter num: '))
print(type(num))
# 5) სტრინგი გადააქციე integer-ად.
num = '517'
print(int(num))
# 6) integer გადააქციე string-ად.
# 7) სტრინგი გადააქციე float-ად.
# 8) float გადააქციე integer-ად.
number = 517
print(str(number))
print(float(number))
flt = 5.17
print(int(flt))
# 9) მომხმარებლის შემოტანილი რიცხვი string-იდან integer-ად გადააქციე.
numstr = input('enter num: ')
print(int(numstr))
# 10) კოდი არასწორად აერთიანებს რიცხვებს, გაასწორე:
num1 = "10"
num2 = "20"

print(int(num1) + int(num2))
# 11.)კოდი ტექსტს ვერ უმატებს რიცხვს, გაასწორე:
#     age = 15

#     print("Age: " + str(age))
# 12) შეამოწმე არის თუ არა 10 მეტი 5-ზე.
print(10 > 5)
# 13) შეამოწმე არის თუ არა ორი რიცხვი ტოლი.
print(17 == 17)
# 14) შეამოწმე არის თუ არა 3 ნაკლები 1-ზე.
print(3 < 1)
# 15) მომხმარებლის ასაკი შეადარე 18-ს.
age = int(input('enter your age: '))
print(age == 18)
# 16) გადახედეთ ხელახლა ჩანაწერს.