#!/usr/local/bin/python3

import telegram
import tailer
import re
import urllib.request
import json

chatid = 

bot = telegram.Bot(token="")

for line in tailer.follow(open("/var/log/auth.log")):
    if line.split()[5] == "error:":
        ip = ""
        if line.split()[10] == "illegal":
            bot.send_message(chat_id=chatid, text="Authentication error for user "+line.split()[12]+" from "+line.split()[14])
            ip = line.split()[14]
        elif line.split()[6] == "maximum":
             bot.send_message(chat_id=chatid, text="Authentication error for user "+line.split()[11]+" from "+line.split()[13])
             ip = line.split()[13]
        else:
            bot.send_message(chat_id=chatid, text="Authentication error for user "+line.split()[10]+" from "+line.split()[12])
            ip = line.split()[12]
            
        if not re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
            ip = ip.split(".")[0].replace("-", ".")

        ip = re.sub("[a-zA-Z]", "", ip)

        if re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
            try:
                with urllib.request.urlopen("https://freegeoip.net/json/"+ip) as url:
                    data = json.loads(url.read().decode())
                    bot.send_location(chat_id=chatid, latitude=data["latitude"], longitude=data["longitude"])
            except HTTPError as e:
                print(e)
