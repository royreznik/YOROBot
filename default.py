from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import ChatAction
import logging
import moviescrape as movieScraper
import reddit

# Current commands:
# /movies
# /thought
# /Hello

dispatcher = None
updater = None
with open('token', 'r') as tokenfile:
    TELEGRAM_TOKEN = tokenfile.read().replace('\n', '')
    print TELEGRAM_TOKEN

def first_init():
    """Create updater instance and dispatcher reference"""
    global dispatcher
    global updater
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

first_init()
# Start logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    print update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text="Welcome to ZizaBot, how may I help you?")


def echo(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    print update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text='YORO')


def moviesCinema(bot, update):
    print update.message.text
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text='The movies in Cinema-City Glilot are:')
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    movies = movieScraper.getMovies()
    bot.sendMessage(chat_id=update.message.chat_id, text='\n'.join(movies))

movies_handler = CommandHandler('movies', moviesCinema)
dispatcher.add_handler(movies_handler)


def showerThought(bot, update):
    print update.message.text
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=reddit.getThought())

thoughts_handler = CommandHandler('thought', showerThought)
dispatcher.add_handler(thoughts_handler)

# def caps(bot, update, args):
#    text_caps = ' '.join(args).upper() + '!!!'
#    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#echo_handler = MessageHandler(Filters.text, echo)
#dispatcher.add_handler(echo_handler)


def hello(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    print update.message.text
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello, Welcome to ZizaBot, how may I help you?")


# Step 1: create handler instance
hello_handler = CommandHandler('Hello', hello)
# Step 2: add handler instance to dispatcher
dispatcher.add_handler(hello_handler)

# TODO finish implementing inline properties
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answerInlineQuery(update.inline_query.id, results)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text="wtf?")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
#caps_handler = CommandHandler('caps', caps, pass_args=True)
#dispatcher.add_handler(caps_handler)

def profile(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=bot.ChatAction.TYPING)



updater.start_polling()

