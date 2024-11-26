from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Абстрактный базовый класс, представляющий животное.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует животное с заданными именем и возрастом.

        Аргументы:
            name (str): Имя животного.
            age (int): Возраст животного.
        """
        self._name = name
        self._age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного для пользователя.

        Возвращает:
            str: Строковое представление животного.
        """
        return f"{self.__class__.__name__} по имени {self.name}, возраст {self.age} лет."

    def __repr__(self) -> str:
        """
        Возвращает однозначное строковое представление животного.

        Возвращает:
            str: Однозначное строковое представление животного.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age})"

    @property
    def name(self) -> str:
        """
        Возвращает имя животного.

        Возвращает:
            str: Имя животного.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает имя животного.

        Аргументы:
            value (str): Новое имя животного.
        """
        self._name = value

    @property
    def age(self) -> int:
        """
        Возвращает возраст животного.

        Возвращает:
            int: Возраст животного.
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """
        Устанавливает возраст животного.

        Аргументы:
            value (int): Новый возраст животного.

        Вызывает:
            ValueError: Если возраст отрицательный.
        """
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self._age = value

    @abstractmethod
    def speak(self) -> str:
        """
        Абстрактный метод для получения звука, который издает животное.

        Возвращает:
            str: Звук животного.
        """
        pass

    def move(self) -> str:
        """
        Описывает движение животного.

        Возвращает:
            str: Описание движения.
        """
        return "Животное двигается."


class Dog(Animal):
    """
    Класс, представляющий собаку, наследуется от Animal.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализирует собаку с заданными именем, возрастом и породой.

        Аргументы:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        """
        Возвращает звук, который издает собака.

        Перегружено для отражения специфичного звука собаки.

        Возвращает:
            str: Звук собаки.
        """
        return "Гав-гав!"

    def fetch(self, item: str) -> str:
        """
        Описывает действие собаки по принесению предмета.

        Аргументы:
            item (str): Предмет, который нужно принести.

        Возвращает:
            str: Описание действия.
        """
        return f"{self.name} приносит {item}."

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки для пользователя.

        Возвращает:
            str: Строковое представление собаки.
        """
        return f"{self.__class__.__name__} по имени {self.name}, порода {self.breed}, возраст {self.age} лет."

    def __repr__(self) -> str:
        """
        Возвращает однозначное строковое представление собаки.

        Возвращает:
            str: Однозначное строковое представление собаки.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, breed={self.breed!r})"

    def move(self) -> str:
        """
        Описывает движение собаки.

        Перегружено для предоставления специфичного описания движения собаки.

        Возвращает:
            str: Описание движения собаки.
        """
        return f"{self.name} бежит энергично."


class Cat(Animal):
    """
    Класс, представляющий кошку, наследуется от Animal.
    """

    def speak(self) -> str:
        """
        Возвращает звук, который издает кошка.

        Перегружено для отражения специфичного звука кошки.

        Возвращает:
            str: Звук кошки.
        """
        return "Мяу!"

    def purr(self) -> str:
        """
        Описывает мурлыканье кошки.

        Возвращает:
            str: Описание мурлыканья.
        """
        return f"{self.name} мурлычет."

    def move(self) -> str:
        """
        Описывает движение кошки.

        Перегружено для предоставления специфичного описания движения кошки.

        Возвращает:
            str: Описание движения кошки.
        """
        return f"{self.name} двигается грациозно."


class Bird(Animal):
    """
    Класс, представляющий птицу, наследуется от Animal.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Инициализирует птицу с заданными именем, возрастом и видом.

        Аргументы:
            name (str): Имя птицы.
            age (int): Возраст птицы.
            species (str): Вид птицы.
        """
        super().__init__(name, age)
        self.species = species

    def speak(self) -> str:
        """
        Возвращает звук, который издает птица.

        Перегружено для отражения специфичного звука птицы.

        Возвращает:
            str: Звук птицы.
        """
        return "Чирик-чирик!"

    def fly(self, speed: int) -> str:
        """
        Описывает полет птицы с заданной скоростью.

        Аргументы:
            speed (int): Скорость полета в км/ч.

        Возвращает:
            str: Описание полета.
        """
        return f"{self.name} летит со скоростью {speed} км/ч."

    def __str__(self) -> str:
        """
        Возвращает строковое представление птицы для пользователя.

        Возвращает:
            str: Строковое представление птицы.
        """
        return f"{self.__class__.__name__} по имени {self.name}, вид {self.species}, возраст {self.age} лет."

    def __repr__(self) -> str:
        """
        Возвращает однозначное строковое представление птицы.

        Возвращает:
            str: Однозначное строковое представление птицы.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age}, species={self.species!r})"


class Vehicle(ABC):
    """
    Абстрактный базовый класс, представляющий транспортное средство.
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует транспортное средство с заданными маркой, моделью и годом выпуска.

        Аргументы:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self._brand = brand
        self._model = model
        self._year = year

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства для пользователя.

        Возвращает:
            str: Строковое представление транспортного средства.
        """
        return f"{self.__class__.__name__} {self.brand} {self.model}, {self.year} года выпуска."

    def __repr__(self) -> str:
        """
        Возвращает однозначное строковое представление транспортного средства.

        Возвращает:
            str: Однозначное строковое представление транспортного средства.
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year})"

    @property
    def brand(self) -> str:
        """
        Возвращает марку транспортного средства.

        Возвращает:
            str: Марка транспортного средства.
        """
        return self._brand

    @property
    def model(self) -> str:
        """
        Возвращает модель транспортного средства.

        Возвращает:
            str: Модель транспортного средства.
        """
        return self._model

    @property
    def year(self) -> int:
        """
        Возвращает год выпуска транспортного средства.

        Возвращает:
            int: Год выпуска транспортного средства.
        """
        return self._year

    @abstractmethod
    def drive(self, speed: int) -> str:
        """
        Абстрактный метод для описания движения транспортного средства с заданной скоростью.

        Аргументы:
            speed (int): Скорость движения в км/ч.

        Возвращает:
            str: Описание движения.
        """
        pass


class Car(Vehicle):
    """
    Класс, представляющий автомобиль, наследуется от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, engine_type: str) -> None:
        """
        Инициализирует автомобиль с заданными маркой, моделью, годом выпуска и типом двигателя.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            engine_type (str): Тип двигателя автомобиля.
        """
        super().__init__(brand, model, year)
        self.engine_type = engine_type

    def drive(self, speed: int) -> str:
        """
        Описывает движение автомобиля с заданной скоростью.

        Перегружено для учета особенностей автомобиля.

        Аргументы:
            speed (int): Скорость движения в км/ч.

        Возвращает:
            str: Описание движения.
        """
        return f"Автомобиль {self.brand} {self.model} движется со скоростью {speed} км/ч."

    def refuel(self, liters: int) -> str:
        """
        Описывает процесс заправки автомобиля.

        Аргументы:
            liters (int): Количество литров топлива.

        Возвращает:
            str: Описание процесса заправки.
        """
        return f"Заправлено {liters} литров топлива в {self.brand} {self.model}."

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля для пользователя.

        Возвращает:
            str: Строковое представление автомобиля.
        """
        return f"{self.__class__.__name__} {self.brand} {self.model}, {self.year} года выпуска, двигатель {self.engine_type}."

    def move(self) -> str:
        """
        Описывает движение автомобиля.

        Перегружено для предоставления специфичного описания движения автомобиля.

        Возвращает:
            str: Описание движения автомобиля.
        """
        return f"Автомобиль {self.brand} {self.model} ускоряется плавно."


class Bicycle(Vehicle):
    """
    Класс, представляющий велосипед, наследуется от Vehicle.
    """

    def __init__(self, brand: str, model: str, year: int, bicycle_type: str) -> None:
        """
        Инициализирует велосипед с заданными маркой, моделью, годом выпуска и типом велосипеда.

        Аргументы:
            brand (str): Марка велосипеда.
            model (str): Модель велосипеда.
            year (int): Год выпуска велосипеда.
            bicycle_type (str): Тип велосипеда (например, горный, дорожный).
        """
        super().__init__(brand, model, year)
        self.bicycle_type = bicycle_type

    def drive(self, speed: int) -> str:
        """
        Описывает движение велосипеда с заданной скоростью.

        Перегружено для учета особенностей велосипеда.

        Аргументы:
            speed (int): Скорость движения в км/ч.

        Возвращает:
            str: Описание движения.
        """
        return f"Велосипед {self.brand} {self.model} движется со скоростью {speed} км/ч под управлением велосипедиста."

    def brake(self) -> str:
        """
        Описывает процесс торможения велосипеда.

        Возвращает:
            str: Описание процесса торможения.
        """
        return f"Велосипед {self.brand} {self.model} тормозит."

    def __str__(self) -> str:
        """
        Возвращает строковое представление велосипеда для пользователя.

        Возвращает:
            str: Строковое представление велосипеда.
        """
        return (
            f"{self.__class__.__name__} {self.brand} {self.model}, {self.year} года выпуска, тип {self.bicycle_type}."
        )

    def move(self) -> str:
        """
        Описывает движение велосипеда.

        Перегружено для предоставления специфичного описания движения велосипеда.

        Возвращает:
            str: Описание движения велосипеда.
        """
        return f"Велосипед {self.brand} {self.model} движется легко и непринужденно."


if __name__ == "__main__":
    # Животные
    dog = Dog(name="Бадди", age=5, breed="Золотистый ретривер")
    cat = Cat(name="Вискес", age=3)
    bird = Bird(name="Твити", age=2, species="Канарейка")

    print(dog)
    print(repr(dog))
    print(dog.speak())
    print(dog.fetch("мяч"))
    print(dog.move())

    print()

    print(cat)
    print(repr(cat))
    print(cat.speak())
    print(cat.purr())
    print(cat.move())

    print()

    print(bird)
    print(repr(bird))
    print(bird.speak())
    print(bird.fly(20))
    print(bird.move())

    print("\n" + "-" * 50 + "\n")

    # Транспортные средства
    car = Car(brand="Тойота", model="Королла", year=2020, engine_type="Гибрид")
    bicycle = Bicycle(brand="Гигант", model="Escape 3", year=2021, bicycle_type="Дорожный")

    print(car)
    print(repr(car))
    print(car.drive(80))
    print(car.refuel(40))
    print(car.move())

    print()

    print(bicycle)
    print(repr(bicycle))
    print(bicycle.drive(25))
    print(bicycle.brake())
    print(bicycle.move())
