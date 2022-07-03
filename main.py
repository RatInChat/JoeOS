import sys
import time
from os import system, name
from random import randrange

user = "guest"
search = ""
downloaded_apps = ["gc", "djbw", "jc"]
apps_list = ["GJoogle CJrome", "Dark Joe Bama Web", "Joecord", "Joe Software", "Delete Software"]
apps_deleteable = ["GJoogle CJrome", "Dark Joe Bama Web", "Joecord"]
apps_downloadable = ["Terminal", "JoeTube"]
count = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def loading():
    print("Loading:")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    clear()


def download_animation():

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


loading()


def loading2():
    animation = "|", "/", "-", "\\", "|", "/", "-", "\\", "|", "/", "-", "\\", "|", "/", "-", "\\"
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    clear()


def intro():
    print("\r Welcome to: ")
    print("             _        _            _               _            _        \n"
          "                /\ \     /\ \         /\ \            /\ \         / /\      \n"
          "                \ \ \   /  \ \       /  \ \          /  \ \       / /  \     \n"
          "                /\ \_\ / /\ \ \     / /\ \ \        / /\ \ \     / / /\ \__  \n"
          "               / /\/_// / /\ \ \   / / /\ \_\      / / /\ \ \   / / /\ \___\ \n"
          "      _       / / /  / / /  \ \_\ / /_/_ \/_/     / / /  \ \_\  \ \ \ \/___/ \n"
          "     /\ \    / / /  / / /   / / // /____/\       / / /   / / /   \ \ \       \n"
          "     \ \_\  / / /  / / /   / / // /\____\/      / / /   / / /_    \ \ \      \n"
          "     / / /_/ / /  / / /___/ / // / /______     / / /___/ / //_/\__/ / /      \n"
          "    / / /__\/ /  / / /____\/ // / /_______\   / / /____\/ / \ \/___/ /       \n"
          "    \/_______/   \/_________/ \/__________/   \/_________/   \_____\/        \n"
          "                                                                             ")


intro()
time.sleep(1)
clear()
loading2()


def version():
    print(""" __      __           _               __ 
 \ \    / /          (_)             /_ |
  \ \  / /__ _ __ ___ _  ___  _ __    | |
   \ \/ / _ \ '__/ __| |/ _ \| '_ \   | |
    \  /  __/ |  \__ \ | (_) | | | |  | |
     \/ \___|_|  |___/_|\___/|_| |_|  |_|
                                         
                                         """)


version()
time.sleep(2)
clear()


def login():
    print("""  _    _                                                     
 | |  | |                                                 _  
 | |  | | ___   ___  _ __  _ __    __ _  _ __ ___    ___ (_) 
 | |  | |/ __| / _ \| '__|| '_ \  / _` || '_ ` _ \  / _ \    
 | |__| |\__ \|  __/| |   | | | || (_| || | | | | ||  __/ _  
  \____/ |___/ \___||_|   |_| |_| \__,_||_| |_| |_| \___|(_) 
                                                             
                                                            """)
    user = input("> ")
    print("""  _____                                           _    
 |  __ \                                         | | _ 
 | |__) |__ _  ___  ___ __      __ ___   _ __  __| |(_)
 |  ___// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` |   
 | |   | (_| |\__ \\\\__ \ \ V  V /| (_) || |  | (_| | _ 
 |_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|(_)
                                                       
                                                       """)
    input("> ")
    print("Logging you in....")
    loading()
    succsess()


def guest():
    time.sleep(1)
    clear()
    print("""  _                           _                 
 | |                         (_)                
 | |      ___    __ _   __ _  _  _ __    __ _   
 | |     / _ \  / _` | / _` || || '_ \  / _` |  
 | |____| (_) || (_| || (_| || || | | || (_| |  
 |______|\___/  \__, | \__, ||_||_| |_| \__, |  
 (_)             __/ |  __/ |            __/ |  
  _  _ __       |___/  |___/__ _  ___   |___/   
 | || '_ \                 / _` |/ __|          
 | || | | |               | (_| |\__ \          
 |_||_| |_|                \__,_||___/          
                              _    _            
                             | |  | |           
      __ _  _   _   ___  ___ | |_ | |           
     / _` || | | | / _ \/ __|| __|| |           
    | (_| || |_| ||  __/\__ \| |_ |_|           
     \__, | \__,_| \___||___/ \__|(_)           
      __/ |                                     
     |___/                                      """)
    loading()
    succsess()


def account():
    print("                 \n"
          " |  __ \        \ \   / /          | |  | |                \n"
          " | |  | | ___    \ \_/ /__  _   _  | |__| | __ ___   _____ \n"
          " | |  | |/ _ \    \   / _ \| | | | |  __  |/ _` \ \ / / _ \\\n"
          " | |__| | (_) |    | | (_) | |_| | | |  | | (_| |\ V /  __/\n"
          " |_____/ \___/     |_|\___/ \__,_| |_|  |_|\__,_| \_/ \___|\n"
          "       /\          | |                                     \n"
          "      /  \         | | ___   ___                           \n"
          "     / /\ \    _   | |/ _ \ / _ \                          \n"
          "    / ____ \  | |__| | (_) |  __/       _  ___             \n"
          "   /_/   /\_\  \____/ \___/ \___|      | ||__ \            \n"
          "        /  \   ___ ___ ___  _   _ _ __ | |_  ) |           \n"
          "       / /\ \ / __/ __/ _ \| | | | '_ \| __|/ /            \n"
          "      / ____ \ (_| (_| (_) | |_| | | | | |_|_|             \n"
          "     /_/    \_\___\___\___/ \__,_|_| |_|\__(_)             \n"
          "                   __         __  __                       \n"
          "                  / /        / /  \ \                      \n"
          "                 | |_   _   / / __ | |                     \n"
          "                 | | | | | / / '_ \| |                     \n"
          "                 | | |_| |/ /| | | | |                     \n"
          "                 | |\__, /_/ |_| |_| |                     \n"
          "                  \_\__/ |        /_/                      \n"
          "                    |___/                                  ")
    status = input("> ")
    if status.lower() == "y":
        clear()
        login()
    else:
        clear()
        print("Log in as guest? (y/n)")
        log_guest = input("> ")
        if log_guest == "y":
            guest()
        elif log_guest == "n":
            print("Well bai.")
            time.sleep(1)
        else:
            print("Please put in a valid answer.")
            account()


def succsess():
    print("""                                          __         _  _          
                                         / _|       | || |         
  ___  _   _   ___  ___   ___  ___  ___ | |_  _   _ | || | _   _   
 / __|| | | | / __|/ __| / _ \/ __|/ __||  _|| | | || || || | | |  
 \__ \| |_| || (__ \__ \|  __/\__ \\\\__ \| |  | |_| || || || |_| |  
 |___/ \__,_| \___||___/ \___||___/|___/|_|   \__,_||_||_| \__, |  
                                                            __/ |  
  _                                 _            _         |___/   
 | |                               | |          (_)       | |      
 | |  ___    __ _   __ _   ___   __| |           _  _ __  | |      
 | | / _ \  / _` | / _` | / _ \ / _` |          | || '_ \ | |      
 | || (_) || (_| || (_| ||  __/| (_| |          | || | | ||_|      
 |_| \___/  \__, | \__, | \___| \__,_|          |_||_| |_|(_)      
             __/ |  __/ |                                          
            |___/  |___/                                           """)

    time.sleep(2)
    clear()
    apps()


def apps():
    clear()
    print("Your apps: ")
    for app in apps_list:
        time.sleep(0.5)
        print(app)
    print("What do you want to open? (use exact name!)")
    app_gui()


def app_gui():
    search = input("> ")
    if search == "GJoogle CJrome" or search.lower() == "gc" and apps_deleteable.count("GJoogle CJrome") > 0:
        loading()
        print("Welcome to GJoogle CJrome!")
        print("(The best browser there is!)")
        print("")
        print("")
        gjoogles = input("Search: ")
        time.sleep(1)
        print("No.")
        apps()
    elif search == "Dark Joe Bama Web" or search.lower() == "djbw" and apps_deleteable.count("Dark Joe Bama Web") > 0:
        loading()
        print("Welcome to Dark Joe Bama Web!")
        print("(The best dark there is!)")
        print("")
        print("")
        darksearch = input("Search: ")
        joe_hack()
    elif search == "Joecord" or search.lower() == "jc" and apps_deleteable.count("Joecord") > 0:
        print("Joecord is closed today sorry!")
        time.sleep(1)
        apps()
    elif search == "Terminal" or search.lower() == "Ter" and apps_deleteable.count("Terminal") > 0:
        print("Put your code in here!")
        code_block = input("> ")
        print("Invalid Syntax!")
        time.sleep(2)
        apps()
    elif search == "JoeTube" or search.lower() == "jt" and apps_deleteable.count("JoeTube") > 0:
        print("No videos here!")
        time.sleep(2)
        apps()

    elif search == "Joe Software":
        loading()
        print("Welcome to Joe Software!")
        time.sleep(1)
        download_place()
    elif search == "Delete Software":
        del_software()

    else:
        print("App does not exist or is not downloaded. Try another one! (use exact name!)")
        apps()


def del_software():
    if len(apps_deleteable) > 0:
        for app in apps_deleteable:
            print(f"\nDo you want to delete {app}?")
            sure = input("> ")
            if sure.lower() == "y":
                print("Deleting...")
                download_animation()
                apps_downloadable.append(f"{app}")
                apps_deleteable.remove(f"{app}")
                apps_list.remove(f"{app}")  # sigh why do I have to make these things so complicated?
                del_software()
            elif sure.lower() == "n":
                time.sleep(1)
                print("There is no other option than yes.")
                time.sleep(1)
                del_software()
            else:
                print("Invalid Argument!")
                time.sleep(1)
                del_software()
            apps()
    else:
        print("\nNo apps to delete :(")
        time.sleep(2)
        apps()


def joe_hack():
    print("WARNING: Without JoeProtection on you will get hacked!")
    ok = input("Turn JoeProtection on? (y/n): ")
    if ok.lower() == "y":
        print("Turning on JoeProtection...")
        loading2()
        print("JoeProtection ON!")
        time.sleep(1)
        print("Continuing with your search...")
        time.sleep(1)
        results = randrange(10000, 1000000)
        print(f"Found {results} results!!")
        time.sleep(1)
        print("That was fast right?")
        time.sleep(1)
        print("Rate us 5 stars!")
        time.sleep(1)
        print("Here are your results...")
        time.sleep(3)
        print("SORRY FOR INTERRUPTION!")
        time.sleep(1)
        print("BUT YOU ARE BEING HACKED BECAUSE JOEPROTECTION SUCKS!!!!!")
        i = 0
        while i < 5:
            print("*SKULL*")
            i += 1
        time.sleep(3)
        print("JoeProtection has exited you from the app so that you would not get hacked! Rate us 5 stars!")
        time.sleep(3)
        apps()
    elif ok.lower() == "n":
        print("We will not allow you to continue without JoeProtection!")
        time.sleep(2)
        joe_hack()
    else:
        print("It's only y or n. Try again.")
        joe_hack()

# I think this was less efficient than the other download place...
# def download_place(download):
#     if download == "Terminal" or download == "ter":
#         print("Downloading Terminal...")
#         download_animation()
#         apps_list.insert(-2, "Terminal")
#         apps_downloadable.remove("Terminal")
#         apps_deleteable.append("Terminal")
#         apps()
#     elif download == "JoeTube" or download == "jt":
#         print("Downloading JoeTube...")
#         download_animation()
#         apps_list.insert(-2, "JoeTube")
#         apps_downloadable.remove("JoeTube")
#         apps_deleteable.append("JoeTube")
#         apps()

# more complicated but more efficient


def download_place():
    if len(apps_downloadable) > 0:
        not_want_app_list = []
        for app in apps_downloadable:
            if not_want_app_list.count(app) == 0:
                print(f"\nDo you want to download {app}")
                does_he = input("> ")
                if does_he.lower() == "y":
                    print(f"Downloading {app}...")
                    download_animation()
                    apps_list.insert(-2, f"{app}")
                    apps_downloadable.remove(f"{app}")
                    apps_deleteable.append(f"{app}")
                    download_place()
                elif does_he.lower() == "n":
                    print("There is not other option than yes.")
                    download_place()
                else:
                    print("Bruh. Invalid!")
                    download_place()
            else:
                pass
    else:
        print("\nNo more apps to download :(")
        time.sleep(2)
        apps()


account()
