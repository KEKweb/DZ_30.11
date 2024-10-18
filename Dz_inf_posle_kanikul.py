# я не понял надо ли делать через input, или просто задать переменную, но получилось вот так
numb = int(input("Введите целое число: "))

while True:
    if len(str(numb))>4 or numb<0:
        print('Вы ввели неправильное число, введите корректное число')
        numb = int(input("Введите целое число: "))
    else:
        numb = int(numb)
        break

c1 = numb // 1000
c2 = numb // 100 - c1 * 10
c3 = numb // 10 - c1 * 100 - c2 * 10
c4 = numb - c1 * 1000 - c2 * 100 - c3 * 10

print(c1,"+",c2,"+",c3,"+",c4,"=", c1 + c2 + c3 + c4)
