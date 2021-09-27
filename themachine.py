"""
- CS2911 - 011
- Fall 2021
- Lab 3
- Names:
  - Lucas Gral
  - Eden Basso
"The Machine" implementation of parsing and executing a program.
The application reads a file name from the user and executes the contents of the file or sends an error if the file format is not valid.
The file format is describe in "The Machine" exercise and the lab description.

Introduction: (Describe the lab in your own words)
This lab is a model of raw bytes sent from program to program, where the goal of the program is to apply 
context(or a protocol) to these bytes to determine the specific message that is being sent. The program uses helper 
methods to iterate through each byte and complete the necessary actions such as verifying the object is intended to be 
read, converting from bytes, decoding, and determining the length of a particular operation(such as adding, 
subtracting, printing, etc.). The actual raw bytes that the program is analyzing is iterated through by the readfile 
class and then returned to themachine class.  

Summary: (Summarize your experience with the lab, what you learned, what you liked, what you disliked, and any suggestions you have for improvement)
This lab taught me the importance of understanding how a program determines and executes the context of a message sent 
from another program. Specifically, I learned how to execute the steps I needed to take such as concatenation, 
decoding, and converting from raw bytes to read these messages sent in order to adhere to a specific protocol. I have no 
specific suggestions for this lab, I believe that the lab connects very well with concepts we discussed in class
(interpreting data sent over the network) and the exercises we practiced leading up to the lab
(encoding/decoding, and converting to/from raw bytes)."""

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


#:LG:
def execute(program_file):
    """
    - Execute a program file formatted for "The Machine"
    :param str program_file: name of the file to execute
    """
    readfile.set_file(program_file)

    verify_magic_num()
    num_operations = read_num_operations()
    parse_operations(num_operations)


#:LG:
def verify_magic_num():
    magic_num = b''
    for i in range(0, 4):
        magic_num += readfile.read_byte()

    if(magic_num == b'\x31\x41\xFA\xCE'):
        print("This is a valid The Machine™ file")
    else:
        print("This is NOT a valid The Machine™ file. It is either corrupted or of a different format.")
        exit(1)


#:LG:
def read_num_operations():
    return int.from_bytes(readfile.read_byte() + readfile.read_byte(), 'big')


#:LG:
def parse_operations(num_operations):
    print(num_operations, "operations...")
    for i in range(0, num_operations):
        operation_index = int.from_bytes(readfile.read_byte(), 'big')
        if operation_index <= 5 and operation_index > 0:
            [operation_add,
             operation_subtract,
             operation_multiply,
             operation_divide,
             operation_print
            ][operation_index-1]()
        else:
            print('Invalid operation:', operation_index)
            exit(1)


def read_operand():
    """
    Read the next 2 bytes and convert to ints

    :return: a list containing 2 ints
    :rtype: list
    :author: Eden Basso
    """
    operand1 = readfile.read_byte()
    operand2 = readfile.read_byte()
    operand1 = int.from_bytes(operand1, 'big')
    operand2 = int.from_bytes(operand2, 'big')
    operand_list = [operand1, operand2]
    return operand_list


def operation_add():
    """
    Add the 2 operands/bytes together

    :return: the sum of 2 ints converted from bytes
    :rtype: int
    :author: Eden Basso
    """
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    sum_bytes = operand1 + operand2
    return sum_bytes


def operation_subtract():
    """
    Subtract the 2 operands/bytes together

    :return: the difference of 2 ints converted from bytes
    :rtype: int
    :author: Eden Basso
    """
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    difference = operand1 - operand2
    return difference


def operation_multiply():
    """
    Multiply the 2 operands/bytes together

    :return: the product of 2 ints converted from bytes
    :rtype: int
    :author: Eden Basso
    """
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    product = operand1 * operand2
    return product


def operation_divide():
    """
    Divide the 1st operand by the second operand

    :return: the quotient of 2 ints converted from bytes
    :rtype: int or float
    :author: Eden Basso
    """
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    quotient = operand1 / operand2
    return quotient


def operation_print():
    """
    Convert bytes to a string until program reads '0A'

    :return: the decoded message in ASCII from bytes
    :rtype: str
    :author: Eden Basso
    """
    byte_str = b''
    while (next_byte := readfile.read_byte()) != b'\n':
        byte_str = byte_str + next_byte
    byte_str = byte_str.decode('ASCII')
    return byte_str


main()
