#check if this is being run as a standalone program, if so then print an error message.
if __name__ == "__main__":
    from tkinter import messagebox
    messagebox.showwarning("Warning", "soupLib is a library, not a standalone program!\nuse import to import soupLib in a program in the same folder.")
    exit()

#import libraries
import os
import platform

class terminal(): #stuff for .py files running in a terminal, this stuff mainly affects the terminal, and as such
    global system_name
    system_name = platform.system()
    
    def clearScreen(): #clears the terminal by running the Windows CLS command
        if system_name == "Windows":
            os.system("cls")
        elif system_name == "Linux" or system_name == "Darwin":
            os.system("clear")
        else:
            print("Invalid OS for clearScreen Method.")
    def userInput(question: str):
        #raise TypeError if input not string
        if not isinstance(question, str):
            raise TypeError("Invalid Input")
        inputText = "=>"
        print(question)
        user_input = input(inputText)
        return user_input