import telegram
from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
updater = Updater('7543672286:AAFOPzzl7QEB1wzJQYXetbnG_PIxcyfi2uo')

def start(update, context):
    chat_id = update.effective_chat.id
    updater.send_message(chat_id, ' kenan !')

# /start command handler
updater.dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
updater.idle()
