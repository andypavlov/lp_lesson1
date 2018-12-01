from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'You called /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    if not update.message.chat.first_name == None:
        user_nick = update.message.chat.first_name
    elif not update.message.chat.last_name == None:
        user_nick = update.message.chat.first_name
    elif not update.message.chat.username == None:
        user_nick =  update.message.chat.username
    else:
        user_nick = 'super hidden man (ID={})'.format(update.message.chat.id)
    user_text = 'Hello {}! You are wrote: {}'.format(user_nick, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s",update.message.chat.username, update.message.chat.id,
                update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    logging.info('Bot starting')
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()