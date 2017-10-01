import re

from actor import Actor
from chat import Chat


class CommandException(Exception):
    def __init__(self, msg, *args):
        super().__init__(msg, *args)


class Bot(Actor):
    def __init__(self, chat: Chat, actor: Actor):
        super().__init__(name='bot', icon='🤖')
        self.chat = chat
        self.actor = actor
        self.commands = {}
        self.command_regex = re.compile(r'^/[\w]+(\s+.*)?$')

    def process_message(self, message: str) -> (str, bool):

        if len(message) > 1 and self.command_regex.match(message):
            return self.process_command(message[1:])
        return message, False

    def process_command(self, message: str) -> (str, bool):
        args = message.split()
        command, args = args[0], args[1:]
        if command in ('quit', 'exit'):
            return 'Bye bye', True

        callback = self.commands.get(command, None)
        if callback is not None:
            try:
                result = callback(self, args)
            except CommandException as e:
                result = str(e)
            except Exception:
                result = 'Command usage (from docstring):\n' + str(callback.__doc__)
            return result, False

        return f'Unknown command /{command}', False

    def register_command(self, command: str, callback):
        """
        :param command: command name. Will be used as /<command>
        :param callback: function that accept 2 argument: bot instance, list of arguments
        :return:
        """
        self.commands[command] = callback
