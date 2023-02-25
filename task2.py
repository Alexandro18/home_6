#отработать для программы исключения

if __name__ == '__main__':
    f = open('input.txt', 'r')
    file = f.read().split()

    try:
        for i in range(len(file)-1):
            if file[i] == '/':
                print(int(file[i-1]) / int(file[i+1]))
    except ArithmeticError:
       print('На ноль делить нельзя')

    f.close()
