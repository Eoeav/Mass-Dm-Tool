import requests
import time
from colorama import Fore, init




rs = requests.Session()
def mass_dm():
    init()

    print(Fore.GREEN)
    print("""
                            .d8888b.  888                   888      
                            d88P  Y88b 888                   888      
                            Y88b.      888                   888      
                            "Y888b.   888  8888b.  .d8888b  88888b.  
                                "Y88b. 888     "88b 88K      888 "88b 
                                "888 888 .d888888 "Y8888b. 888  888 
                            Y88b  d88P 888 888  888      X88 888  888 
                            "Y8888P"  888 "Y888888  88888P' 888  888 
    """)
    #ui fixes this shit

    print("Mass DMER Made By Eoeav!/Shasher!")
    print("Helped By Ui & Satzzz")

    print(Fore.RED)
    token = input("Enter Token: ")
    message = input('Message: ')
    headers = {"authorization": token, "user-agent": "Mozilla/5.0"}

    reqmas = rs.get(
        "https://discord.com/api/v9/users/@me/channels", headers=headers
    ).json()
    for chen in reqmas:
        json = {"content": message}
        time.sleep(1)
        rs.post(
            f"https://discord.com/api/v9/channels/{chen['id']}/messages",
            headers=headers,
            data=json,
        )
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} {chen['id']} Sent")

mass_dm()
