

import datetime
import time




class Messages():

    def __init__(self, minutes=1):
        self.messages = []
        self.window = datetime.timedelta(minutes=minutes)

    def _print(self):
        print(self.messages)

    def clean_messages(self):
        now = datetime.datetime.now()
        cutoff = now - self.window
        self.messages = [ i for i in self.messages if i[0] > cutoff ]

    def add_message(self, message):
        if len(self.messages) >= 10:
            self.messages.pop()
        now = datetime.datetime.now()
        item = (now, message)
        self.messages.insert(0, item)

    def full_context_from_messages(self):
        prefix = "Conversation so far:\n"
        msgs = "\n\n".join([i[1] for i in self.messages[::-1]])
        return prefix + msgs



if __name__ == "__main__":
    print("simple testing")
    msgs = Messages(minutes=1)
    msgs.clean_messages()
    msgs.add_message("hey")
    msgs.add_message("hey")
    msgs.add_message("hey")
    time.sleep(10)
    msgs.add_message("hey")
    msgs._print()
    msgs.clean_messages()
    msgs._print()
    time.sleep(50)
    msgs.clean_messages()
    msgs._print()
