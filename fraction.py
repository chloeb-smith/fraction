# ======================================================
# Chloe Smith
# 1/31/2024
# This file creates a fraction class, it will house all the methods
# that go along with creating, using, and operating with fractions
# ======================================================
class Fraction:

    def __init__(self, num, den):
        """
        instantiates a Fraction
        parameters: self, num, den
        returns: None
        """
        print('You made an object!')
        self.__num = num
        self.__den = den
        self.reduce()

    def __str__(self):
        """
        creates a string to represent fraction
        parameters: self
        returns: result
        """
        if self.__den != 1:
            result = str(self.__num) + '/' + str(self.__den)
        else:
            result = str(self.__num)
        return result

    def getNum(self):
        """
        gets the numerator of a fraction
        parameters: self
        returns: numerator (self.__num)
        """
        return self.__num

    def setNum(self,value):
        """
        sets the numerator of a fraction to a specified value
        parameters: self, value
        returns: None
        """
        self.__num = value

    def getDen(self):
        """
        gets the denominator of a fraction
        parameters: self
        returns: denominator (self.__den)
        """
        return self.__den

    def setDen(self,value):
        """
        sets the denominator of a fraction to a specified value
        parameters: self, value
        returns: None
        """
        self.__den = value

    def __calcGCD(self,a,b):
        """
        calculates the greatest common denominator
        parameters: self, a, b
        returns: a
        """
        while b:
            a , b = b , a%b
        return a

    def reduce(self):
        """
        reduces a fraction
        parameters: self
        returns: None
        """
        common = self.__calcGCD(self.__num,self.__den)
        self.__num = self.__num//common
        self.__den = self.__den//common

    def __neg__(self, other):
        """
        negates the fraction
        parameters: self, other
        returns: Fraction(-self.__num, self.__den)
        """
        return Fraction(-self.__num, self.__den)

    def __add__(self, other):
        """
        adds two fractions together
        parameters: self, other
        returns: Fraction(new_num//common, new_den//common)
        """
        new_num = self.__num * other.__den + self.__den * other.__num
        new_den = self.__den * other.__den
        common = self.__calcGCD(new_num,new_den)
        return Fraction(new_num//common, new_den//common)

    def __sub__(self, other):
        """
        subtracts two fractions
        parameters: self, other
        returns: Fraction(new_num // common, new_den // common)
        """
        new_num = self.__num * other.__den - self.__den * other.__num
        new_den = self.__den * other.__den
        common = self.__calcGCD(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        """
        multiplies a fraction by another fraction
        parameters: self, other
        returns: resultFrac
        """
        numer = self.__num * other.getNum()
        denom = self.__den * other.getDen()

        resultFrac = Fraction(numer, denom)
        resultFrac.reduce()

        return resultFrac

    def __truediv__(self, other):
        """
        divides a fraction by another fraction
        parameters: self, other
        returns: resultFrac
        """
        numer = self.__num * other.getDen()
        denom = self.__den * other.getNum()

        resultFrac = Fraction(numer, denom)
        resultFrac.reduce()

        return resultFrac

    def __eq__(self, other):
        """
        determines if two fractions are equal to one another
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num == second_num

    def __ne__(self, other):
        """
        determines if two fractions are not equal to one another
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num != second_num

    def __lt__(self, other):
        """
        determines if a fraction is less than another fraction
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num < second_num

    def __le__(self, other):
        """
        determines is a fraction is less than or equal to another fraction
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num <= second_num

    def __gt__(self, other):
        """
        determines is a fraction is greater than another fraction
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num > second_num

    def __ge__(self, other):
        """
        determines if a fraction is greater than or equal to another fraction
        parameters: self, other
        returns: True or False
        """
        first_num = self.__num * other.__den
        second_num = self.__den * other.__num
        return first_num >= second_num
