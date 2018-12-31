# Logbot for Telegram

So I've decided to revive this project. I've done some cleanup including a better pattern search as well as improving the ease of use. For example, it is no longer required to fetch the chat id yourself, the script takes care of it itself!

Though it is no longer able to send location, since freegeoip merged into ipstack, which means new API endpoints as well as requiring an access key.

## Requirements

* Python3
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* tailer

## Usage

```
sudo python3 setup.py install
logbot $configPath
```

There is a sample config file included in this repo (logbot.cfg) which can be used. Only token is required to get started; if you have a different ssh log path it can be specified here as well (key=logpath)

The token can be acquired from the Botfather.

Logbot can now be used as a service! Install logbot using the instructions above, then copy the logbot.service file to your systemd system directory (usually `/etc/systemd/system/logbot.service`) and your config file to `/etc/logbot.cfg`. Then run `sudo systemctl start logbot`.

## IP Lookup

Sadly IP lookup now requires registration for an API key. That can be done [here](https://ipstack.com/product). Then enter the API key in the cfg file.
