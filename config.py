import os

API_ID = int(os.getenv("API_ID", 23939637))
API_HASH = os.getenv("API_HASH", "477f51720ede3eef6997dbc442151c43")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7489586742:AAFyIDZwQa8prfQqhtXYgBJYrqhT94JuRWE")

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://hepoda3624:lA8B88ten9lJFTqu@cluster0.ymnbbuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

SOURCE_CHAT_ID = int(os.getenv("SOURCE_CHAT_ID", -1002557248555))
DEST_CHAT_ID = int(os.getenv("DEST_CHAT_ID", -1004686512840))

OWNER_ID = int(os.getenv("OWNER_ID", 6425525488))
