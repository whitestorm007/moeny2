import os
import requests
from dotenv import load_dotenv
import requests
import json
import socket
BASE_URL = "https://database.sigmacodeblue.workers.dev/api"
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}

 

class Script:
    def start(self, token):
        url = f"{BASE_URL}/script/start"
        payload = f'_id={token}'
        SendMessage(method="POST", url=url, payload=payload)
        return True
        
    def stop(self, token):
        hostname = socket.gethostname()
        url = f"{BASE_URL}/script/stop"
        payload = f'_id={token}&pc={hostname}'
        SendMessage(method="POST", url=url, payload=payload)
        
    def error(self,email, error,folder):
        url = f"{BASE_URL}/script/error"
        token = os.environ.get('TOKEN')
        payload = f'_id={token}&error={error}&email={email}&folder=${folder}'
        SendMessage(method="POST", url=url, payload=payload)



class Accounts:
    def lockdown(self,email):
        url = f"{BASE_URL}/account/lockdown"
        token = os.environ.get('TOKEN')
        payload = f'_id={token}&email={email}'
        SendMessage(method="POST", url=url, payload=payload)

    def lock(self,email):
        url = f"{BASE_URL}/account/lock"
        token = os.environ.get('TOKEN')
        payload = f'_id={token}&email={email}'
        SendMessage(method="POST", url=url, payload=payload)

    def block(self,email):
        url = f"{BASE_URL}/account/block"
        token = os.environ.get('TOKEN')
        payload = f'_id={token}&email={email}'
        SendMessage(method="POST", url=url, payload=payload)

    def Error(self,email):
        url = f"{BASE_URL}/account/error"
        token = os.environ.get('TOKEN')
        payload = f'_id={token}&email={email}&err=⛔️ Unknown error occurred'
        SendMessage(method="POST", url=url, payload=payload)

    def updatePoint(self,email,POINTS_COUNTER ,New_points):
        url = f"{BASE_URL}/account/update/point"
        POINTS_COUNTER = int(POINTS_COUNTER)
        New_points= int(New_points)
        payload = f'email={email}&POINTS_COUNTER={POINTS_COUNTER}&New_points={New_points}'
        SendMessage(method="POST", url=url, payload=payload)

    def updateCookie(self,email,token):
        print("hack account")
    def GrindDone(self,scriptId):
        print("grind complete on script")



def SendMessage(method="POST", url=None, payload=None):
    response = requests.request(method=method, url=url, headers=HEADERS, data=payload)
    # print(response.text)


"""
logic of what to grind next
VARIABLE : location , folderId;

1) load json data from file 
2) update data accordingly (which folder req to update data)
3) check if current location(GRIND) is done for all folder or not
4) if not then ignore , else , run main()
"""