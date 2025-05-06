# Documentation

### terminal class

- clearScreen() needs no parameters and will clear the screen when running in a terminal. If running in a non-terminal environment, will instead do nothing.
- userInput() takes a question as a parameter and will return the user answer (as string)
- colorScreen() accepts a set of colors, the first one is the text, the second is the backround, also only works in a terminal like clearScreen()

### files class

- findFilesInDir() finds files in a directory, which is provided as a string argument (returns list)
- findDirsInDir() does the same as findFilesInDir but for directorys in the directory provided as a string argument (returns list)

# Version 0.0.1 (first version)

- clearScreen() function
- userInput() function

# Version 0.0.2

- stuff from 0.0.1
- check for if running as main program (and if so throw error dialouge and exit)

# Version 0.0.3

- colorScreen() function

#Version 0.0.4

- files() class
- findFilesInDir() function
- findDirsInDir() function
