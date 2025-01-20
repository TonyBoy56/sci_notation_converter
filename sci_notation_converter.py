from array import array 
from pynput.keyboard import Key, Controller

# Initialize receiving input from the user
def init_user_input():
    user_keypress()    
    
    name = input("Hello, user. Please enter your name: ")
    if name:
        print(f"Excellent. Nice to meet you {name}. Let's get started.")
        user_input = input("Enter a number. I will convert it to scientific notation for you: ")
        str_to_float(user_input)
    else:
        print("Well then, have an nice day. Run the program to try again.")

# Simulate Keyboard inputs
def user_keypress():
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('`')
    keyboard.release(Key.ctrl)
    keyboard.release('`')

# Convert string input to float
def str_to_float(input):
    try:
        # convert string input to float
        input = float(input)
        float_to_notation(input)
    except Exception as e:
        print(f"Invalid input occurred: {e}")
        print("Restart the program and enter a number.")
    
# Convert user's input to scientific notation
def float_to_notation(float_input):
    # scientific notation formula:  a x 10^b
    input_char_list = list(str(float_input))
    
    if '.' in input_char_list:
        decimal_index = input_char_list.index('.')
    else:
        raise ValueError("Error: the number must contain a decimal point.")
    
    # Calculate how many places the decimal needs to move
    
    if float_input > .99 or float_input < -.99:
        places_moved = 1 - decimal_index
    else:
        print("float_input is less than 1")
        
    # Remove the decimal from the current index
    input_char_list.pop(decimal_index)
    # Insert the decimal at index 1
    if input_char_list[0] != "-":
        input_char_list.insert(1, '.')
    else:
        input_char_list.insert(2, '.')
        
    
    # Determine negative/positive exponent
    # if float_input < 1 and float_input > 0:
    #     if places_moved < 0:
    #         places_moved
    #     else: 
    #         places_moved = places_moved * -1
    
    # print(input_char_list, places_moved)
    
    # join the list and store as a float
    result_num = float(''.join(input_char_list))
    print(f"Value of the result_num: {result_num}") 
    print(f"value of places_moved: {places_moved}")
    print(f"result string data type: {type(result_num)}")
    
    
# Convert input of scientific notation value to floating-point number

init_user_input()