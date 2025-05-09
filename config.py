import os

API_ID = int(os.getenv("API_ID", ))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

MONGO_URI = os.getenv("MONGO_URI", "")

SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", ))
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", ))

OWNER_ID = int(os.getenv("OWNER_ID", ))
