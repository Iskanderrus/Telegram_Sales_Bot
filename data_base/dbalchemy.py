

class Singleton(type):
    """
    Паттерн Singleton предоставляет механизм создания одного
    и только одного объекта класса,
    и предоставляет к нему глобальную точку доступа.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """ 
    Класс менеджер для работы с БД 
    """

    def __init__(self):
        pass