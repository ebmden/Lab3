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
    operand1 = readfile.read_byte()
    operand2 = readfile.read_byte()
    operand1 = int.from_bytes(operand1, 'big')
    operand2 = int.from_bytes(operand2, 'big')
    operand_list = [operand1, operand2]
    return operand_list


def operation_add():
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    byte_sum = operand1 + operand2
    return byte_sum


'''def operation_add():
    operand1 = readfile.read_byte()
    operand2 = readfile.read_byte()
    operand1 = int.from_bytes(operand1, 'big')
    operand2 = int.from_bytes(operand2, 'big')
    byte_sum = operand1 + operand2
    return byte_sum'''


def operation_subtract():
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    byte_sub = operand1 - operand2
    return byte_sub


def operation_multiply():
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    byte_multi = operand1 * operand2
    return byte_multi


def operation_divide():
    operand_list = read_operand()
    operand1 = operand_list[0]
    operand2 = operand_list[1]
    byte_div = operand1 / operand2
    return byte_div


def operation_print():
    byte_str = b''
    while (next_byte := readfile.read_byte()) != b'\n':
        byte_str = byte_str + next_byte
    byte_str = byte_str.decode('ASCII')
    return byte_str

main()
