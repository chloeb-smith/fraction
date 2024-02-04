# =================================================================================
# Chloe Smith
# 1/26/2024
# This is the testing file for the fraction class we created
# =================================================================================

from fraction import *
def main():
    print('Fraction Fun!!')
    print('This program will display the different methods for the fraction class\n')
    frac1 = Fraction(1,2)
    frac2 = Fraction(1,3)
    print('The hard coded fractions are as follows:')
    print(f'frac1 is {frac1} frac2 is {frac2}\n')
    print('Next you will change the fractions')

    flag = True
    while flag == True:
        # input validation to make sure when the user enters their fractions
        # they enter integers
        try:
            frac1.setNum(int(input('Enter numerator for first fraction: ')))
            frac1.setDen(int(input('Enter denominator for first fraction: ')))
            frac1.reduce()

            frac2.setNum(int(input('Enter numerator for second fraction: ')))
            frac2.setDen(int(input('Enter denominator for second fraction: ')))
            frac2.reduce()
            # input validation to confirm user did not set denominators to zero
            if frac1.getDen() != 0 and frac2.getDen() != 0:
                flag = False
            else:
                print('Denominators cannot be set to zero')
        except ValueError:
            print('You need to enter integers!')

    print(f'\nyour first fraction is {frac1}')
    print(f'your second fraction is {frac2}\n')

    # displaying the __neg__ method
    print(f'Your fractions negated are {frac1.__neg__(frac1)} \
and {frac2.__neg__(frac2)}\n')

    # displaying the __add__ and __sub__ methods
    print(f'The sum of your fractions is {frac1.__add__(frac2)}')
    print(f'Your second fraction subtracted from your first fraction is \
{frac1.__sub__(frac2)}\n')

    # displaying the __mul__ and __truediv__ methods
    print(f'The product of your fractions is {frac1.__mul__(frac2)}')
    print(f'Your first fraction dived by your second fraction is \
{frac1.__truediv__(frac2)}\n')

    # displaying the __eq__ method
    equality = frac1.__eq__(frac2)
    if equality == True:
        print(f'The fractions are equal to each other')
    elif equality == False:
        print(f'The fractions are not equal to each other')

    # displaying the __ne__ method
    notEqual = frac1.__ne__(frac2)
    if notEqual == True:
        print(f'The fractions are not equal to each other\n')
        # displays __le__ method only if fractions aren't equal
        lessThan = frac1.__lt__(frac2)
        if lessThan == True:
            print(f'{frac1} < {frac2}\n')
        elif lessThan == False:
            print(f'{frac1} < {frac2}\n')
        # displays __ge__ method only if fractions aren't equal
        greaterThan = frac1.__gt__(frac2)
        if greaterThan == True:
            print(f'{frac1} > {frac2}\n')
        elif greaterThan == False:
            print(f'{frac2} > {frac1}\n')
    elif notEqual == False:
        print(f'The fractions are equal to each other\n')

    # displays the __le__ method
    lessEqual = frac1.__le__(frac2)
    if lessEqual == True:
        print(f'{frac1} <= {frac2}\n')
    elif lessEqual == False:
        print(f'{frac2} <= {frac1}\n')

    # displays the __ge__ method
    greaterEqual = frac1.__ge__(frac2)
    if greaterEqual == True:
        print(f'{frac1} >= {frac2}\n')
    elif greaterEqual == False:
        print(f'{frac2} >= {frac1}\n')


main()
