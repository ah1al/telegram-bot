import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

WEBHOOK_URL = "https://<your-app-name>.herokuapp.com/"  # رابط Webhook الخاص بك

# إعداد Webhook
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

# نقطة النهاية الرئيسية
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
