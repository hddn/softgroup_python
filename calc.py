def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print 'You cannot divide by 0'

def substract(a, b):
    return a - b

actions = {
    '+': add,
    '*': multiply,
    '/': divide,
    '-': substract
}


number_one = float(raw_input('Please enter the first number: '))
number_two = float(raw_input('Please enter the second number: '))
operator = raw_input('Enter the operator: ')

result = actions[operator](number_one, number_two)

print result

