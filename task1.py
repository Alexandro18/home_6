#прочитать примеры с одного файла и записать ответы в другой файл
if __name__ == '__main__':
    f = open('input.txt', 'r')
    f1 =  open('output.txt', 'w')
    file = f.read().split()


    for i in range(len(file)-1):
        if file[i] == '+':
            a = int(file[i-1]) + int(file[i+1])
            f1.write(str(a))
        elif file[i] == '-':
            a = int(file[i - 1]) - int(file[i + 1])
            f1.write(str(a))
        elif file[i] == '*':
            a = int(file[i - 1]) * int(file[i + 1])
            f1.write(str(a))
        try:
            if file[i] == '/':
                a = int(file[i - 1]) / int(file[i + 1])
                f1.write(str(a))
        except ArithmeticError:
            print('На ноль делить нельзя')
    f.close()