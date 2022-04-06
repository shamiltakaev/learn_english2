import telebot

token = "2121965523:AAGC8Wep-94MqaRGOqYjWvVu3RZkUQNXQaY"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start", "help"])
def start_or_help(msg):
    t = msg.text

    if "start" in t:
        bot.send_message(msg.chat.id, "Добро пожаловать на наш бот.")
        bot.send_message(msg.chat.id, "Данный бот обучает английскому. "
                                          "Давайте для начала изучим английский алфавит.")
        bot.send_photo(msg.chat.id, open("img_letters/letter_a.jpg", "rb"))
        bot.send_audio(msg.chat.id, open("sound_letters/a.mp3", "rb"))



bot.polling()