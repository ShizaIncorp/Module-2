from tkinter.font import names


class Telephone:

    """Базовый класс"""

    def __init__(self, memory: int, name: str, model: str):
        self._name = name #так как имя не телефона по желанию пользователя нельзя менять, поэтому оно непубличное
        self._model = model #так же причина, что и выше
        self._memory = memory #Память дискретна, слоты для расширения памяти не предусмотрены)

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, memory):
        if not isinstance(memory, int):
            raise TypeError
        if not memory > 0:
            raise ValueError
        self._memory = memory

    def __str__(self):
        return f"Название телефона {self.name}. Модель {self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, model={self.model!r})"

    def passwords(self) -> None:
        """Выбирается один из 3 видов записи паролей"""
        ...

    def screen(self) -> None:
        """Выбирается один из 2 видов экронов"""
        ...



class Apple(Telephone):

    """Дочерний класс"""

    def __init__(self, memory: int, name: str, model: str, system: str):
        super().__init__(memory, name, model)
        self._system = system #система идет от компании

    @property
    def system(self):
        return self._system

    def interface_management(self) -> None:
        """Выбирается система управления интерфейсом, кнопочная или жестами зависит также от системы"""
        ...


