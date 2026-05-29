from colorama import init, Fore
import multiprocessing
import subprocess
import time 
import sys
import os


init(autoreset=True)


def parse_arguments():
    args = {}
    for arg in sys.argv[1:] :
        if "=" in arg:
            key, value = arg.split("=", 1)
            args[key] = value

    return args

def timer(t:int= 15*60):
    print(f"{Fore.YELLOW}timer started")
    time_to_run = t
    
    while time_to_run >= 0:
        time.sleep(1)
        time_to_run -= 1

def chaffer():
    subprocess.run([sys.executable, "./chaffer.py"])

def mhrvrs():
    os.system("./mhrv-rs")

def main():
    now: time.struct_time = time.localtime()

    args: dict = parse_arguments()
    
    try:
        if int(now.tm_hour) < 6 and args["past_12"] == "false":
            print(f"{Fore.RED}Disallowed.")
            print(f"{Fore.RED}Please don't access mhrv rs at this time, pattern detection would be much easier.")
    except: pass
    
    else :
        try:
            if args["past_12"] == "true":
                print(f"{Fore.LIGHTYELLOW_EX} WARNING: Using this app past 12 p.m. isn't recommended for security. Use at your own risk !")
        except: pass

        print(f"{Fore.GREEN}Allowed")
        
        process = multiprocessing.Process(target=chaffer)
        process.start()
    
        time.sleep(2)
        
        process2 = multiprocessing.Process(target=mhrvrs)
        process2.start()
        
        timer(int(args["time"]))

        print(f"{Fore.MAGENTA}TIME'S UP")
        
        time.sleep(2)
        
        os.system("killall mhrv-rs")

        process2.terminate()
        process2.close()
        process.terminate()
        process.close()


if __name__ == "__main__":
    main()
