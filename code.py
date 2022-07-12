num = int(input('введите число: '))


def fib(var):
    if var <= 1:
        return var
    else:
        return fib(var - 1) + fib(var - 2)


for n in range(num):
    print(fib(n))
