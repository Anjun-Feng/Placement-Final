def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def read_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

def add_values(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Invalid types for addition. Both values must be numbers."

def check_file_permissions(filename):
    try:
        with open(filename, 'r'):
            # We only need to open it to check permissions, no need to read.
            pass
        return f"Successfully opened '{filename}'."
    except PermissionError:
        return f"Error: Permission denied to access '{filename}'."

def get_list_element(data, index):
    try:
        return data[index]
    except IndexError:
        return f"Error: Index {index} is out of range for the list."

def get_user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        return "Input cancelled by user."

def safe_division(dividend, divisor):
    try:
        return dividend / divisor
    except ArithmeticError:
        return "An arithmetic error occurred (e.g., division by zero)."

def file_with_encoding(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        return f"Error: Could not decode '{filename}' with '{encoding}' encoding."

def safe_list_sort(data):
    try:
        data.sort()
        return "Data sorted successfully."
    except AttributeError:
        return "Error: The provided data object does not have a 'sort' method."