import math


def addition(num_1, num_2):
    return num_1+num_2

def subtraction(num_1, num_2):
    return num_1-num_2

def multiplication(num_1, num_2):
    return num_1*num_2

def division(num_1, num_2):
    return num_1/num_2

def square_root(num_1):
    return math.sqrt(num_1)

def mean(num_1, num_2):
    return (num_1+num_2)/2

def power(num_1, num_2):
    return num_1**num_2

def cosine(num_1):
    return math.cos(num_1)

def range_between_operands(num_1, num_2):
    range_ = []
    for num in range(num_1+1, num_2):
        range_.append(num)

    return range_

def enter_operands():
    operands = {}
    try:
        operands['num_1'] = int(input('enter first number: '))
        operands['num_2'] = int(input('enter second number: '))

    except ValueError:
        print('Not a valid operand: please input an integer')

    return operands

def choose_operation():
    valid_operations = ['+', '-', '*', '/', 's', 'm', 'p', 'c', 'r']
    operation = input('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        s for square root
        m for mean
        p for power
        c for cosine
        r for range (this prints the numbers exclusive between operands)
        ''')

    for op in valid_operations:
        if op == operation:
            return op
            break
    else:
        raise Exception("'{}' is not a valid operand: please input a valid operation.".format(operation))


def calculate():
    # cal = Calculator()
    operand = enter_operands()
    operation = choose_operation()

    if operation == '+':
        sum_ = addition(operand['num_1'], operand['num_2'])
        print("{} + {} is: ".format(operand['num_1'],
                                    operand['num_2']), sum_)

    elif operation == '-':
        difference = subtraction(operand['num_1'], operand['num_2'])
        print("{} - {} is: ".format(operand['num_1'],
                                    operand['num_2']), difference)

    elif operation == '*':
        product = multiplication(operand['num_1'], operand['num_2'])
        print("{} * {} is: ".format(operand['num_1'],
                                    operand['num_2']), product)

    elif operation == '/':
        quotient = division(operand['num_1'], operand['num_2'])
        print("{} / {} is: ".format(operand['num_1'],
                                    operand['num_2']), quotient)

    elif operation == 's':
        try:
            sqroot = square_root(operand['num_1'])
            print("the square root of {} is: ".format(operand['num_1'], sqroot))
        except ValueError:
            print('s: square root, does not take in negative numbers')

    elif operation == 'm':
        avg = mean(operand['num_1'], operand['num_2'])
        print("The mean of {} and {} is: ".format(operand['num_1'],
                                                  operand['num_2']), avg)

    elif operation == 'p':
        power_ = power(operand['num_1'], operand['num_2'])
        print("{} to the power of {} is: ".format(operand['num_1'],
                                                  operand['num_2'], sqroot))

    elif operation == 'c':
        cos = cosine(operand['num_1'])
        print("the cosine of {} is: ".format(operand['num_1'], cos))

    elif operation == 'r':
        range_ = range_between_operands(operand['num_1'], operand['num_2'])
        print("The range between {} and {} exclusive is : ".format(operand['num_1'],
                                                                   operand['num_2'],
                                                                   range_))
    again()


def again():
    calculate_again = input('''

        Would you like to use Calculator again?
        Y for yes
        N for no

        ''')

    # Accept 'y' or 'Y' by adding str.upper()
    if calculate_again.upper() == 'Y':
        calculate()

    # Accept 'n' or 'N' by adding str.upper()
    elif calculate_again.upper() == 'N':
        print('''

        Thanks for using Calculator!
        Come back anytime :)

        ''')

    else:
        again()


if __name__ == '__main__':
    print('''

    Welcome to Calculator!

    You will be asked to enter two operands and an operation to be performed on
    them. For example: <5> and <2>, and <+>, will return <7>. If a particular
    operation requires only one operand, it will neglect the second operand
    entered. For example: <36> and <2>, and <s> (for square root) will return the
    the square root of 36.

    ''')

    calculate()
