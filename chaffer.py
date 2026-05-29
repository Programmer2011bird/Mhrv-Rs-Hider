from colorama import init, Fore
import requests
import random 
import time 


init(autoreset=True)

internal_sites: list[str] = [
    "https://web.eitaa.com/",
    "https://www.digikala.com/",
    "https://divar.ir/",
    "https://toplearn.com/",
    "https://rubika.ir/",
    "https://www.tgju.org/"
]


def main():
    while True:
        site = random.choice(internal_sites)
    
        try: 
            REQUEST = requests.head(site)

            print(f"{Fore.CYAN}{site}  :  {Fore.GREEN}{REQUEST.status_code}")
    
        except:
            pass
    
        time.sleep(random.randint(10, 60))

if __name__ == "__main__":
    main()
