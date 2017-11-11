## Logbot for Telegram

Sends you a message when an incorrect login was made, along with a location approximation of the IP that was trying to log in. Tested on FreeBSD. Might, or might not work on other systems, but open an issue if you need help setting it up on your system!

## Requirements

* Python3
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* tailer

## Usage

`python3 logbot.py $configPath`

There is a sample config file included in this repo (logbot.cfg) which can be used. For now only two options are present; chat_id and token. As more features are added, more settings will be added. Then I'll also compile a list describing the settings.

The token can be acquired from the Botfather.

The chat id can be obtained by following [this guide](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot), until they mention the `def start(bot, update):` function. From there the chat_id can be acquired using `update.message.chat_id`

## Autostart

Create a service that runs the script, and enable it on boot. This will be different depending on which OS you're using. I'm running FreeBSD, so for me this file in rc.d works fine:

```

#!/bin/sh

# PROVIDE: logbot

. /etc/rc.subr

name="logbot"
rcvar=`set_rcvar`
start_cmd="logbot_start"

logbot_start()
{
    /usr/local/bin/python3 /usr/home/luka/Documents/Python/Logbot/logbot.py $configPath &
}

load_rc_config $name
run_rc_command "$1"

```

## Plans

* Send notification when user logs in
* Send notification when service starts
* ~~Config file~~
* Method for acquiring chat_id