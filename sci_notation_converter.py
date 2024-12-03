from pynput.keyboard import Key, Controller

# Accept input from the user


def init_user_input():
    user_keypress()    
    
    name = input("Hello, user. Please enter your name: ")
    if name:
        print(f"Excellent. Nice to meet you {name}. Let's get started.")
        user_input = input("Enter a number in scientific notation. I will convert into a floating-point number for you: ")
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
        print(type(input), input)
    except Exception as e:
        print(f"Invalid input occurred: {e}")
    
    
# Convert user's input to scientific notation
# Convert input of scientific notation value to floating-point number

init_user_input()