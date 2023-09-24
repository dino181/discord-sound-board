from dotenv import load_dotenv
import os

load_dotenv()

GUILD_ID = os.getenv("DISCORD_GUILD_ID")
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
BASE_PATH = os.getenv("FILE_BASE_PATH")
