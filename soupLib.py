#check if this is being run as a standalone program, if so then throw an error message.
if __name__ == "__main__":
    from tkinter import messagebox
    messagebox.showerror("soupLib", "soupLib is a library, not a standalone program!\nuse import to import soupLib in a program in the same folder.")
    exit()

#import libraries
import os
import platform

class terminal(): #stuff for .py files running in a terminal, this stuff mainly affects the terminal, and as such
    global OS_name
    OS_name = platform.system()
    
    def clearScreen(): #clears the terminal by running the Windows CLS command
        if OS_name == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def userInput(question: str):
        #raise TypeError if input not string
        if not isinstance(question, str):
            raise TypeError("Invalid Input")
        inputText = "=>"
        print(question)
        user_input = input(inputText)
        return user_input
    def colorScreen(foreGround, backGround):
        #format colors for checking
        colA = str(foreGround).lower().strip()
        colB = str(backGround).lower().strip()
        
        #colA
        if colA == "black":
            fA = "0"
        elif colA == "blue":
            fA = "1"
        elif colA == "green":
            fA = "2"
        elif colA == "aqua":
            fA = "3"
        elif colA == "red":
            fA = "4"
        elif colA == "purple":
            fA = "5"
        elif colA == "yellow":
            fA = "6"
        elif colA == "white":
            fA = "7"
        elif colA == "gray":
            fA = "8"
        elif colA == "light_blue":
            fA = "9"
        elif colA == "light_green":
            fA = "A"
        elif colA == "light_aqua":
            fA = "B"
        elif colA == "light_red":
            fA = "C"
        elif colA == "light_purple":
            fA = "D"
        elif colA == "light_yellow":
            fA = "E"
        elif colA == "light_white":
            fA = "F"
            
        #colB
        if colB == "black":
            fB = "0"
        elif colB == "blue":
            fB = "1"
        elif colB == "green":
            fB = "2"
        elif colB == "aqua":
            fB = "3"
        elif colB == "red":
            fB = "4"
        elif colB == "purple":
            fB = "5"
        elif colB == "yellow":
            fB = "6"
        elif colB == "white":
            fB = "7"
        elif colB == "gray":
            fB = "8"
        elif colB == "light_blue":
            fB = "9"
        elif colB == "light_green":
            fB = "A"
        elif colB == "light_aqua":
            fB = "B"
        elif colB == "light_red":
            fB = "C"
        elif colB == "light_purple":
            fB = "D"
        elif colB == "light_yellow":
            fB = "E"
        elif colB == "light_white":
            fB = "F"
        
        os.system(f"color {fB}{fA}")
class files():
    def findFilesInDir(path):
        returnList = []
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                returnList.append(file)
        return returnList
    
    def findDirsInDir(path):
        returnList = []
        for file in os.listdir(path):
            if not os.path.isfile(os.path.join(path, file)):
                returnList.append(file)
        return returnList