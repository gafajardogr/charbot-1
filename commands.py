from bot import Bot, CommandException


def config(command):
    def decorator(func):
        return command, func
    return decorator


@config('msg_width')
def change_msg_width(bot: Bot, args: list):
    if len(args) != 1:
        raise CommandException('Command accept exactly one argument.')
    width = args[0]
    if not width.isdecimal():
        raise CommandException('Width must be an integer.')
    width = int(width)
    bot.chat.set_msg_width(width)
    return f'Changed message width to {width} chars'


@config('chat_width')
def change_chat_width(bot: Bot, args: list):
    if len(args) != 1:
        raise CommandException('Command accept exactly one argument.')
    width = args[0]
    if not width.isdecimal():
        raise CommandException('Width must be an integer.')
    width = int(width)
    bot.chat.set_chat_width(width)
    return f'Changed chat width to {width} chars'


@config('username')
def change_name(bot: Bot, args: list):
    if len(args) != 1:
        raise CommandException('Command accept exactly one argument.')
    name = args[0]
    if not 1 <= len(name) <= 64:
        raise CommandException('Name must be in range(1, 64) inclusively.')
    bot.actor.name = name
    return f'Changed name to "{name}"'


# functions with @config are actually tuples: (command, func)
commands = [
    change_chat_width,
    change_msg_width,
    change_name,
]
