import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Marlow ")
ALIVE_NAME = getenv("ALIVE_NAME", "Marlow")
BOT_USERNAME = getenv("BOT_USERNAME", "p84BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "p84BOT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DDSJD")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "nnn_e")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/125306966b713949afc3d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RAZANALYAFAE/AQANI")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b72180ca259cfbe7747e0.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b72180ca259cfbe7747e0.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b72180ca259cfbe7747e0.jpg")
