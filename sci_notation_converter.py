from pynput.keyboard import Key, Controller

# Accept input from the user
def accept_input():
    keyboard = Controller()
    
    keyboard.press(Key.ctrl)
    keyboard.press('`')
    keyboard.release(Key.ctrl)
    keyboard.release('`')
    
    name = input("Hello, user. Please enter your name: ")
    print(type(name))
    if name:
        print(f"Excellent. Nice to meet you {name}. Let's get started.")
        print("Enter a number in scientific notation. I will convert into a floating-point number for you")
    
    
    
# Convert user's input to scientific notation
# Convert input of scientific notation value to floating-point number

accept_input()