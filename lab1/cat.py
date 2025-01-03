import doctest

class Cat:
    def __init__(self, name: str, age: int):
        """
        Инициализация объекта "Кот"

        :param name: Имя кота
        :param age: Возраст кота

        :raise TypeError: Если возраст не типа int
        :raise ValueError: Если возраст меньше 0

        Example:
        >>> cat = Cat("Барсик", 3)
        """
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть меньше 0")
        self.age = age
        self.energy = 5

    def speak(self) -> None:
        """
        Подать голос

        Пример:
        >>> cat = Cat("Барсик", 3)
        >>> cat.speak()
        """
        ...

    def eat(self, food: str) -> None:
        """
        Покушать

        :param food:
        :raises ValueError: Если еда несъедобна, то вызываем ошибку

        Пример:
        >>> cat = Cat("Барсик", 3)
        >>> cat.eat("рыба")
        """
        eligible_food = ("рыба", "корм", "мышка")
        if food not in eligible_food:
            raise ValueError("Кот не ест такую еду")
        ...

    def sleep(self) -> None:
        """
        Поспать

        :raises ValueError: Если кот полон сил, то вызываем ошибку

        Пример:
        >>> cat = Cat("Барсик", 3)
        >>> cat.sleep()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()