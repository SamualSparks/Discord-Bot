import os

def deleteDir():
    dir = "Desktop/bot/Bot"
    os.system("rm -rf " + dir)

def mk_bot_dir():
    os.system("mkdir Desktop/bot/Bot")
    
def cloneRepo():
    dir = "Desktop/bot/Bot"
    os.system("cd " + dir)
    os.system("git clone https://github.com/SamualSparks/Discord-Bot.git")

def run():
    deleteDir()
    mk_bot_dir()
    cloneRepo()

run()