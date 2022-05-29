#!/usr/bin/env python3
# -- coding: utf-8 --


if __name__ == '__main__':
    lis = []
    i_null = []
    k = 0
    n = int(input('Введите длину массива: '))
    print('Введите элементы массива\n')
    for i in range(n):
        lis.append(int(input()))
        if lis[i] == 0:
            i_null.append(i)
            k += 1
    print('Колчисетво нулевых элементов = ', k)
    print('Индексы нулевых элементов = ', i_null)
