import os
import subprocess
import logging
import time

logger = "noLogging"
skip = False
log = "undef"
powerMode = False
logged_in_user = os.getlogin()

os.chdir("C:/")
dir_to_use = "C:/"


def startup():
    print("Hello there! Welcome to xyCMD")
    print("You're currently running version xyCMD-v1.2 of the script.")


blocked_args = [
    "*"
    "-q"
]


def change_file(with_this_name, write_this):
    try:
        with open(with_this_name, 'w') as writer:
            writer.write(write_this)
        print(f"File '{with_this_name}' changed successfully!")
    except OSError as err:
        print(f"Error creating file: {err}")


def change_dir(dir_to_change):
    if dir_to_change == "cancel":
        print("Operation canceled.")
        if log == "y":
            logger.info(f"Canceled switching directories.")
    if os.path.exists(dir_to_change):
        if os.path.isdir(dir_to_change):
            os.chdir(dir_to_change)
            if log == "y":
                logger.info(f"Changed directory to: {dir_to_change}")
            to_use = dir_to_change
            return to_use
        else:
            print("The specified item is not a directory.")
            if log == "y":
                logger.error(f"The specified item is not a directory: {dir_to_change}")
    else:
        print("The specified item does not exist.")
        if log == "y":
            logger.error(f"The specified item does not exist: {dir_to_change}")


name_of_file = "C:/xyCMD/permLog.txt"

if os.path.exists("C:/xyCMD/permLog.txt"):
    try:
        with open(name_of_file, 'r') as f:
            content = f.read()
            if content == "yes":
                skip = True
            else:
                skip = False
    except OSError as e:
        print(f"Error reading file: {e}")

if skip is False:
    if not os.path.exists("C:/xyCMD/xyCMD-v1.2.log"):
        print("Before you start, you can make a LOG file to save error messages.")
        print("It doesn't look like you have one already.")
        log = input("Do you want to create a file now? (y/n): ")
        if log == "y":
            logdirpar = "C:/"
            logdirname = "xyCMD"
            logdirpath = os.path.join(logdirpar, logdirname)
            if not os.path.exists("C:/xyCMD"):
                os.mkdir(logdirpath)
                os.chdir("C:/xyCMD")
                logging.basicConfig(filename='xyCMD-v1.2.log', level=logging.DEBUG)
                logger = logging.getLogger(__name__)
                print("Activating permLog will not show this again.")
                print("WARNING! permLog cannot be deactivated without going into the file manually!")
                perm_log = input("Do you want to activate permLog? (y/n) ")
                if perm_log == "y":
                    if not os.path.exists("C:/xyCMD/permLog.txt"):
                        os.chdir("C:/xyCMD/")
                        change_file("C:/xyCMD/permLog.txt", "yes")
                        print("Restarting...")
                        exit()
                    else:
                        print("permLog file already created!")
                        print("Modifying file contents...")
                        change_file("C:/xyCMD/permLog.txt", "yes")
                        print("Restarting...")
                        exit()
            else:
                os.chdir("C:/xyCMD/")
                logging.basicConfig(filename='xyCMD-v1.2.log', level=logging.DEBUG)
                logger = logging.getLogger(__name__)
                print(f"Created logging directory: {logdirpath}")
                logger.info(f"Created the logging directory: {logdirpath}")
                print("Activating permLog will not show this again.")
                print("WARNING! permLog cannot be deactivated without going into the file manually!")
                perm_log = input("Do you want to activate permLog? (y/n) ")
                if perm_log == "y":
                    if not os.path.exists("C:/xyCMD/permLog.txt"):
                        os.chdir("C:/xyCMD/")
                        change_file("permLog.txt", "yes")
                        print("Restarting...")
                        exit()
                    else:
                        print("permLog file already created!")
                        print("Modifying file contents...")
                        change_file("C:/xyCMD/permLog.txt", "yes")
                        print("Restarting...")
                        exit()

        elif log == "n":
            print("Log not created.")
    else:
        log = "y"
        os.chdir("C:/xyCMD")
        logging.basicConfig(filename='xyCMD-v1.2.log', level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        print("Activating permLog will not show this again.")
        perm_log = input("Do you want to activate permLog? (y/n) ")
        if perm_log == "y":
            if not os.path.exists("C:/xyCMD/permLog.txt"):
                change_file("permLog.txt", "yes")
                print("Restarting...")
                exit()
            else:
                print("permLog file already created!")
                print("Modifying file contents...")
                change_file("C:/xyCMD/permLog.txt", "yes")
                print("Restarting...")
                exit()


def list_cmd():
    print("Sort by an extension or type * for any extension, leave blank for folders or use exit to quit.")
    while True:
        sort = input(">>> ")
        if sort == "exit":
            break
        elif sort == "*":
            files = [File for File in os.listdir(dir_to_use) if not os.path.isdir(os.path.join(dir_to_use, File))]
            print(f"Here are the files in the current directory ({os.getcwd()}):")
            print(files)
        elif sort == "":
            folders = [folder for folder in os.listdir(dir_to_use) if os.path.isdir(os.path.join(dir_to_use, folder))]
            print(f"Here are the folders in the current directory ({os.getcwd()}):")
            print(folders)
        else:
            extension_files = [ext for ext in os.listdir(dir_to_use) if ext.endswith(sort)]
            print(f"Here are the files ending in {sort}: ")
            print(extension_files)


def read_path():
    path_to_read = input("What is the full PATH to the file? ")
    if os.path.exists(path_to_read):
        try:
            with open(path_to_read, "r") as file:
                ret = file.read()
                print("Reading the file:")
                print(ret)
                if log == "y":
                    logger.info(f"Read file successfully: {path_to_read}")
        except OSError as err:
            print(err)
            if log == "y":
                logger.error(f"An OS error has ocurred: {err}")
    else:
        print("The selected path does not exist or is mispelled.")
        if log == "y":
            logger.error(f"The selected path does not exist or is mispelled: {path_to_read}")


def read_dir():
    print("Be sure you are in the correct directory!")
    print("Current directory is", dir_to_use)
    print("Current text files in the directory are: ")
    text_files = [t for t in os.listdir(dir_to_use) if t.endswith(".txt")]
    print(text_files)
    extend = input("Do you want to extend the search for text files? (y/n) ")
    if extend == "y":
        print("Here are the .log, .docx and .pdf files in this directory:")
        log_files = [L for L in os.listdir(dir_to_use) if L.endswith(".log")]
        docx_files = [d for d in os.listdir(dir_to_use) if d.endswith(".docx")]
        pdf_files = [p for p in os.listdir(dir_to_use) if p.endswith(".pdf")]
        print(f"LOG files: {log_files}")
        print(f"DOCX files: {docx_files}")
        print(f"PDF files: {pdf_files}")
    open_this_txt = input("What is the file you want to open? ")
    if os.path.exists(os.path.join(dir_to_use, open_this_txt)):
        if os.path.isfile(os.path.join(dir_to_use, open_this_txt)):
            fname, file_ext = os.path.splitext(open_this_txt)
            if file_ext == '.txt' or file_ext == ".log" or file_ext == ".docx" or file_ext == ".pdf":
                try:
                    with open(os.path.join(dir_to_use, open_this_txt), 'r') as file:
                        ret = file.read()
                        print("Reading the file:")
                        print(ret)
                        if log == "y":
                            logger.info(f"Read file successfully: {open_this_txt}")
                except OSError as err:
                    print(err)
                    if log == "y":
                        logger.error(f"An OS error has ocurred: {err}")
            else:
                print("File extension is not .txt")
                logger.error(f"The specified item is not a .txt file: {open_this_txt}")
        else:
            print("The specified item is not a file.")
            logger.error(f"The specified item is not a file: {open_this_txt}")
    else:
        print("The specified item does not exist.")
        if log == "y":
            logger.error(f"The specified item does not exist: {open_this_txt}")


def back(child_dir):
    par_dir = os.path.dirname(child_dir)
    print("Went to parent directory: ", par_dir)
    return par_dir


def user():
    if os.name == "nt":
        if str(logged_in_user)[-1] == "s" or str(logged_in_user)[-1] == "S":
            print(f"Going to {logged_in_user}' user folder: C:\\Users\\{logged_in_user}")
            try:
                os.chdir(f"C:/Users/{logged_in_user}")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
        else:
            print(f"Going to {logged_in_user}'s user folder: C:\\Users\\{logged_in_user}")
            try:
                os.chdir(f"C:/Users/{logged_in_user}")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
    else:
        print("Currently only works on Windows (NT), sorry!")


def dl():
    if os.name == "nt":
        if str(logged_in_user)[-1] == "s" or str(logged_in_user)[-1] == "S":
            print(f"Going to {logged_in_user}' Downloads folder: C:\\Users\\{logged_in_user}\\Downloads")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Downloads")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
        else:
            print(f"Going to {logged_in_user}'s Downloads folder: C:\\Users\\{logged_in_user}\\Downloads")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Downloads")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
    else:
        print("Currently only works on Windows (NT), sorry!")


def pic():
    if os.name == "nt":
        if str(logged_in_user)[-1] == "s" or str(logged_in_user)[-1] == "S":
            print(f"Going to {logged_in_user}' Pictures folder: C:\\Users\\{logged_in_user}\\Pictures")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Pictures")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
        else:
            print(f"Going to {logged_in_user}'s Pictures folder: C:\\Users\\{logged_in_user}\\Pictures")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Pictures")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
    else:
        print("Currently only works on Windows (NT), sorry!")


def vid():
    if os.name == "nt":
        if str(logged_in_user)[-1] == "s" or str(logged_in_user)[-1] == "S":
            print(f"Going to {logged_in_user}' Videos folder: C:\\Users\\{logged_in_user}\\Videos")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Videos")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
        else:
            print(f"Going to {logged_in_user}'s Videos folder: C:\\Users\\{logged_in_user}\\Videos")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Videos")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
    else:
        print("Currently only works on Windows (NT), sorry!")


def doc():
    if os.name == "nt":
        if str(logged_in_user)[-1] == "s" or str(logged_in_user)[-1] == "S":
            print(f"Going to {logged_in_user}' Documents folder: C:\\Users\\{logged_in_user}\\Documents")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Documents")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
        else:
            print(f"Going to {logged_in_user}'s Documents folder: C:\\Users\\{logged_in_user}\\Documents")
            try:
                os.chdir(f"C:/Users/{logged_in_user}/Documents")
            except OSError as oserr:
                print(f"An error ocurred: {oserr}")
    else:
        print("Currently only works on Windows (NT), sorry!")


def open_path():
    path_to_open = input("What is the full PATH to the file? ")
    if os.path.exists(path_to_open):
        try:
            if os.path.isfile(path_to_open):
                print("Are you ABSOLUTELY SURE you want to open this file?")
                print("Opening random .EXEs can do some tough damage.")
                confirm = input("Type YES in capital letters to confirm you want to do this: ")
                if confirm == "YES":
                    print("Opening...")
                    subprocess.Popen([path_to_open], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print("Done! You can now continue with other tasks!")
                else:
                    print("Canceling the operation")
            else:
                print("The selected path does not lead to a .exe file")
                if log == "y":
                    logger.error(f"The selected path does not lead to a .exe file: {path_to_open}")
        except OSError as err:
            print(err)
            if log == "y":
                logger.error(f"An OS error has ocurred: {err}")
    else:
        print("The selected path does not exist or is mispelled.")
        if log == "y":
            logger.error(f"The selected path does not exist or is mispelled: {path_to_open}")


def open_dir():
    print("Be sure you are in the correct directory!")
    print("Current directory is", dir_to_use)
    print("Current executables in the directory are: ")
    exes = [exes for exes in os.listdir(dir_to_use) if exes.endswith(".exe")]
    print(exes)
    extended = input("Do you want to extend the search for executable files? (y/n) ")
    if extended == "y":
        print("Here are the .bat, .py, .pl, .rb, .js, .jar, .scr, .com, .vbs and .ps1 files in this directory:")
        bat_files = [other for other in os.listdir(dir_to_use) if other.endswith(".bat")]
        py_files = [other for other in os.listdir(dir_to_use) if other.endswith(".py")]
        pl_files = [other for other in os.listdir(dir_to_use) if other.endswith(".pl")]
        rb_files = [other for other in os.listdir(dir_to_use) if other.endswith(".rb")]
        js_files = [other for other in os.listdir(dir_to_use) if other.endswith(".js")]
        jar_files = [other for other in os.listdir(dir_to_use) if other.endswith(".jar")]
        scr_files = [other for other in os.listdir(dir_to_use) if other.endswith(".scr")]
        com_files = [other for other in os.listdir(dir_to_use) if other.endswith(".com")]
        vbs_files = [other for other in os.listdir(dir_to_use) if other.endswith(".vbs")]
        ps1_files = [other for other in os.listdir(dir_to_use) if other.endswith(".ps1")]
        print(f"Batch files: {bat_files}")
        print(f"Python files: {py_files}")
        print(f"Perl files: {pl_files}")
        print(f"Ruby files: {rb_files}")
        print(f"JavaScript files (Needs Node.js): {js_files}")
        print(f"Java Archive files: {jar_files}")
        print(f"Screensavers: {scr_files}")
        print(f"Command files: {com_files}")
        print(f"Visual Basic Script files: {vbs_files}")
        print(f"PowerShell scripts: {ps1_files}")
    exe_to_open = input("What is the file you want to open? ")
    if os.path.exists(os.path.join(dir_to_use, exe_to_open)):
        if os.path.isfile(os.path.join(dir_to_use, exe_to_open)):
            exe_name, file_ext = os.path.splitext(exe_to_open)
            try:
                if file_ext == ".exe" or file_ext == ".bat" or file_ext == ".py" or file_ext == ".pl" or file_ext == ".rb" or file_ext == ".js" or file_ext == ".jar" or file_ext == ".scr" or file_ext == ".com" or file_ext == ".vbs" or file_ext == ".ps1":
                    print("Are you ABSOLUTELY SURE you want to open this file?")
                    print("Opening random .EXEs can do some tough damage.")
                    confirm = input("Type YES in capital letters to confirm you want to do this: ")
                    if confirm == "YES":
                        print("Opening...")
                        subprocess.Popen([exe_to_open, dir_to_use], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    else:
                        print("Canceling the operation")
                else:
                    print("File extension is not .exe, .bat, .py, .pl, .rb, .js, .jar, .scr, .com, .vbs or .ps1.")
                    if log == "y":
                        logger.error(f"The specified item is not a .exe file: {exe_to_open}")
            except OSError as err:
                print(err)
                if log == "y":
                    logger.error(f"An OS error has ocurred: {err}")
        else:
            print("The specified item is not a file.")
            if log == "y":
                logger.error(f"The specified item is not a file: {exe_to_open}")
    else:
        print("The specified item does not exist.")
        if log == "y":
            logger.error(f"The specified item does not exist: {exe_to_open}")


def perm_log():
    print("Do you want to (q)uerry or (s)witch permanent logging?")
    permlog = input("(q/s): ")
    if permlog == "s":
        if os.path.exists("C:/xyCMD/permLog.txt"):
            try:
                with open(name_of_file, 'r') as file:
                    cont = file.read()
                    if cont == "yes":
                        change_file("C:/xyCMD/permLog.txt", "no")
                    else:
                        change_file("C:/xyCMD/permLog.txt", "yes")
            except OSError as err:
                print(f"Error reading file: {err}")
    elif permlog == "q":
        try:
            with open(name_of_file, 'r') as file:
                cont = file.read()
        except OSError as err:
            print(f"Error reading file: {err}")
        print(f"Permanent Logging is currently set to: {cont}")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def activate_power_mode():
    print("WARNING! PowerUser Mode allows executing (almost, basically, pretty much) ANY command!")
    print("This can be dangerous, so proceed with caution!")
    print("Enter 'XYCMD_POWER_MODE_CONFIRM' to activate or 'cancel' to exit.")
    confirmation = input("")
    if confirmation.upper() != "XYCMD_POWER_MODE_CONFIRM":
        print("PowerUser Mode canceled.")
        return
    print("PowerUser Mode active. Type 'exit' to return to normal xyCMD.")
    print("Some arguments are restricted for your safety.")
    while True:
        command = input("PowerUser > ")
        if command == "exit":
            break
        for arg in blocked_args:
            if arg in command:
                print("This command isn't currently supported for your safety. Certain arguments are blocked to prevent accidental data loss.")
                print()
                print("Here's how you can get help:")
                print()
                print("> Refer to the xyCMD GitHub repository for a list of blocked arguments: https://github.com/TheOneXylite/xyCMD")
                print("> Search online for the specific command and its safety implications.")
                print()
                print("If you believe this command is safe and should be considered for inclusion, you can")
                print("contact me via GitHub (comments, issues, whatever you want).")
        else:
            os.system(command)


def runtime():
    while True:
        print()
        choice = input("Command: ")
        print()

        if choice == "exit":
            print("See you later!")
            exit()

        elif choice == "help":
            print("Available Commands:")
            print("> exit: Exits the program;")
            print("> help: Shows this useful list of commands;")
            print("> ver: Shows some info about this project;")
            print("> change: Changes the directory to one of your choosing;")
            print("> back: Goes to the parent directory;")
            print("> cwd: Shows the current working directory;")
            print("> permLog: Querries or switches permanent logging;")
            print("> clear: Clears the command prompt;")
            print("> list:")
            print("     > FILES: Type * to list any file or filter by extension (.txt, .exe, etc...);")
            print("     > FOLDERS: Leave blank to list every subfolder in the current directory")
            print("> read: Reads a text file of your choosing;")
            print("> open: Opens an executable file of your choosing;")
            print()
            print("--- WINDOWS ONLY! ---")
            print()
            print("> user: Shows the currently logged in user (Might work on other OSes);")
            print("     > GO: Type \"user GO\" to go to the user folder;")
            print("> doc: Goes to the logged in user's Documents folder;")
            print("> pic: Goes to the logged in user's Pictures folder;")
            print("> vid: Goes to the logged in user's Videos folder;")
            print("> dl: Goes to the logged in user's Downloads folder;")

        elif choice == "change":
            change_to = input("Choose a directory to switch to or type \"cancel\" to cancel the operation: ")
            dir_to_change = change_dir(change_to)
            os.chdir(dir_to_change)

        elif choice == "back":
            os.chdir(back(os.getcwd()))

        elif choice == "cwd":
            print("This is the current directory:")
            print(os.getcwd())

        elif choice == "user":
            print(f"Currently logged in user: {logged_in_user}")
            print("Type \"user GO\" to go to the user folder!")

        elif choice == "user GO":
            user()

        elif choice == "doc":
            doc()

        elif choice == "dl":
            dl()

        elif choice == "pic":
            pic()

        elif choice == "vid":
            vid()

        elif choice == "list":
            list_cmd()

        elif choice == "read":
            print("Select one of the options below:")
            print("> Use file path;")
            print("> Choose file from current directory;")
            open_like_this = input("Do you want to use a PATH, current DIRectory or CANCEL? ")
            if open_like_this == "PATH":
                read_path()
            elif open_like_this == "DIR":
                read_dir()
            elif open_like_this == "CANCEL":
                print("Operation canceled.")
                if log == "y":
                    logger.info("Operation OPEN canceled.")
            else:
                print("Invalid method chosen.")
                if log == "y":
                    logger.error(f"Invalid method chosen for READ: {open_like_this}")

        elif choice == "open":
            print("Select one of the options below:")
            print("> Use file path;")
            print("> Choose file from current directory;")
            print("> Cancel the operation;")
            open_like_this = input("Do you want to use a PATH, current DIRectory or CANCEL? ")
            if open_like_this == "PATH":
                open_path()
            elif open_like_this == "DIR":
                open_dir()

        elif choice == "permLog":
            perm_log()

        elif choice == "clear":
            clear()

        elif choice == "ver":
            print(" ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,      |")
            print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     |")
            print("##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
            print("%%%%%%%..%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Version: xyCMD-v1.2")
            print("%%%%%%......%%%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Language: en-US")
            print("%%%%%%%%%.....%%%%%%%%%%%%%%%%%%%%%%%%%%     |  Python version: 3.8")
            print("%%%%%%%%%%%.....%%%%%%%%%%%%%%%%%%%%%%%%     |  Made by: Xylite")
            print("%%%%%%%%......%%%%%%%%%%%%%%%%%%%%%%%%%%     |")
            print("%%%%%%......%%%%%%%%...............%%%%%     |")
            print("%%%%%%%..%%%%%%%%%%%...............%%%%%     |")
            print(" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%      |")
            print("")

        elif choice == "TurnUpThePower":
            activate_power_mode()

        else:
            print("Invalid command entered.")
            print("Type \"help\" if you want a list of commands/options.")
            if log == "y":
                logger.error(f"Invalid command entered: {choice}")


def block_keyboardinterrupts():
    try:
        runtime()
    except KeyboardInterrupt:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("An error ocurred. Restarting...")
        time.sleep(1)
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
            startup()
        block_keyboardinterrupts()


startup()
block_keyboardinterrupts()
