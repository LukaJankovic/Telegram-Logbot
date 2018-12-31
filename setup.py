from setuptools import setup, find_packages

setup(
        name = "LogBot",
        version = "1.0.0",
        author = "Luka Jankovic",
        author_email = "lukjan1999@gmail.com",
        description = "Telegram bot that notifies about SSH logins",
        license = "GPLv3",
        keywords = "bot",
        packages = find_packages(),
        url = "https://github.com/LukaJankovic/Telegram-Logbot",
        scripts = ["logbot"]
)
