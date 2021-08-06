import time
import os
import subprocess


def home(user):
    commands = f"""
Welcome back '{user}'!
1) Add a new preset\n2) Remove a preset\n3) Activate Presets\n4) View All presets
5) Change mouse sensitivity (N/A)\n6) Keybinds (N/A)\n7) Log out"""

    print(commands)
    getcommand = input("$ ")

    if getcommand == '5' or getcommand == '6':
        print("That command isn't available yet! Try checking out the latest version on github")
        print("https://github.com/Whitelisted1/SettingsPresets")
        print("")
        home(user)

    elif getcommand == '6':
        pass

    elif getcommand == '4':
        f = open(f"{user}/games.txt", "r")
        directories = f.read()
        files = directories.split()
        f.close()

        print("All files:")
        if len(files) != 0:
            for i in range(len(files)):
                file = files[i]
                filename = file.split('/')
                filename = filename[-1]  # Get file name
                print(f'{i+1}: {filename}')
            home(user)
        else:
            print("No files to show")
            home(user)

    elif getcommand == '7':
        print("")
        loginsignup()

    elif getcommand == '3':
        gamesettings = open(f"{user}/games.txt", "r")
        settingsdir = gamesettings.read()
        gamesettings.close()
        if settingsdir == '':
            print("No presets to activate")
            home(user)
        allsettings = settingsdir.split()

        for i in range(len(allsettings)):
            settingFile = allsettings[i]
            filename = settingFile.split('/')
            filename = filename[-1]

            settingsfile = open(f"{user}/{filename}", "r")
            filesettings = settingsfile.read()
            settingsfile.close()

            copySFile = open(f"{settingFile}", "w")
            copySFile.truncate(0)
            copySFile.write(filesettings)
            copySFile.close()
            print(f"Restored settings for {filename}")
        home(user)

    elif getcommand == '2':

        deleteDir = open(f"{user}/games.txt", "r")
        Dirs = deleteDir.read()
        AllDirs = Dirs.split()
        deleteDir.close()

        if len(AllDirs) == 0:
            print("No presets are available")
            home(user)
        else:
            menu = ''
            i = 0
            for i in range(len(AllDirs)):
                i += 1
                menu = menu + f'{i}) {AllDirs[i - 1]}\n'
            menu = menu + f'{i + 1}) Back'
            print(menu)
            exitMenu = i+1
            str(exitMenu)
            selectedDir = input("$ ")
            try:
                selectedDir = int(selectedDir)
            except ValueError:
                print("That's not a number!")
                home(user)
            if selectedDir == int(exitMenu):
                home(user)
            elif int(selectedDir) > int(len(AllDirs)) or int(selectedDir) < 1:
                print("That's not a correct value")
                home(user)

            DeletedDir = AllDirs[int(selectedDir) - 1]
            AllDirs.remove(DeletedDir)
            notDeletedDir = ''

            for i in range(len(AllDirs)):
                addDir = AllDirs[i]
                notDeletedDir += f'\n{addDir}'

            f = open(f"{user}/games.txt", 'w')
            f.truncate(0)
            f.write(notDeletedDir)
            f.close()
            print(f"Removed {DeletedDir}")
            home(user)

    elif getcommand == '1':
        print("Please enter the directory to the settings file, or type 'exit' to go back")
        print("Please note that you CANNOT have an options file that contians a space, it will return an error")
        # Will be fixed in an update
        directory = input("$ ")

        f = open(f"{user}/games.txt", "r")
        allDirs = f.read()
        checkSettings = allDirs.split()
        f.close()

        if directory == 'exit':
            home(user)
        else:

            try:
                filename = directory.split('/')
                filename = filename[-1]  # Get file name

                settingsfile = open(f"{directory}", "r")
                filesettings = settingsfile.read()
                settingsfile.close()

                copySFile = open(f"{user}/{filename}", "w")
                copySFile.truncate(0)
                copySFile.write(filesettings)
                copySFile.close()

                if directory in checkSettings:
                    print("That directory is already taken!")
                else:
                    gameFile = open(f"{user}/games.txt", 'a')
                    gameFile.write(f"\n{directory}")
                    gameFile.close()
                    print("Finished creating presets (May have overwritten other settings)")
            except FileNotFoundError:
                print("File not found")
                home(user)
            home(user)
    else:
        print("Invalid input!")
        home(user)


def delete():  # add confirmation to delete
    f = open(f"users.txt", "r")
    users = f.read()
    f.close()
    if users != '':
        users = users.split()
        i = 0
        menu = ""
        numberOfUsers = len(users)
        print("\nType the number of the user you would like to delete ('Exit' to logout)")
        for i in range(numberOfUsers):
            i += 1
            menu = menu + f'{i}) {users[i - 1]}\n'
        menu = menu + f'{i + 1}) Back'
        print(menu)
        choice = input("\r$ ")
        try:
            choice = int(choice)
        except ValueError:
            print("That is not a number!\n")
            loginsignup()
        Back = numberOfUsers + 1
        int(Back)

        if choice > Back or choice < 1:
            print("That is not a valid user!")
            login()

        elif str(choice) == f'{str(Back)}':
            print("Going back to home...\n")
            loginsignup()

        else:
            selectedUser = users[int(choice - 1)]
            print(f"Confirm the deletion of {selectedUser}?\n1) Yes\n2) No")
            confirm = input("$ ")
            try:
                confirm = int(confirm)
            except ValueError:
                print("That is not a valid number!")
                loginsignup()
            if confirm == 2:
                print("Canceled deletion\n")
                loginsignup()
            elif confirm == 1:
                selectedUser = users[int(choice - 1)]
                users.remove(selectedUser)
                notDeletedUser = ''

                for i in range(len(users)):
                    addUser = users[i]
                    notDeletedUser += f'\n{addUser}'

                f = open(f"users.txt", "w")
                f.truncate(0)
                f.write(notDeletedUser)
                f.close()

                if os.path.isdir(f"{selectedUser}") is True:
                    if len(os.listdir(f'{selectedUser}')) == 0:
                        os.system(f"rmdir {selectedUser}")
                    else:
                        listFiles = subprocess.getoutput(f'ls {selectedUser}')
                        files = listFiles.split()

                        os.chdir(f'{selectedUser}')
                        for i in range(len(files)):
                            os.system(f'rm {files[i]}')
                        dir_path = os.path.dirname(os.path.realpath(__file__))
                        os.chdir(dir_path)
                        os.system(f'rmdir {selectedUser}')

                print(f'Successfully deleted profile \'{selectedUser}\'\n')
                loginsignup()
            else:
                print("That is not a choice!")
                loginsignup()

    else:
        print("No users are available...\n")
        loginsignup()


def login():
    f = open(f"users.txt", "r")
    users = f.read()
    f.close()
    if users != '':
        users = users.split()
        i = 0
        menu = ""
        numberOfUsers = len(users)
        print("\nType the number of the user you would like to login as ('Exit' to cancel)")
        while i < numberOfUsers:
            i += 1
            menu = menu + f'{i}) {users[i-1]}\n'
        menu = menu + f'{i+1}) Exit'
        print(menu)
        choice = input("\r$ ")
        try:
            choice = int(choice)

        except ValueError:
            print("That is not a number!")
            login()

        exitchoice = numberOfUsers+1
        int(exitchoice)

        if choice > exitchoice or choice < 1:
            print("That is not a valid user!")
            login()

        elif str(choice) == f'{str(exitchoice)}':
            print("Going to main menu...\n")
            loginsignup()

        else:
            selectedUser = users[int(choice-1)]
            home(selectedUser)

    else:
        print("No users are available...\n")
        loginsignup()


def signup():
    print("\nEnter your username (spaces are not allowed)")
    print("Or enter 'exit' to go to menu")
    username = input("$ ")

    if username == 'exit':
        print("Going to log in screen...\n")
        loginsignup()
    if ' ' in username or 'exit' in username.lower():
        print("Illegal Character! Start again")
        signup()
    if len(username) > 16:
        print("Too many characters!")
        signup()
    elif len(username) < 3:
        print("Not enough characters!")
        signup()
    else:
        print("Creating account..")

        readUsers = open("users.txt", 'r')
        users = readUsers.read()
        readUsers.close()

        testUsers = users.lower()
        testUsers = testUsers.split()

        if username.lower() in testUsers:
            print("Creation failed! Another profile already exists with that username")
            time.sleep(1.5)
            signup()

        os.system(f"mkdir {username}")
        os.system(f"cd {username}\n>games.txt")

        addUser = open("users.txt", 'w')
        addUser.truncate(0)
        addUser.write(f'{users}\n{username}')
        addUser.close()
        print("Successfully created account\n")
        loginsignup()


def loginsignup():
    print("Type the number of the option you would like to select")
    print("1) Login\n2) Signup\n3) Delete a profile\n4) Exit Program")
    loginSignup = input("$ ")
    loginSignup.lower()

    if loginSignup == '1' or loginSignup == 'login':
        login()
    elif loginSignup == '2' or loginSignup == 'signup':
        signup()
    elif loginSignup == '3' or loginSignup == 'delete':
        delete()
    elif loginSignup == '4' or loginSignup == 'exit':
        print("Exiting program...")
        exit()
    else:
        print("That is an invalid value, please try again\n")
        loginsignup()


if __name__ == "__main__":
    print("This isn't the file to run! Please run 'main.py'")
    input("Press enter to exit file")
