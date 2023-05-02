import os
import socket
import requests
import json
import subprocess
import requests
from dotenv import load_dotenv
from datetime import datetime
from messages import Script, Accounts
import traceback
import time
import asyncio
import platform

my_script = Script()
my_account = Accounts()

# 642d83902b90b0a503aa33cf


def prRed(prt):
    """colour print"""
    print(f"\033[91m{prt}\033[00m")


def file_check(name):
    return os.path.isfile(name)


def Validate(TOKEN):
    print("validating data")
    url = "https://database.sigmacodeblue.workers.dev/api/get/group"
    payload = {'_id': TOKEN}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request(
        "POST", url, headers=headers, data=payload, files=[])

    data = response.json()

    accounts = data[0]['accounts']
    # Write the accounts data to a file
    with open('config.json', 'w') as f:
        json.dump(accounts, f)
    print("JSON DATA LOADED")
    return DistributeAccount()


def main():
    print("Load environment variables from .env file")
    load_dotenv()  # Load environment variables from .env file
    if not file_check(".env"):
        print(".env file does not exist.")
        print("to create token goto:- 'https://sigmacodeblue.pages.dev/' ")
        token = input("Please enter your token: ")
        with open(".env", "w") as f:
            f.write(f"TOKEN={token}")
            os.environ["TOKEN"] = token
        return Validate(os.environ.get('TOKEN'))
    elif 'TOKEN' not in os.environ:
        print("to create token goto:- 'https://sigmacodeblue.pages.dev/' ")
        token = input('TOKEN (groupID) does not exist. Please enter it now: ')
        with open(".env", "a") as f:
            f.write(f"\nTOKEN={token}")
            os.environ["TOKEN"] = token
        return Validate(os.environ.get('TOKEN'))
    else:
        return Validate(os.environ.get('TOKEN'))


def divideEqually(items, n):
    # Calculate the size of each group
    group_size = len(items) // n

    # Create a list to hold the groups
    groups = []

    # Iterate over the groups
    for i in range(n):
        # Calculate the start and end indexes for this group
        start = i * group_size
        end = start + group_size

        # If this is the last group, include any remaining items
        if i == n - 1:
            end = len(items)

        # Add the items for this group to the list of groups
        groups.append(items[start:end])

    return groups


def DistributeAccount():
    print("Distributing account")
    path = "./"
    with open('config.json') as f:
        data = json.load(f)
    dirs = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    dirs.remove("__pycache__")
    num = (len(data)//len(dirs))
    x = divideEqually(data, len(dirs))
    for i, n in enumerate(x):
        with open(f'./{i}/accounts.json', 'w') as f:
            json.dump(n, f)
    return True


async def connectVPN(location):
    if location == "US":
        location = "Ranch"
    if location == "CA":
        location = "comfort zone"
    # Start Windscribe VPN service
    process = subprocess.Popen(
        ['windscribe-cli', 'connect', location], stdout=subprocess.PIPE)
    process2 = subprocess.Popen(
        ['windscribe-cli', 'firewall', 'off'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    time.sleep(12)
     


async def DisconnectVPN():
    print("Disconnecting VPN...")
    process = subprocess.Popen(
        ['windscribe-cli', 'disconnect'], stdout=subprocess.PIPE)
    time.sleep(6)
    print("VPN disconnected!")
    return True


def whereAmI():
    url = "https://hidemy.name/api/geoip.php?out=js&htmlentities"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers)
    jsons = json.loads(response.text)
    print(jsons)
    ip_address = next(iter(jsons))
    # Get the value of 'US'
    value = jsons[ip_address][0]
    return value


def check_data():
    today = datetime.now().strftime("%d:%m:%Y")
    path = "./"
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    dirs.remove("__pycache__")

    if file_check("data.json"):
        with open("data.json", "r") as f:
            data = json.load(f)
        if data["data"] == today:

            US = True
            CA = True

            for item in data['Grind']:
                if item['US'] == False:
                    US = False
                if item['CA'] == False:
                    CA = False

            data["US"] = US
            data["CA"] = CA

            with open("data.json", "w") as f:
                json.dump(data, f)

            false_keys = []
            if data["US"] == False:
                false_keys.append("US")
            if data["CA"] == False:
                false_keys.append("CA")
            return false_keys
        else:
            data = {
                "data": today,
                "US": False,
                "CA": False,
                "Grind": []
            }
            for item in dirs:
                items = {"name": item, "US": False, "CA": False}
                data["Grind"].append(items)
            # Write the JSON object to a new file called data.json
            with open("data.json", "w") as f:
                json.dump(data, f)
            return check_data()
    else:
        data = {
            "data": today,
            "US": False,
            "CA": False,
            "Grind": []
        }
        for item in dirs:
            items = {"name": item, "US": False, "CA": False}
            data["Grind"].append(items)
        # Write the JSON object to a new file called data.json
        with open("data.json", "w") as f:
            json.dump(data, f)
        return check_data()


def runFiles():
    path = "./"
    dirs = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    args = ['--session', '--no-images', '--superfast', "--skip-shopping"]
    dirs.remove("__pycache__")
    processes = []
    for subdir in dirs:
        patha = os.path.join(path, str(subdir), 'main.py')
        command = ['py', patha] + args
        process = subprocess.Popen(command)
        processes.append(process)
    # Wait for all processes to complete
    for process in processes:
        process.wait()


 

def completeGrind(folderId):
    prRed(f"GRIND COMPLETE IN FOLDER : - {folderId}")
    location = whereAmI()
    # 1) load json data from file
    with open('data.json', 'r') as f:
        data = json.load(f)

    # 2) update data accordingly (which folder req to update data)
    for n in data["Grind"]:
        if n["name"] == str(folderId):
            n[location] = True

    # 3) check if current location(GRIND) is done for all folder or not
    US = True  # first true
    CA = True

    for n in data["Grind"]:  # if anyone of that is false then main variable is false
        if n['US'] == False:
            US = False
        if n['CA'] == False:
            CA = False

    data["US"] = US
    data["CA"] = CA
    
    with open("data.json", "w") as f:
        json.dump(data, f)

    if data["US"] == True and data["CA"] == True:
        GrindFinish()
    elif location == "US" and data["US"] == True:
        run(False)
        print("grind from US done")
    elif location == "CA" and data["CA"] == True:
        run(False)
        print("grind from CA done")
    else:
        print(f"Some Grind Left In {location}")

def run(first):
    asyncio.run(DisconnectVPN())
    main()
    x = check_data()
    y = whereAmI()

    if first:   
        my_token = os.environ.get('TOKEN')  # Replace with your actual token value
        my_script.start(my_token)
    print(f"grind left in : - {x}")
    print(f"we are currently in :- {y}")
    x.sort(reverse=True)
    if len(x) == 1:
        GrindFinish()
    else:
        print(f"GRIND START FROM : - {x[0]}")
        asyncio.run(connectVPN(x[0]))
        runFiles()

def GrindFinish():
        print("both grind complete")
        print("shutdown pc")
        asyncio.run(DisconnectVPN())
        plat = platform.system()
        my_token = os.environ.get('TOKEN')
        my_script.stop(my_token)
        if plat == "Windows":
            #os.system("shutdown /s /t 10")
            input("now this pc shouting down in 10  sec")

def prBlue(prt):
    """colour print"""
    print(f"\033[94m{prt}\033[00m")

def logo():
    prBlue("""
____ _ ____ _  _ ____    ____ ____ ____ _  _ ___  
[__  | | __ |\/| |__|    | __ |__/ |  | |  | |__] 
___] | |__] |  | |  |    |__] |  \ |__| |__| |                                                                                              
    """)
    prRed("Let's Fuck Microsoft : - ")

if __name__ == '__main__':
    try:
        logo()
        run(True)
    except Exception as e:
        traceback.print_exc()
        prRed(str(e))
        my_script.error("null", str(e), "main")
        input("press Enter to close...")



"""
Task that need to be updated
1) improve point counter
2) add auto vpn change function 
3) every update to telegram
4) script start stop function
"""
