import os
from dotenv import load_dotenv
import json
from datetime import datetime
import shutil


def create_directories():
    # Check if directory 0 exists
    if not os.path.exists('0'):
        print("Directory 0 does not exist")
        return
    
    # Loop through directories 1-4
    x = int(input("How many script you want to run simultaneously? : - "))
    for i in range(1, x):
        dir_name = str(i)
        # Check if directory i exists
        if os.path.exists(dir_name):
            print("Directory", dir_name, "already exists")
        else:
            # Copy directory 0 to directory i
            print("Creating directory", dir_name)
            shutil.copytree('0', dir_name)

create_directories()



