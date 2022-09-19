import telebot

from settings import API_KEY


class EchoBot:
    BOT = telebot.TeleBot(API_KEY)
    HELP_TEXT = "You can control bot by sending these commands:\n\n\n" \
                "/start_echo : start echo process\n" \
                "/stop_echo: start echo process"

    @staticmethod
    @BOT.message_handler(commands=['start', 'help'])
    def help(message):
        EchoBot.BOT.send_message(message.chat.id, EchoBot.HELP_TEXT)

    @staticmethod
    @BOT.message_handler(commands=['start_echo'])
    def start_echo(message):
        sent_msg = EchoBot.BOT.send_message(message.chat.id, "start Echo\nEnter your message")
        EchoBot.BOT.register_next_step_handler(sent_msg, EchoBot.echo_message_handler)

    @staticmethod
    @BOT.message_handler(commands=['stop_echo'])
    def stop_echo(message):
        EchoBot.BOT.send_message(message.chat.id, "Echo process is stopped")

    @staticmethod
    def echo_message_handler(message):
        if message.text != "/stop_echo":
            sent_msg = EchoBot.BOT.send_message(message.chat.id, message.text)
            EchoBot.BOT.register_next_step_handler(sent_msg, EchoBot.echo_message_handler)
        else:
            EchoBot.stop_echo(message)

    @classmethod
    def run(cls):
        cls.BOT.polling()


if __name__ == "__main__":
    EchoBot.run()
