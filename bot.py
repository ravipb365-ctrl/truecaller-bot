import os
import requests
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# ✅ Load .env file
load_dotenv()

BOT_TOKEN = os.getenv("7394121126:AAEdafEE_8hff1NmDLO7tsirJKUXsldF_lI")

def start(update, context):
    update.message.reply_text(
        "👋 Welcome to 📞 Truecaller Info Bot!\n\n"
        "🔹 This bot helps you to get basic information about any phone number.\n\n"
        "📌 Example:\n"
        "`/lookup +916351516535`",
        parse_mode="Markdown"
    )

def lookup(update, context):
    if not context.args:
        update.message.reply_text("❌ Please provide a number!\n\nUsage: `/lookup +911234567890`", parse_mode="Markdown")
        return

    number = context.args[0]
    url = f"https://numb.hosters.club/?number={number}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        reply_msg = (
            "===================================\n"
            "📞 Truecaller Info Bot\n"
            "===================================\n"
            f"📱 Number   : {data.get('number')}\n"
            f"👤 Name     : {data.get('name')}\n"
            f"📡 Carrier  : {data.get('carrier')}\n"
            f"🌍 Country  : {data.get('country')}\n"
            "===================================\n"
            "✅ Lookup Completed!\n\n"
            "🛠 Script Prepared By Ravi"
        )
        update.message.reply_text(reply_msg)

    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN missing in .env file!")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("lookup", lookup))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
