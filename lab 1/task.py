# TODO: Подробно описать три произвольных класса
import random
from random import randint

class Cheese:
    def __init__(self, length: int, width: int, heigth: int):
        self.length = length
        self.width = width
        self.heigth = heigth



    def init_change_length(self, length: int) -> None:
        """
        Данный метод, позволяет изменить длину сыра.

        :param length:
        :return None:
        """
        if not isinstance(length, int):
            raise TypeError
        if not length > 0:
            raise ValueError
        self.length = length


    def init_change_width(self, width: int) -> None:
        """
        Данный метод, позволяет изменить ширину сыра.

        :param width:
        :return None:
        """
        if not isinstance(width, int):
            raise TypeError
        if not width > 0:
            raise ValueError
        self.width = width

    def init_change_heigth(self, heigth: int) -> None:
        """
        Данный метод, позволяет изменить высоту сыра.

        :param heigth:
        :return None:
        """
        if not isinstance(heigth, int):
            raise TypeError
        if not heigth > 0:
            raise ValueError
        self.heigth = heigth

    def init_calculate_volume(self) -> int:
        """
        Данный метод, позволяет найти объем сыра.

        :return volume:
        """
        if self.heigth and self.width and self.length > 0:
            volume = self.length * self.width * self.heigth
        else:
            raise ValueError
        return volume

class Lamp:
    """
    >>> lamp = Lamp(1, 300)
    >>> lamp.init_check_lamp_on()
    True
    >>> lamp.init_change_switch()
    >>> print(lamp.switch)
    0
    >>> lamp.init_change_brightness(500)
    >>> print(lamp.brightness)
    500
    """
    def __init__(self, switch: int, brightness: int):
        self.switch = switch
        self.brightness = brightness


    def init_change_switch(self) -> None:
        """
        Данный метод переключает лампочку.

        :param switch:
        :return None:
        """
        if self.switch == 1:
            self.switch = 0
        else:
            self.switch = 1

    def init_check_lamp_on(self) -> bool:
        """
        Данный метод проверяет включена ли лапочка.

        :return check:
        """
        if self.switch is None:
            raise ValueError
        check = None
        if self.switch == 1:
            check = True
        else:
            check = False
        return check

    def init_change_brightness(self, brightness: int) -> None:
        """
        Данный метод позволяет изменить яркость лампочки.

        :param brightness:
        :return None:
        """
        if not isinstance(brightness, int):
            raise TypeError
        if not brightness > 0:
            raise ValueError
        self.brightness = brightness



class MysteriousTangerine:
    def __init__(self, radius: int, colour: str):
        self.radius = radius
        self.colour = "Оранжевый"
        if colour == self.colour:
            random_colour = ["Красный", "Желтый", "Фиолетовый", "Зеленый", "Голубой", "Синий"]
            self.colour = random.choice(random_colour)
        self.peel = randint(0,1)

    def init_repaint(self, colour: str) -> None:
        """
        Данный метод меняет цвет мандаринки.

        :param colour:
        :return None:
        """
        if not isinstance(colour, str):
            raise TypeError
        else:
            self.colour = colour


    def init_check_peel(self) -> bool:
        """
        Данный метод позволяет проверить, есть ли кожура на мандарине.

        :return check:
        """
        if not isinstance(self.peel, int):
            raise TypeError
        if not self.peel in [0, 1]:
            raise ValueError
        if self.peel == 1:
            check = True
        else:
            check = False
        return check

    def init_remove_peel(self) -> None:
        """
        Данный метод позволяет снять кожура если она есть.

        :return None:
        """
        if not isinstance(self.peel, int):
            raise TypeError
        if not self.peel in [0, 1]:
            raise ValueError
        if self.peel == 1:
            self.peel = 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()





