import os
import json
from emoji import emojize

data = json.load(open("/home/alex/Документы/Konder_86_Bot.json", "r"))

TOKEN = data.get("token")
NAME_DB = 'products.sqlite'
VERSION = '0.0.1'
AUTHOR = 'User'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///' + BASE_DIR, NAME_DB)
COUNT = 0

# кнопки управления:
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Полный каталог'),
    'INFO': emojize(':speech_balloon: О приложении'),
    'SETTINGS': emojize('⚙️ Инструкция'),
    'SPAREPARTS': emojize(':pizza: Запасные части'),
    'SPLITSYSTEMS': emojize(':bread: Сплит-системы'),
    'SERVICES': emojize(':shaved_ice: Сервис'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'SPAREPARTS': 1,
    'SPLITSYSTEMS': 2,
    'SERVICES': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
