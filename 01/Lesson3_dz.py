a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

action = input("Виберіть яку дію виконати з числами + - / : ")

if action == "+":
    print("Результат:", a + b)

elif action == "-":
    print("Результат:", a - b)

elif action == "/":
    if float(b) == 0:
        print("Розподіл на 0 не можливий!")
    else:
        print("Результат:", a / b)

elif action == "*":
    print("Результат:", a * b)

else:
    print("Не вірна дія!")