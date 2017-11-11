#!/usr/local/bin/python3

import telegram
import tailer
import re
import urllib.request
import json
import sys
import configparser
import os

from telegram.ext import Updater

with open(os.path.expanduser(sys.argv[1])) as fp:
    config = configparser.ConfigParser()
    config.readfp(fp)

chatid = config.get("settings", "chat_id")
token = config.get("settings", "token")

updater = Updater(token=token)
dispatcher = updater.dispatcher
bot = updater.bot

def sendIPOnMap(ip):

    match = re.search("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ip)

    if not match:
        ip = ip.split(".")[0].replace("-", ".")
  
        ip = re.sub("[a-zA-Z]", "", ip)
        ip = ip.strip()

        sendIPOnMap(ip)
    else:
         try:
             with urllib.request.urlopen("https://freegeoip.net/json/"+match.group(0)) as url:
                 data = json.loads(url.read().decode())
                 bot.send_location(chat_id=chatid, latitude=data["latitude"], longitude=data["longitude"])
         except HTTPError as e:
             print(e)
             sendMessage("Unable to locate IP")
         
def sendMessage(message):
     bot.send_message(chat_id=chatid, text=message)
                
for line in tailer.follow(open("/var/log/auth.log")):
    match1 = re.search("authentication error for (.*) from (.*)", line)
    match2 = re.search("Failed password for (.*) from (.*)", line)
    
    match = None

    if match1:
        match = match1
    elif match2:
        match = match2

    if match:
        message = "Authentication failure for "

        nameArray = match.group(1).split()
        
        if not len(nameArray) == 1:
            name = nameArray[-1]

            message += "non-existent user "
            message +=  name
            
        else:
            message += "user "
            message += nameArray[0]
            
        message += " from "
        message += match.group(2)
    
        sendMessage(message)
        sendIPOnMap(match.group(2))
