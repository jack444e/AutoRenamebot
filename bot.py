from pyrogram import Client, filters
from pymongo import MongoClient
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI, SOURCE_CHAT_ID, DEST_CHAT_ID

# MongoDB setup
mongo = MongoClient(MONGO_URI)
db = mongo["captionbot"]
replacements = db["replacements"]

# Create defaults if empty
if replacements.count_documents({}) == 0:
    replacements.insert_many([
        {"old": "hello", "new": "hi"},
        {"old": "bot", "new": "assistant"}
    ])

# Telegram bot setup
app = Client("captionbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def replace_caption(text):
    for item in replacements.find():
        text = text.replace(item["old"], item["new"])
    return text

@app.on_message(filters.chat(SOURCE_CHAT_ID) & filters.caption)
async def forward_with_caption_edit(client, message):
    new_caption = replace_caption(message.caption)
    media = None

    if message.photo:
        media = message.photo
        await client.send_photo(DEST_CHAT_ID, photo=media.file_id, caption=new_caption)
    elif message.video:
        media = message.video
        await client.send_video(DEST_CHAT_ID, video=media.file_id, caption=new_caption)
    elif message.document:
        media = message.document
        await client.send_document(DEST_CHAT_ID, document=media.file_id, caption=new_caption)
    else:
        await client.send_message(DEST_CHAT_ID, new_caption)

app.run()
