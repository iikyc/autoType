import pyautogui
import time

print("Welcome to autoType!\n")

message = input("Enter the text you want to type:-\n")
number = int(input("Enter how many times you would like the program to type and send the message:-\n"))
timeDelay = int(input("Enter how long you would like the program to wait before typing in seconds:-\n"))
confirm = input("WARNING: PLEASE MAKE SURE YOU ARE IN THE CORRECT TEXTFIELD BEFORE CONTINUING, WOULD YOU LIKE TO CONTINUE? (y / n):-\n")

def start(number, message, timeDelay):
    print("Starting...")
    time.sleep(timeDelay)

    for n in range(0, number):
        pyautogui.typewrite(message)
        pyautogui.press("enter")

if (confirm == "y"):
    start(number, message, timeDelay)
else:
    print("Aborting program!...")
    exit(0)








