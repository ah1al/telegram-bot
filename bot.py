
import telebot

# التوكن الخاص بالبوت
TOKEN = '7782723958:AAGYgjNcxv8tokZzAFPv-qO3yKOIpwMvd10'
bot = telebot.TeleBot(TOKEN)

# رسالة البداية
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا وسهلًا بك في البوت! 🌟\nأرسل لي أي رسالة وسأعيدها مع تعديل بسيط.")

# معالجة الرسائل النصية
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    modified_text = f"📝 رسالتك بعد التعديل: {message.text.upper()} 📝"
    bot.reply_to(message, modified_text)

# تشغيل البوت
print("🚀 البوت يعمل الآن...")
bot.polling()
