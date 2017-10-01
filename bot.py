from actor import Actor


class Bot(Actor):
    def __init__(self, name='bot', icon='🤖'):
        super().__init__(name, icon)

    def process_message(self, message: str) -> (str, bool):
        if len(message) > 1 and message.startswith('/'):
            return self.process_command(message[1:])
        return message, False

    def process_command(self, message: str) -> (str, bool):
        args = message.split()
        command = args[0]
        if command in ('quit', 'exit'):
            return 'Bye bye', True
        return f'Unknown command /{command} and args {args[1:]}', False
