import math

def Z(a, b, c, d):
    return ((a * math.sqrt(b) - c * math.sqrt(d)) ** 2) * (5.6/(a+b+c))

if __name__ == '__main__':
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    d = int(input('d: '))

    print(f'Результат виконання функції: {Z(a, b, c, d)}')
    print('При аргументах: ')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
