import telebot

token='7658232918:AAEa-Nsj0jp1gT0aEv350cCShJSPDUdcd0U'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ ==  '__main__':
     bot.polling()