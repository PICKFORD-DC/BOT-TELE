# MODULE
import os
import time
import logging
import telegram
from dotenv import load_dotenv
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
    ConversationHandler
    )
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update)

# CALL BACK
load_dotenv()
FIRST = range(1)


# LOG INFO
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# TOKEN SET
bot_token = os.getenv('BOT_TOKEN')
bot = telegram.Bot(token=bot_token)


# START COMMAND
def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("MENU", callback_data='menu'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hello World! \n My Name Is Pick_Bot ;-;", reply_markup=reply_markup)
    return FIRST


# GROUP RULLES
def menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("GROUP", callback_data='rules'),
            InlineKeyboardButton("INFO", callback_data='info'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Klick button untuk detail", reply_markup=reply_markup)
    return FIRST


# GROUP RULES-1
def rules(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Confirm", callback_data='ruless'),
            InlineKeyboardButton("Back", callback_data='menu'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Contoh Rules group :\n  - No Spam\n  - No Bapper\n  - No Ripp", reply_markup=reply_markup)
    return FIRST


def ruless(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Confirm", callback_data='group'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Contoh Rules group -1 :\n  - No Spam\n  - No Bapper\n  - No Ripp", reply_markup=reply_markup)
    return FIRST


def info(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Back", callback_data='menu'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Kumpulan Menu Lainya:\n  - /menu\n  - /menu\n", reply_markup=reply_markup)
    return FIRST


def puisi(update, context):
    text_puisi = "bercahayalah jiga kamu ingin dicintai setiap lawan jenis. 😉"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_puisi)


def pantun(update, context):
    text_pantun = "jalan-jalan ke jakarta barat, pulangnya beli sempolan. kalau kamu tidak ingin bersahabat, mari kita pacaran"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text_pantun)


def testing(update, context):
    text_puisi = "bercahayalah jiga kamu ingin dicintai setiap lawan jenis."
    update.message.reply_text("tes")
    update.message.reply_text("Testing")
    update.message.reply_text("Eittss")
    update.edit_message_text("")
    time.sleep(1)


def echo(update, context):
    message = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message)
    print(f"pesan dari user: {message}")


def main() -> None:
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(menu, pattern='menu'),
                CallbackQueryHandler(rules, pattern='rules'),
                CallbackQueryHandler(info, pattern='info'),
                CallbackQueryHandler(ruless, pattern='ruless'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('puisi', puisi))
    dispatcher.add_handler(CommandHandler('pantun', pantun))
    dispatcher.add_handler(CommandHandler('testing', testing))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
