# Clear console
print(end="\033c")

# Default modules
import os, sys

# Pip update
print("→[     ] Updating pip", end="\r")
if not os.system("pip install --upgrade pip >> NUL") == 0:
        print("×[EX004] > FATAL: Could not update \"pip\"")
        sys.exit(4)
print("√[DONE ]")

# Modules update
print("→[     ] Updating module \"colorama\"", end="\r")
if not os.system("pip install --upgrade colorama >> NUL") == 0:
    print("×[EX005] > FATAL: Could not update \"colorama\"")
    sys.exit(5)
print("√[DONE ]")
print("→[     ] Updating module \"cursor\"", end="\r")
if not os.system("pip install --upgrade cursor >> NUL") == 0:
    print("×[EX007] > FATAL: Could not update \"cursor\"")
    sys.exit(7)
print("√[DONE ]")

# Modules failcheck and import
print("→[     ] Importing module \"colorama\"", end="\r")
try:
    import colorama
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    if not os.system("pip install colorama >> NUL") == 0:
        print("×[EX002] > FATAL: Could not import \"colorama\"")
        sys.exit(2)
    import colorama
    from colorama import Fore, Back, Style
print("√[DONE ]")
print("→[     ] Importing module \"cursor\"", end="\r")
try:
    import cursor
except ModuleNotFoundError:
    if not os.system("pip install cursor >> NUL") == 0:
        print("×[EX008] > FATAL: Could not import \"cursor\"")
        sys.exit(8)
    import cursor
print("√[DONE ]")
print("→[     ] Importing module \"time\"", end="\r")
try:
    import time
except ModuleNotFoundError:
    if not os.system("pip install time >> NUL") == 0:
        print("×[EX011] > FATAL: Could not import \"time\"")
        sys.exit(11)
    import time
print("√[DONE ]")

# Module Initialization
print("→[     ] Initializing module \"colorama\"", end="\r")
try:
    colorama.init()
except:
    print("×[EX009] > FATAL: Could not initialize \"colorama\"")
    sys.exit(9)
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")
print("→[     ] Initializing module \"cursor\"", end="\r")
try:
    cursor.hide()
except:
    print("×[EX010] > FATAL: Could not initialize \"cursor\"")
    sys.exit(10)
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")

# Importing data.py
print(f"{Fore.CYAN}→{Fore.WHITE}[     ] {Fore.YELLOW}Importing local file \"data.py\"{Fore.WHITE}", end="\r")
try:
    import data
except ModuleNotFoundError:
        print(f"{Fore.RED}×{Fore.WHITE}[{Fore.RED}EX003{Fore.WHITE}] > {Fore.RED}FATAL{Fore.WHITE}: {Fore.YELLOW}Could not initialize local file \"data.py\"")
        sys.exit(3)
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")

# data.py integrity check
print(f"{Fore.CYAN}→{Fore.WHITE}[     ] {Fore.YELLOW}Verifying integrity of \"data.py\"{Fore.WHITE}", end="\r")
try:
    data.ver
    data.runtime.error
    data.pc
    data.users
    data.passw
    data.llv
    data.user
    data.dir
    data.ilv
    data.lv
except AttributeError:
        print(f"{Fore.RED}×{Fore.WHITE}[{Fore.RED}EX006{Fore.WHITE}] > {Fore.RED}FATAL{Fore.WHITE}: {Fore.YELLOW}\"data.py\" is corrupted ")
        sys.exit(3)
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")

# Configuration
print(f"{Fore.CYAN}→{Fore.WHITE}[     ] {Fore.YELLOW}Configuring Cybertex{Fore.WHITE}", end="\r")
os.chdir(os.path.join(os.path.abspath(os.path.curdir), os.path.expanduser("~")))
data.dir = os.path.expanduser("~")
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")
print(f"{Fore.CYAN}→{Fore.WHITE}[     ] {Fore.YELLOW}Starting Cybertex{Fore.WHITE}", end="\r")
print(f"{Fore.GREEN}√{Fore.WHITE}[{Fore.GREEN}DONE {Fore.WHITE}]")

# Finalization
print(end="\033c")
print(f"Cybertex V{data.ver}")

# Commands
try:
    while not data.runtime.error:
        cursor.show()
        cmd = input(f"{Style.RESET_ALL}{Fore.CYAN}╭──╴[{Fore.GREEN}{data.pc} {Fore.CYAN}● {Fore.GREEN}{data.user}{Fore.CYAN}] {Fore.MAGENTA}{data.dir} {Fore.YELLOW}#\n{Style.RESET_ALL}{Fore.CYAN}╰╴{Fore.MAGENTA}{data.lv} {Fore.GREEN}→ {Fore.YELLOW}")
        cmd = cmd.split(" ")
        print(Style.RESET_ALL)
        cursor.hide()
        if cmd[0] == "" and len(cmd) == 1:
            pass
        elif cmd[0] in ["usradd", "useradd"]:
            if not data.ilv == 2:
                print(f"{Fore.RED}{cmd[0]} > you don't have the privileges to run this command (yours: {data.ilv}, needed: 2 or higher)\n")
                continue
            try:
                usrname = cmd[1]
            except IndexError:
                print(f"{Fore.RED}{cmd[0]} > missing argument 1\n")
                continue
            try:
                usrpwrd = cmd[2]
            except IndexError:
                print(f"{Fore.YELLOW}{cmd[0]} > missing argument 2 \"password\", setting to empty\n")
                usrpwrd = ""
            try:
                usrllv = int(cmd[3])
            except IndexError:
                print(f"{Fore.YELLOW}{cmd[0]} > missing argument 3 \"level\", setting to 0\n")
                usrllv = 0
            except ValueError:
                print(f"{Fore.RED}{cmd[0]} > expected number in argument 3 \"level\"\n")
                continue
            if not usrllv in [0, 1, 2]:
                print(f"{Fore.RED}{cmd[0]} > argument 3 \"level\" must be 0, 1 or 2\n")
                continue
            if usrname in data.users:
                print(f"{Fore.RED}{cmd[0]} > user \"{usrname}\" already exists\n")
                continue
            data.users.append(usrname)
            data.passw.append(usrpwrd)
            if usrllv == 0: usrlv = "base"
            if usrllv == 1: usrlv = "user"
            if usrllv == 2: usrlv = "root"
            data.llv.append([usrllv, usrlv])
        elif cmd[0] == "cd":
            try:
                os.chdir(os.path.join(os.path.abspath(os.path.curdir), os.path.expanduser(cmd[1])))
            except IndexError:
                pass
            except FileNotFoundError:
                if not ("--secret" in cmd and cmd[1] == "mg"):
                    print(f"{Fore.RED}cd > \"{cmd[1]}\" is missing")
                else:
                    print(f"{Fore.RED}c{Fore.YELLOW}d{Fore.GREEN} > {Fore.CYAN}\"{Fore.BLUE}m{Fore.MAGENTA}g{Fore.RED}\"{Fore.YELLOW} i{Fore.GREEN}s{Fore.CYAN} m{Fore.BLUE}i{Fore.MAGENTA}s{Fore.RED}s{Fore.YELLOW}i{Fore.GREEN}n{Fore.CYAN}g")
            except NotADirectoryError:
                print(f"{Fore.RED}cd > \"{cmd[1]}\" is not a folder")
        elif cmd[0] == "chuser":
            try:
                if cmd[1] in data.users and not cmd[1] == data.user:
                    cursor.show()
                    while True:
                        try:
                            if data.passw[data.users.index(cmd[1])] == "":
                                print(f"{Style.RESET_ALL}Password for \"{cmd[1]}\": {Fore.CYAN}Skipped [empty]")
                                data.user = cmd[1]
                                data.ilv = data.llv[data.users.index(cmd[1])][0]
                                data.lv = data.llv[data.users.index(cmd[1])][1]
                                break
                            if input(f"{Style.RESET_ALL}Password for \"{cmd[1]}\": {Fore.YELLOW}") == data.passw[data.users.index(cmd[1])]:
                                data.user = cmd[1]
                                data.ilv = data.llv[data.users.index(cmd[1])][0]
                                data.lv = data.llv[data.users.index(cmd[1])][1]
                                break
                        except KeyboardInterrupt:
                            print(end="\n")
                            break
                    cursor.hide()
                elif cmd[1] == data.user:
                    print(f"{Fore.RED}chuser > you are already using this user")
                else:
                    print(f"{Fore.RED}chuser > user not found")
            except IndexError:
                print(f"{Fore.RED}chuser > missing username")
        elif cmd[0] in ["cls", "clr", "clear"]:
            print(end="\033c")
        elif cmd[0] == "exit":
            print(end="\033c")
            sys.exit(0)
        elif cmd[0] == "ls":
            dir = ""
            for file in os.listdir():
                if (not file.startswith(".")) or "-h" in cmd:
                    if os.path.isfile(file):
                        dir += f"{Fore.WHITE}{file} {Fore.GREEN}● {Fore.WHITE}"
                    else:
                        dir += f"{Fore.YELLOW}{file} {Fore.GREEN}● {Fore.WHITE}"
            dir = dir[0:-13]
            print(dir)
        elif cmd[0] in ["usrlist", "userlist", "usrls", "userls"]:
            usrlist = ""
            for user in data.users:
                usrlist += f"{Fore.MAGENTA}{data.llv[data.users.index(user)][0]} {data.llv[data.users.index(user)][1]}{Fore.YELLOW} @ {Fore.GREEN}{user}\n"
            usrlist = usrlist[0:-1]
            print(usrlist)
        elif cmd[0] == "whoami":
            print(data.user)
        else:
            print(f"{Fore.RED}Missing command \"{cmd[0]}\"")
        data.dir = os.getcwd()
        print(end="\n")
        
except KeyboardInterrupt:
    print(Style.RESET_ALL, end="\n")
    cursor.show()