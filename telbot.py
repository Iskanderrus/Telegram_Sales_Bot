from telebot import TeleBot
from settings import config
from handlers.handler_main import HandlerMain


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):

        # указываем токен
        self.token = config.TOKEN
        # инициализируем бот на основе зарегистрированного токена
        self.bot = TeleBot(self.token)
        # инициализируем обработчик событий
        self.handler = HandlerMain(self.bot)

    def start(self):

        self.handler.handle()

    def run_bot(self):

        # обработчик событий
        self.start()
        # служит для запуска бота (работа в режиме нон-стоп)
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    bot = TelBot()
    bot.run_bot()
