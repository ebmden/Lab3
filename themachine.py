"""
- NOTE: REPLACE 'N' Below with your section, year, and lab number
- CS2911 - 011
- Fall 2021
- Lab 3
- Names:
  - 
  - 

"The Machine" implementation of parsing and executing a program.

The application reads a file name from the user and executes the contents of the file or sends an error if the file format is not valid.

The file format is describe in "The Machine" exercise and the lab description.


Introduction: (Describe the lab in your own words)




Summary: (Summarize your experience with the lab, what you learned, what you liked, what you disliked, and any suggestions you have for improvement)




"""

# import the readfile modules to read bytes from a file
import readfile


def main():
    """
    - Input and execute a file formatted for "The Machine"
    """
    # Get chosen file from the user.
    program_file = input('Enter the name of the program to execute: ')
    # Execute the chosen file.
    execute(program_file)


def execute(program_file):
    """
    - Execute a program file formatted for "The Machine"
    :param str program_file: name of the file to execute
    """
    verify_magic_num()
    num_operations = read_num_operations()
    parse_operations(num_operations)

def verify_magic_num():

def read_num_operations():

def parse_operations(nun_operations):

def operation_add():

def operation_subtract():

def operation_multiply():

def operation_divide():

def operation_print():



# Invoke the main method to run the program.
main()
