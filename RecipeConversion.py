# Recipe Conversion Program
# ==============================================================================
# Chloe Smith
# 1/2/2024
# This program will read an existing recipe and change it based on a conversion
# entered by the user
# ==============================================================================
from fraction import *

def getFile():

    ''' Returns as a tuple the file name entered by the user and the
        open file object. If the file exceeds three attempts of opening
        sucessfully, an IO exception is raised.
    '''
    # setting the maximum number of attempts and also setting the current attempts
    # variable to 0
    MAX_ATTEMPTS = 3
    current_attempt = 0

    # input validation loop for incorrect user input
    while current_attempt < MAX_ATTEMPTS:
        file_name = input('Enter the file name: ')
        try:
            # opens file in read mode
            input_file = open(file_name, 'r')
            return (file_name, input_file)
        # if a FileNotFoundError is found it will print an error message
        except FileNotFoundError:
            print('File not found, please enter an existing file')
            # adds 1 to the current attempts
            current_attempt += 1
    # this will raise an IOError
    if current_attempt == MAX_ATTEMPTS:
        raise IOError(f'{file_name} is not a valid file name')


#don't touch removeMeasure
def removeMeasure(line):

    ''' Returns provided line with any initial digits and fractions (and
        any surrounding blanks) removed. 
    '''

    k = 0
    blank_char = ' '
    
    while k < len(line) and (line[k].isdigit() or \
                             line[k] in ('/', blank_char)):
        k = k + 1

    return line[k:len(line)]

#don't touch scanAsFraction
def scanAsFraction(line):

    ''' Scans all digits, including fractions, and returns as a Fraction
        object. For example, '1/2' would return as Fraction value 1/2,
        '2' would return as Fraction 2/1, and '2 1/2' would return as
        Fraction value 3/2.
    '''

    completed_scan = False
    value_as_frac = Fraction(0,1)
    
    while not completed_scan:
        k = 0
        while k < len(line) and line[k].isdigit():
            k = k + 1
            
        numerator = int(line[0:k])
        
        if k < len(line) and line[k] == '/':
            k = k + 1
            start = k
            while k < len(line) and line[k].isdigit():
                k = k + 1
                
            denominator = int(line[start:k])
        else:
            denominator = 1

        value_as_frac = value_as_frac + Fraction(numerator, denominator)

        
        if k == len(line):
            completed_scan = True
        else:  
            line = line[k:len(line)].strip()
            
            if not line[0].isdigit():
                completed_scan = True
            
    return value_as_frac

def convertLine(line, factor):

    ''' If line begins with a digit, then returns line with the value
        incremented by factor. Otherwise, returns line unaltered.
        (For example, for a factor of 2, '1/4 cup sugar' returns as
        '1/2 cup sugar and '2 cups sugar' returns as '4 cups sugar'.)
    '''

    #code goes here
    #The idea is that you are going to step through the line of the recipe
    #if you find the digit in the line
    #scan through the line looking for the fraction and mulitply it by the factor to create a new fraction
    #then you need to build the new line by removing the original measure and putting the new fraciton measure in the line
    #return the new line
    #this method should utilize the scanasfraction and removemeasure functions

    # checking to see if a line starts with a number
    if line[0].isdigit():
        # if the line starts with a number it will convert the number by the
        # conversion factor and assign it to conv_line
        # calls the scanAsFraction function to create a fraction object
        value = scanAsFraction(line)
        new_value = value * factor
        without_measure = removeMeasure(line)
        conv_line = str(new_value) + ' ' + without_measure
    # if the line doesn't begin with a number conv_line is just assigned to
    # the pre-existing line
    else:
        conv_line = line

    return conv_line


# Do not change anything below this line!
# You are responsible for writing the 2 empty functions above
# ---- main
# This is where the program begins running
# Step through this and make sure you understand what main is doing

# display welcome
print('This program will convert a given recipe to a different')
print('quantity based on a specified conversion factor. Enter a')
print('factor of 1/2 to halve, 2 to double, 3 to triple, etc.\n')

try:

    # get file name and open file
    file_name, input_file = getFile()   #you need to write this function

    # get conversion factor
    conv_factor = input('Enter the conversion factor: ')
    conv_factor = scanAsFraction(conv_factor)   #you need to write this function

    # open output file named 'conv_' + file_name
    output_file_name = 'conv_' + file_name
    output_file = open(output_file_name, 'w')

    # convert recipe                  
    empty_str = ''
    recipe_line = input_file.readline()  #you are converting the recipe line by line

    while recipe_line != empty_str:     #while we haven't gotten to the end of the file
        recipe_line = convertLine(recipe_line, conv_factor)    #you need to write this funciton
        output_file.write(recipe_line)      #write the new line to the new file
        recipe_line = input_file.readline()   #get the next line of the original recipe

    # close files
    input_file.close()
    output_file.close()

    # display completion message to user
    print('Converted recipe in file: ', output_file_name)

except IOError as err_mesg:  # catch file open error
    print(err_mesg)

