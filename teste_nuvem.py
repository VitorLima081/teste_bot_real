import telebot
import time

chave_api = '6809143224:AAEJcwZqR9CPvZvEziZbgrXWZavd0wPUy38'
bot = telebot.TeleBot(chave_api)

id_usuario = 5416509396

while True:
    texto = 'testando nuvem'
    bot.send_message(id_usuario, texto)
    time.sleep(3600)