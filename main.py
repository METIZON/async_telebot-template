from telebot.async_telebot import AsyncTeleBot
import asyncio

import config
import text_messages as txt
import keyboards
import database


bot = AsyncTeleBot(config.token)


# TXT TEMPLATES
txtMenu = txt.Message()

# INLINE MARKUPS
markup = keyboards.Inline()

# REPLY MARKUPS
kb = keyboards.Reply()


async def tables():
    users_dic = {
        'chatid': "integer",
        'name': "text"
    }

    await database.create_table('users', users_dic)


if __name__ == '__main__':
    try:
        asyncio.run(tables())
        print('[200] - tables ')
    except Exception:
        print('[400] - tables')
    finally:
        asyncio.run(bot.infinity_polling())
