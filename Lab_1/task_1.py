class SpaceShip:
    """
    Класс, описывающий космический корабль.

    Атрибуты:
        name (str): Название корабля.
        fuel_level (float): Уровень топлива в процентах.
        capacity (int): Вместимость корабля в тоннах.

    Пример:
        >>> ship = SpaceShip("Enterprise", 75.0, 100)
        >>> ship.name
        'Enterprise'
    """

    def __init__(self, name: str, fuel_level: float, capacity: int):
        self.name: str = name
        if not (0.0 <= fuel_level <= 100.0):
            raise ValueError("Уровень топлива должен быть между 0 и 100.")
        self.fuel_level: float = fuel_level
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом.")
        self.capacity: int = capacity

    def launch(self) -> str:
        """
        Запускает корабль, если топлива достаточно.

        Возвращает:
            str: Сообщение о запуске.

        Пример:
            >>> ship = SpaceShip("Enterprise", 75.0, 100)
            >>> ship.launch()
            'Корабль Enterprise успешно запущен.'
        """
        if self.fuel_level < 50.0:
            return f"Недостаточно топлива для запуска корабля {self.name}."
        self.fuel_level -= 50.0
        return f"Корабль {self.name} успешно запущен."

    def refuel(self, amount: float) -> None:
        """
        Заправляет корабль заданным количеством топлива.

        Аргументы:
            amount (float): Количество топлива для заправки. Должно быть положительным и не превышать 100.

        Пример:
            >>> ship = SpaceShip("Enterprise", 75.0, 100)
            >>> ship.refuel(10.0)
            >>> ship.fuel_level
            85.0
        """
        if amount <= 0.0:
            raise ValueError("Количество топлива для заправки должно быть положительным.")
        if self.fuel_level + amount > 100.0:
            raise ValueError("Уровень топлива не может превышать 100%.")
        self.fuel_level += amount

    def get_status(self) -> str:
        """
        Возвращает текущий статус корабля.

        Возвращает:
            str: Статус корабля.

        Пример:
            >>> ship = SpaceShip("Enterprise", 75.0, 100)
            >>> ship.get_status()
            'Корабль Enterprise: Топливо - 75.0%, Вместимость - 100 тонн.'
        """
        return f"Корабль {self.name}: Топливо - {self.fuel_level}%, Вместимость - {self.capacity} тонн."


class VirtualPet:
    """
    Класс, описывающий виртуального питомца.

    Атрибуты:
        name (str): Имя питомца.
        hunger (int): Уровень голода (0-100).
        happiness (int): Уровень счастья (0-100).

    Пример:
        >>> pet = VirtualPet("Fluffy", 50, 70)
        >>> pet.name
        'Fluffy'
    """

    def __init__(self, name: str, hunger: int, happiness: int):
        self.name: str = name
        if not (0 <= hunger <= 100):
            raise ValueError("Уровень голода должен быть между 0 и 100.")
        self.hunger: int = hunger
        if not (0 <= happiness <= 100):
            raise ValueError("Уровень счастья должен быть между 0 и 100.")
        self.happiness: int = happiness

    def feed(self, amount: int) -> None:
        """
        Кормит питомца, уменьшая уровень голода.

        Аргументы:
            amount (int): Количество еды. Должно быть положительным.

        Пример:
            >>> pet = VirtualPet("Fluffy", 50, 70)
            >>> pet.feed(20)
            >>> pet.hunger
            30
        """
        if amount <= 0:
            raise ValueError("Количество еды должно быть положительным.")
        self.hunger = max(self.hunger - amount, 0)

    def play(self, duration: int = 30) -> None:
        """
        Играет с питомцем, увеличивая уровень счастья и голода.

        Аргументы:
            duration (int, по умолчанию 30): Длительность игры в минутах. Должна быть положительной.

        Пример:
            >>> pet = VirtualPet("Fluffy", 50, 70)
            >>> pet.play(20)
            >>> pet.happiness
            90
        """
        if duration <= 0:
            raise ValueError("Длительность игры должна быть положительной.")
        self.happiness = min(self.happiness + duration, 100)
        self.hunger = min(self.hunger + duration // 2, 100)

    def get_status(self) -> str:
        """
        Возвращает текущий статус питомца.

        Возвращает:
            str: Статус питомца.

        Пример:
            >>> pet = VirtualPet("Fluffy", 50, 70)
            >>> pet.get_status()
            'Fluffy: Голод - 50, Счастье - 70.'
        """
        return f"{self.name}: Голод - {self.hunger}, Счастье - {self.happiness}."


class Cryptocurrency:
    """
    Класс, описывающий криптовалюту.

    Атрибуты:
        name (str): Название криптовалюты.
        symbol (str): Символ криптовалюты.
        market_cap (float): Рыночная капитализация в миллиардах долларов.

    Пример:
        >>> crypto = Cryptocurrency("Bitcoin", "BTC", 800.0)
        >>> crypto.name
        'Bitcoin'
    """

    def __init__(self, name: str, symbol: str, market_cap: float):
        self.name: str = name
        self.symbol: str = symbol
        if market_cap < 0.0:
            raise ValueError("Рыночная капитализация не может быть отрицательной.")
        self.market_cap: float = market_cap

    def update_market_cap(self, new_cap: float) -> None:
        """
        Обновляет рыночную капитализацию криптовалюты.

        Аргументы:
            new_cap (float): Новая рыночная капитализация. Должна быть неотрицательной.

        Пример:
            >>> crypto = Cryptocurrency("Bitcoin", "BTC", 800.0)
            >>> crypto.update_market_cap(850.0)
            >>> crypto.market_cap
            850.0
        """
        if new_cap < 0.0:
            raise ValueError("Рыночная капитализация не может быть отрицательной.")
        self.market_cap = new_cap

    def get_symbol(self) -> str:
        """
        Возвращает символ криптовалюты.

        Возвращает:
            str: Символ криптовалюты.

        Пример:
            >>> crypto = Cryptocurrency("Bitcoin", "BTC", 800.0)
            >>> crypto.get_symbol()
            'BTC'
        """
        return self.symbol

    def convert_to_usd(self, amount: float, rate: float = 1.0) -> float:
        """
        Конвертирует количество криптовалюты в доллары США.

        Аргументы:
            amount (float): Количество криптовалюты. Должно быть положительным.
            rate (float, по умолчанию 1.0): Курс обмена. Должен быть положительным.

        Возвращает:
            float: Эквивалент в долларах США.

        Пример:
            >>> crypto = Cryptocurrency("Bitcoin", "BTC", 800.0)
            >>> crypto.convert_to_usd(2, 50000.0)
            100000.0
        """
        if amount < 0.0:
            raise ValueError("Количество криптовалюты не может быть отрицательным.")
        if rate <= 0.0:
            raise ValueError("Курс обмена должен быть положительным.")
        return amount * rate
