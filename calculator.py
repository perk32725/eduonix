#!/usr/bin/env python3
# simple calculator project

import sys

def add(n1, n2):  # addition
    return n1 + n2

def sub(n1, n2):  # subtraction
    return n1 - n2

def mul(n1, n2):  # multiplication
    return n1 * n2

def div(n1, n2):  # division
    if n2:
        return n1 / n2
    print('cannot divide by Zero!')
    return 0

def rec(n):  # reciprocal
    if n:
        return 1/n
    print('cannot take reciprocal of Zero!')
    return 0


# main()
if __name__ == '__main__':
    while True:
        func = input('function (add, sub, mul, div, rec, or exit):')
        if func == 'exit':
            sys.exit(0)

        num1 = int(input('first number: '))

        if func == 'add':
            num2 = int(input('second number: '))
            print(f'{num1} + {num2} = {add(num1, num2)}')

        if func == 'sub':
            num2 = int(input('second number: '))
            print(f'{num1} - {num2} = {sub(num1, num2)}')

        if func == 'mul':
            num2 = int(input('second number: '))
            print(f'{num1} * {num2} = {mul(num1, num2)}')

        if func == 'div':
            num2 = int(input('second number: '))
            print(f'{num1} / {num2} = {div(num1, num2)}')

        if func == 'rec':
            print(f'reciprocal of {num1} is {rec(num1)}')

# EOF:
