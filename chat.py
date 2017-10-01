from actor import Actor


class Chat(object):
    def __init__(self,
                 width=100,
                 msg_width=70):
        self.width = width
        self.msg_width = msg_width
        self.max_msg_width = msg_width
        self.main_actor: Actor = None
        self.current_actor: Actor = None

    def send_message(self, msg: str, actor: Actor):
        self.current_actor = actor
        rows = self.match_width(msg)
        right_align = False
        if self.current_actor == self.main_actor:
            right_align = True
        response = self.join(rows, right_align=right_align)
        print(response)

    def match_width(self, msg: str):
        if len(msg) < self.max_msg_width:
            self.msg_width = len(msg)
        else:
            self.msg_width = self.max_msg_width

        words = msg.split()
        rows = []
        row = []
        row_len = 0

        while words:
            word = words.pop(0)

            if len(word) > self.msg_width:
                lim = self.msg_width - (row_len + len(row))
                word, tail = word[:lim], word[lim:]
                row.append(word)
                rows.append(row)
                row, row_len = [], 0
                words = [tail] + words

            elif row_len + len(word) + len(row) <= self.msg_width:
                row.append(word)
                row_len += len(word)

            else:
                words = [word] + words
                rows.append(row)
                row, row_len = [], 0
        if row:
            rows.append(row)

        return rows

    def join(self, rows: list, right_align=False):
        lines = [
            ' '.join(r).ljust(self.msg_width)
            for r in rows
        ]

        lines = self.outline(lines, padding=2)
        lines = self.add_actor_info(lines, self.current_actor, right_align=right_align)

        if right_align:
            lines = [line.rjust(self.width) for line in lines]
        return '\n'.join(lines)

    def outline(self, lines: list, padding=1) -> list:
        row = '-' * (self.msg_width + padding * 2)
        top = '┌' + row + '┐'
        bot = '└' + row + '┘'
        space = ' ' * padding
        lines = [
            '|' + space + line + space + '|'
            for line in lines
        ]
        return [top] + lines + [bot]

    def add_actor_info(self, lines: list, actor: Actor, right_align=False) -> list:
        lines = lines.copy()
        name = actor.name
        name_len = len(name)
        name_space = ' ' * (len(name) + 1)
        if right_align:
            lines = [
                line + name_space
                for line in lines
            ]
            lines[1] = lines[1][:-name_len] + name
        else:
            lines = [
                name_space + line
                for line in lines
            ]
            lines[1] = name + lines[1][name_len:]
        return lines
