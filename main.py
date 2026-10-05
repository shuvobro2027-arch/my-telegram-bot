import os
import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

# ----------------- CONFIGURATION ----------------- #
# টেস্ট API_ID এবং API_HASH ব্যবহার করা হয়েছে
API_ID = 2040
API_HASH = "b18441a12607e109d9492a9a277e62c8"

# আপনার BotFather থেকে পাওয়া টোকেন
BOT_TOKEN = "8827350604:AAFGO-2wiBNimfUVgem3UE6KVbkTQ4NEBYI"
# ------------------------------------------------- #

app = Client("DRM_Downloader_Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

START_TIME = time.time()

def get_uptime():
    uptime = int(time.time() - START_TIME)
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"hours : {hours:02d} minutes : {minutes:02d} and seconds : {seconds:02d} ago"

@app.on_message(filters.command("start"))
async def start_command(client, message):
    user_name = message.from_user.first_name
    uptime_str = get_uptime()
    
    caption = (
        f"Hello 🖐️ **{user_name}** I am DRM Downloader Bot on Telegram.\n\n"
        f"📥 **Bot Uptime:** {uptime_str}"
    )

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("◇ Update Group ↗️", url="https://t.me/telegram"), InlineKeyboardButton("© Support ↗️", url="https://t.me/telegram")],
        [InlineKeyboardButton("📑 Usage", callback_data="usage"), InlineKeyboardButton("⚫ Plans", callback_data="plans")]
    ])

    await message.reply_text(caption, reply_markup=buttons, disable_web_page_preview=True)

print("Bot is running successfully...")
app.run()
