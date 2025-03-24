import requests
from colorama import Fore, Style
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
def send_sms():
    print(f"""{blue}
███████╗██████╗ ███████╗███████╗    ███████╗███╗   ███╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔════╝████╗ ████║██╔════╝
█████╗  ██████╔╝█████╗  █████╗      ███████╗██╔████╔██║███████╗
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝      ╚════██║██║╚██╔╝██║╚════██║
██║     ██║  ██║███████╗███████╗    ███████║██║ ╚═╝ ██║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝     ╚═╝╚══════╝
                 {white}Free sms by Jovan Reguya                                             
""")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    number = input(f"{green}📞 Enter the phone number: ")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    text = input(f"{white}💬 Enter the message: ")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    
    url = f"https://haji-mix.up.railway.app/api/lbcsms?text={text}&number={number}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            message = f"{green}✅ Message sent successfully!"
            width = len(message) + 4
            print(Fore.GREEN + "┌" + "─" * width + "┐")
            print("│ " + message + " │")
            print("└" + "─" * width + "┘" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"❌ Failed to send message. Status code: {response.status_code}" + Style.RESET_ALL)
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"⚠️ An error occurred: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    send_sms()
