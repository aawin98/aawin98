from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

token = '7881094347:AAHUtOi70ZLuWcPwSyvN_XWU0Uvpny-JZRg'


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Let's start!")

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Option 3", callback_data='3'),
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please choose:", reply_markup=reply_markup)

def keyboard_register(update: Update, context: Register(Context):
    query = update.register_query 
    query.answer() 
    query.edit_message_text(text=f"Selected option: {query.data}") 
    
if name == '__main__':
    updater = Updater(token=token, use_context=True)
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(keyboard_callback)) 
    updater.start_polling()
    updater.idle()
