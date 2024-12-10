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
        input = float(input)
        # confirm the value of input is a float type
        # print(type(input), input)
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
    places_moved = 1 - decimal_index
    # Remove the decimal from the current index
    input_char_list.pop(decimal_index)
    # Insert the decimal at index 1
    input_char_list.insert(1, '.')
    print(input_char_list, places_moved)
    
    # # run a for loop
    # for i in range(len(input_char_list)):
    #     for j in range(i + 1, len(input_char_list)):
    #         distance = j - i
    #         print("distance between i and j", distance)
        
        # if (input_char_list[i] == "."):
        #     print(i, f"list: {input_char_list}")
        #     decimal = input_char_list[i]
        #     input_char_list.remove(decimal)
        #     input_char_list.insert(1, decimal)
        #     print(input_char_list)
# Convert input of scientific notation value to floating-point number

init_user_input()