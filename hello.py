import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os
from telegram import InlineKeyboardMarkup, InlineKeyboardButton



import youtube_dl

import random

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




logger = logging.getLogger(__name__)
TOKEN = '1146262208:AAFMuvTCSA5Slblqg2wYGUg9x8mnClusBmE'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    print("hi")
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    
def help(update, context):

    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')
    
    item_yes = InlineKeyboardButton('yes', callback_data='yes')
    
    markup_reply = InlineKeyboardMarkup([[item_yes]])
    update.message.reply_text('Something', reply_markup=markup_reply)


def callback_query(update, context):
    
    if update.callback_query.data == 'yes':
        update.callback_query.edit_message_text('Ok')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

alp = 'qwertyuioplkjhgfdsazxcvbnm'
def echo(update, context):
    if update.message.entities:             # Работа со ссылками pkanal = 6
        for item in update.message.entities:
            if item.type == "url" and update.message.text.find('  ') == -1:
                if 'youtube.com' in update.message.text or 'youtu.be' in update.message.text:           #  Загружаем с Ютуб
                    doc1 = random.choices(alp, k=10)
                    doc = ""
                    for j in doc1:
                        doc+=j
                    doc = 'f'
                    if os.path.exists('f.mp4'):
                        os.remove('{}.mp4'.format(doc))
                    else:
                        pass
                    
                    ydl_opts = {'outtmpl': '{}.mp4'.format(doc), 'max_filesize': 600000000000000, 'preferredcodec': 'mp4'}
                    
                    link_of_the_video = update.message.text 
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link_of_the_video])
                    

                    #if os.path.exists('/tmp/f.mp4'):  # файл есть
                    
                    video = open('{}.mp4'.format(doc), 'rb')
                    update.message.reply_document(video)
                    
"""Start the bot."""
# Create the Updater and pass it your bot's token.
# Make sure to set use_context=True to use the new context based callbacks
# Post version 12 this will no longer be necessary
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher
# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))

# on noncommand i.e message - echo the message on Telegram
dp.add_handler(MessageHandler(Filters.text, echo))

dp.add_handler(CallbackQueryHandler(callback_query))
    
dp.add_error_handler(error)
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.start_polling()


