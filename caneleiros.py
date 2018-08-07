import telegram
import logging
import requests
import datetime
from flask import Flask, request
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = Flask(__name__)
logger = logging.getLogger(__name__)

bot_token = "579475538:AAFjEgtt1BFPIU_f4IjYyaix-heREgouX3g"

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

def get_url(method):
  return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

def marca(bot, update):
    update.message.reply_text("Jogo marcado!")

def confirma(bot, update):
    update.message.reply_text("Confirmado.")

def desconfirma(bot, update):
    update.message.reply_text("Desconfirmado!")

def cancel(bot, update):
    update.message.reply_text('Sem futebol essa semana entao...', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

marca_handler = CommandHandler('marca', marca)
dispatcher.add_handler(marca_handler)

confirmar_handler = CommandHandler('confirma', confirma)
dispatcher.add_handler(confirmar_handler)

desconfirmar_handler = CommandHandler('desconfirma', desconfirma)
dispatcher.add_handler(desconfirmar_handler)

updater.start_polling()