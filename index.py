import sys

from actor import Actor
from bot import Bot
from chat import Chat


def start():
    me = Actor(name='me')
    bot = Bot()
    chat = Chat(width=80, msg_width=40)
    chat.main_actor = me

    while True:
        msg = input('> ')
        # remove input line
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

        chat.send_message(msg, me)
        response, stop = bot.process_message(msg)
        chat.send_message(response, bot)

        if stop:
            break


def test():
    width = 40
    msg_width = 80
    you = Actor()
    bot = Actor(name='bot')
    chat = Chat(width=width, msg_width=msg_width)
    chat.current_actor = you
    rows = chat.match_width('bla bla bla bla blaaaaaaaaaaaaaa bla bla bla bla bla bla bla bla bla bla bla')
    # pprint(rows)
    print(chat.join(rows))
    chat.current_actor = bot
    print(chat.join(rows, right_align=True))
    chat.current_actor = you
    print(chat.join(rows))
    chat.current_actor = bot
    print(chat.join(rows, right_align=True))


def main():
    start()
    # test()


if __name__ == '__main__':
    main()
