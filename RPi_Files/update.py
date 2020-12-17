import os
import shutil as she
    
def cloneRepo():
    os.system("git clone https://github.com/SamualSparks/Discord-Bot.git")

def run():
    print("UPDATING THE REPO")
    she.rmtree("Discord-Bot")
    print("REMOVED OLD FILES")
    print("CLONING REPO")
    cloneRepo()
    print("PROCESS COMPLETE!")

run()