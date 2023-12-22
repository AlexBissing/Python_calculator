def main():
    try:
        while(True):
            put = input("input: ")
            sl = put.split()
            a, op, b = int(sl[0]), sl[1], int(sl[2])

            if len(sl) > 3:
                print("Ошибка ввода")
            elif a > 10 or b > 10:
                print("Вводите числа до 10 включительно")
            elif b == 0:
                print("Делить на ноль нельзя")
            elif op == '+':
                print(a + b)
            elif op == '-':
                print(a - b)
            elif op == '/':
                print(a // b)
            elif op == '*':
                print(a * b)
    except Exception:
        print("Строка не является математической операцией")




main()
