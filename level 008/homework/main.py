# 1. შექმენი ლისტი 5 რიცხვით და დაბეჭდე.
lst = [5, 11, 17, 24, 27]
# 2. numbers = [10, 20, 30, 40, 50], დაბეჭდე პირველი და ბოლო ელემენტი.
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
# 3. numbers = [1, 2, 3, 4, 5], შეცვალე მესამე ელემენტი (3) 100-ით.
numbers = [1, 2, 3, 4, 5]
numbers[2] = 100
# 4. numbers = [5, 10, 15, 20, 25], დაბეჭდე რამდენი ელემენტია ლისტში.
numbers = [5, 10, 15, 20, 25]
print(len(numbers))
# 5. numbers = [2, 4, 6, 8, 10], for ციკლით დაბეჭდე ყველა ელემენტი ცალ-ცალკე.
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    print(num)
# 6. მომხმარებელს შემოატანინე 3 რიცხვი და ჩაწერე ლისტში.\
lst = []
for i in range(3):
    num = int(input('enter number: '))
    lst.append(numbers)
# 7. numbers = [1, 2, 3], გამოითვალე ჯამი.
numbers = [1, 2, 3]
total = 0
for num in numbers:
    total += num
# 8. numbers = [8, 3, 12, 1, 6], იპოვე ყველაზე პატარა რიცხვი(min - ის გარეშე).
numbers = [8, 3, 12, 1, 6]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)
# 9. numbers = [1, 2, 3, 4, 5, 6], დაბეჭდე მხოლოდ ლუწი რიცხვების ჯამი.
numbers = [1, 2, 3, 4, 5, 6]
total = 0
for num in numbers:
    if num % 2 == 0:
        total += num
print(total)
# 10. numbers = [10, 15, 20, 25, 30, 35], დაბეჭდე მხოლოდ კენტი რიცხვები.
numbers = [10, 15, 20, 25, 30, 35]
for num in numbers:
    if num % 2 == 1:
        print(num)