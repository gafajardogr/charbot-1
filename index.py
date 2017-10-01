import sys

from actor import Actor
from bot import Bot
from chat import Chat
from commands import commands


def main():
    me = Actor(name='me')
    chat = Chat(width=80, msg_width=40, main_actor=me)
    bot = Bot(chat, actor=me)
    for command, callback in commands:
        bot.register_command(command, callback)

    while True:
        msg = input('> ')

        # remove input line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

        chat.send_message(me, msg)
        response, stop = bot.process_message(msg)
        chat.send_message(bot, response)

        if stop:
            break


if __name__ == '__main__':
    main()
