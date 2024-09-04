import builtwith
import webbrowser
import pyfiglet 
from termcolor import colored

# Display banner
banner = colored(pyfiglet.figlet_format("BAD SERVER", font="banner3-D"), "light_red")
print(banner)

# Menu function
def menu():
    print("   -g / --git >>> github")
    print("   -u / --url >>> url target")
    print("   -a / --about >>> about this tool")
    print("   -h / --help >>> help")

menu()

# Get command from user
command = input(colored("|__> enter your command : ", "cyan"))

command = command.split(" ")

if command[0] == "-u" or command[0] == "--url":
    url = command[-1]
    result = builtwith.builtwith(url)
    
    for key, value in result.items():
        value = str(value)
        value = value.replace("[", "")
        value = value.replace("]", "")
        print("\n", key, " : ", value, "\n")

elif command[0] == "-g" or command[0] == "--git":
    webbrowser.open("https://github.com/pop-hacker313")

elif command[0] == "-a" or command[0] == "--about":
    webbrowser.open("https://github.com/pop-hacker313")

elif command[0] == "-h" or command[0] == "--help":
	menu()

else:
    print(colored("warning !", "yellow"))
    
input()