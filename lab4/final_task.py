class Car:
    """
    Класс, описывающий базовый автомобиль
    """

    def __init__(self, brand: str, year_of_manufacture: int, color: str) -> None:
        """
        Инициализировать объект "Автомобиль"

        :param brand: марка автомобиля
        :param year_of_manufacture: год выпуска автомобиля
        :param color: цвет автомобиля

        :raise TypeError: если один из (brand, color) не является строкой или year_of_manufacture не является целым числом
        :raise ValueError: если year_of_manufacture меньше или равен 0
        """
        if not isinstance(brand, str) or not isinstance(color, str):
            raise TypeError("brand и color должны быть строками")
        if not isinstance(year_of_manufacture, int):
            raise TypeError("year_of_manufacture должен быть целым числом")
        if year_of_manufacture <= 0:
            raise ValueError("year_of_manufacture должен быть положительным числом")

        self.brand = brand
        self.year_of_manufacture = year_of_manufacture
        self.color = color
        self._current_speed: float = 0.0  # Защищённый атрибут, предотвращает некорректное изменение скорости извне

    def __str__(self) -> str:
        """
        Вернуть строковое представление автомобиля

        :return: строка с описанием автомобиля
        """
        return f"{self.brand} ({self.year_of_manufacture}), цвет: {self.color}"

    def __repr__(self) -> str:
        """
        Вернуть строковое представление автомобиля для разработчика

        :return: строка, содержащая всю информацию об автомобиле в формате конструктора
        """
        return (f"Car(brand={self.brand!r}, year_of_manufacture={self.year_of_manufacture!r}, color={self.color!r})")

    def drive(self, speed: float) -> None:
        """
        Начать движение автомобиля на заданной скорости

        :param speed: скорость движения (км/ч)

        :raise TypeError: если speed не является числом
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом")

        self._current_speed = speed
        print(f"Автомобиль {self.brand} двигается со скоростью {self._current_speed} км/ч")

    def stop(self) -> None:
        """
        Остановить автомобиль, сбрасывая скорость до нуля

        :return: None
        """
        self._current_speed = 0.0
        print(f"Автомобиль {self.brand} остановлен")


class PassengerCar(Car):
    """
    Класс, описывающий легковой автомобиль
    """

    def __init__(self, brand: str, year_of_manufacture: int, color: str, passenger_capacity: int) -> None:
        """
        Инициализировать объект "Легковой автомобиль"

        :param brand: марка автомобиля
        :param year_of_manufacture: год выпуска автомобиля
        :param color: цвет автомобиля
        :param passenger_capacity: вместимость автомобиля (количество пассажиров)

        :raise TypeError: если passenger_capacity не является целым числом
        :raise ValueError: если passenger_capacity меньше или равен 0
        """
        super().__init__(brand, year_of_manufacture, color)

        if not isinstance(passenger_capacity, int):
            raise TypeError("passenger_capacity должен быть целым числом")
        if passenger_capacity <= 0:
            raise ValueError("passenger_capacity должен быть положительным числом")

        self.passenger_capacity = passenger_capacity
        self._seat_belts_fastened = False  # Список состояния ремней безопасности

    def __str__(self) -> str:
        """
        Вернуть строковое представление легкового автомобиля

        :return: строка с описанием легкового автомобиля
        """
        return f"{super().__str__()}, вместимость: {self.passenger_capacity} пассажиров"

    def __repr__(self) -> str:
        """
        Вернуть строковое представление легкового автомобиля для разработчика

        :return: строка, содержащая всю информацию об автомобиле в формате конструктора
        """
        return (f"PassengerCar(brand={self.brand!r}, year_of_manufacture={self.year_of_manufacture!r}, "
                f"color={self.color!r}, passenger_capacity={self.passenger_capacity!r})")

    def fasten_seat_belts(self) -> None:
        """
        Пристегнуть все ремни безопасности

        :return: None
        """
        self._seat_belts_fastened = True
        print("Все пассажиры пристегнули ремни безопасности")

    def drive(self, speed: float) -> None:
        """
        Перегруженный метод: начать движение легкового автомобиля на заданной скорости

        Перед началом движения проверяется, пристёгнуты ли все пассажиры
        Если не все пристёгнуты, автомобиль не поедет

        :param speed: скорость движения (км/ч)

        :raise TypeError: если speed не является числом
        """
        if not self._seat_belts_fastened:
            print("Не все пассажиры пристёгнуты! Автомобиль не может начать движение")
            return

        super().drive(speed)
