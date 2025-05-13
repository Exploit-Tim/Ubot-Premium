import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "1927018403").split()))

API_ID = int(os.getenv("API_ID", "27418440"))

API_HASH = os.getenv("API_HASH", "0a08a360e0e9f41b9896f655c300d09d")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7883408843:AAGGxg588CdO_3AzO-1WMDd3TksewdwaCEE")

OWNER_ID = int(os.getenv("OWNER_ID", "1927018403"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", " -1002356932965").split()))

RMBG_API = os.getenv("RMBG_API", "f3CYy31QTGdSyYABY8D7FTqQ")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Unixxpedia:unix2008@cluster0.cn4kypa.mongodb.net/Unixxpedia?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002197595899"))
