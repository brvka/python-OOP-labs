import doctest


class BoxItem:
    def __init__(self, name: str, length: float, width: float, height: float):
        """
        Инициализация объекта "Предмет коробки"

        :param name: Имя предмета
        :param length: Длина предмета
        :param width: Ширина предмета
        :param height: Высота предмета

        :raise TypeError: Если один из параметров размера не типа int или float
        :raise ValueError: Если один из параметров размера меньше или равен 0

        Пример:
        >>> item = BoxItem("Машинка", 15, 10, 5.5)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        self.name = name

    def calculate_size(self) -> float:
        """
        Метод для измерения размера предмета

        :return: Размер предмета

        Пример:
        >>> item = BoxItem("Машинка", 15, 10, 5.5)
        >>> item.calculate_size()
        """
        ...

    def rename(self, new_name: str) -> "BoxItem":
        """
        Переименовать предмет

        :return: Объект предмета

        Пример:
        >>> item = BoxItem("Машинка", 15, 10, 5.5)
        >>> item.rename("Porsche 911")
        """
        ...




class Box:
    def __init__(self, length: float, width: float, height: float):
        """
        Инициализировать объект "Коробка"

        :param length: длина коробки
        :param width: ширина коробки
        :param height: высота коробки

        :raise TypeError: Если один из параметров не типа int или float
        :raise ValueError: Если один из параметров меньше или равен 0

        Пример:
        >>> box = Box(30.3, 25.7, 50)
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        self.height = height

        self.items: list[BoxItem] = []

    def calculate_capacity(self) -> float:
        """
        Метод для подсчета вместительности коробки

        :return: Вместительность коробки

        Пример:
        >>> box = Box(30.3, 25.7, 50)
        >>> box.calculate_capacity()
        """
        ...

    def put_object(self, item: BoxItem) -> None:
        """
        Положить предмет в коробку

        :raise ValueError: Если предмет не помещается в коробку, то вызываем ошибку

        Пример:
        >>> item = BoxItem("Машинка", 15, 10, 5.5)
        >>> box = Box(30.3, 25.7, 50)
        >>> box.put_object(item)
        """
        ...

    def take_object(self, item_name: str) -> BoxItem:
        """
        Вынуть предмет из коробки по его имени

        :raise ValueError: Если такого предмета нет в коробке, то вызываем ошибку

        :return: Объект предмета коробки

        Пример:
        >>> item = BoxItem("Машинка", 15, 10, 5.5)
        >>> box = Box(30.3, 25.7, 50)
        >>> box.put_object(item)
        >>> box.take_object("Машинка")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()