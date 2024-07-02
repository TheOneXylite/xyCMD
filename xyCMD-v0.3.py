import os
import subprocess

file_extension = "UNDEFEXT"
process = "UNDEFPROC"
filename = "UNDEFNAME"
openThis = "UNDEFFILE"
os.chdir("C:/")
dirToUse = "C:/"
choice = "UNDEFCOM"
debugOn = -1

while True:
    if debugOn == 1:
        print(choice)

    choice = input("Type \"help\" if you want a list of commands/options: ")

    if choice == "exit":
        exit()

    elif choice == "help":
        print("Available Commands:")
        print("> help: Shows this list of commands and options;")
        print("> ver: Shows some info about the project;")
        print("> exit: Stops the code from running;")
        print("> change: Changes the working directory to one of your choosing;")
        print("> back: Goes to the parent directory, works like typing cd.. in Command Prompt;")
        print("> cwd: Says what directory you're currently working on;")
        print("> list: Lists the available files/directories again.")
        print("> open: READ: Reads a .txt file and prints the result; OPEN: Opens a program on your computer;")

    elif choice == "change":
        changeDirTo = input("Choose a directory to switch to or type \"cancel\" to cancel the operation: ")
        if changeDirTo == "cancel":
            print("Operation canceled.")
        if os.path.exists(changeDirTo):
            if os.path.isdir(changeDirTo):
                os.chdir(changeDirTo)
                dirToUse = changeDirTo
            else:
                print("The specified item is not a directory.")
        else:
            print("The specified item does not exist.")

    elif choice == "back":
        dirToUse = os.path.dirname(dirToUse)
        print("Went to parent directory: ", dirToUse)

    elif choice == "cwd":
        print(os.getcwd())

    elif choice == "list":
        print("Here are the files:")
        print("Current working directory", dirToUse)
        print(os.listdir(dirToUse))

    elif choice == "open":
        action = input("Do you want to (o)pen, (r)ead or (c)ancel? ")

        if action == "c":
            print("Canceled.")

        elif action == "r":
            print("Make sure you are in the directory the file is located at!")
            print("Current directory:", os.getcwd())
            openThis = input("Select the file you want to read (.txt) or cancel: ")
            if openThis == "cancel":
                print("Canceled.")
            if os.path.exists(os.path.join(dirToUse, openThis)):
                if os.path.isfile(os.path.join(dirToUse, openThis)):
                    filename, file_extension = os.path.splitext(openThis)
                    if file_extension == '.txt':
                        with open(os.path.join(dirToUse, openThis), 'r') as file:
                            ret = file.read()
                            print("Reading the file:")
                            print(ret)
                else:
                    print("File exists but is not a .txt file.")
            else:
                print("The specified item does not exist.")

        elif action == "o":
            print("Make sure you are in the directory the file is located at!")
            print("Current directory:", os.getcwd())
            openThis = input("Select the file you want to open or cancel: ")
            if openThis == "cancel":
                print("Canceled.")
            elif os.path.exists(openThis):
                if os.path.isfile(openThis):
                    print("Opening...")
                    process = subprocess.Popen([openThis, dirToUse], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if debugOn == 1:
                        print(process)
                    print("Done! You can now continue with other tasks!")
                else:
                    print("Specified item is a directory.")
            else:
                print("Specified item not found (Are you in the correct folder?) or does not exist.")

        else:
            print("The action you chose is not valid.")

    elif choice == "dswitch":
        debugOn = 0 - debugOn
        print("Switched \"debugOn\" to: ", debugOn)

    elif choice == "debug":
        print("dswitch = switch \"debugOn\"")
        print("osdir", os.getcwd())
        print("cdir", dirToUse)
        print(choice)
        print(filename)
        print(file_extension)
        print(os.path.join(dirToUse, openThis))
        print("f:", openThis, "p:", dirToUse)
        print(process)
        print("debug?", debugOn)

    elif choice == "ver":
        print("  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,      |")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     |")
        print("##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
        print("%%%%%%%..%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Version: beta-3c")
        print("%%%%%%......%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Language: en-US")
        print("%%%%%%%%%.....%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Python version: 3.8")
        print("%%%%%%%%%%%.....%%%%%%%%%%%%%%%%%%%%%%%%     |  Made by: Xylite")
        print("%%%%%%%%......%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
        print("%%%%%%......%%%%%%%%...............%%%%%     |")
        print("%%%%%%%..%%%%%%%%%%%...............%%%%%     |")
        print(" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%      |")

    else:
        print("Invalid command entered.")
