from pynput.keyboard import Key, Controller

# Accept input from the user
def accept_input():
    keyboard = Controller()
    
    keyboard.press(Key.ctrl)
    keyboard.press('`')
    keyboard.release(Key.ctrl)
    keyboard.release('`')
    
    name = input("Hello, user. Please enter your name: ")
    if name:
        print(f"Excellent. Nice to meet you {name}. Let's get started.")
        user_input = input("Enter a number in scientific notation. I will convert into a floating-point number for you: ")
        
        try:
            user_input = float(user_input)
            print(type(user_input))
        except Exception as e:
            print(f"Invalid input occurred: {e}")
    else:
        print("Well then, have an nice day.")
    
    
# Convert user's input to scientific notation
# Convert input of scientific notation value to floating-point number

accept_input()