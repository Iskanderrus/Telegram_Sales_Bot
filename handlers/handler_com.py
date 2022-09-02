from handlers.handler import Handler


class HandlerCommands(Handler):
    # класс для обработки входящих команд /start & /help и т.д.
    def __int__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        # обработка входящей /start команды
        self.bot.send_message(message.chat.id,
                              f'(message.from_user.first_name)',
                              f'(здравствуйте! Жду дальнейших задач.)',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            print(message)
            if message.text == '/start':
                self.pressed_btn_start(message)
