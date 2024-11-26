from task_1 import SpaceShip, VirtualPet, Cryptocurrency

if __name__ == "__main__":
    try:
        ship = SpaceShip("Enterprise", 75.0, 100)
        ship.refuel(-10.0)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        pet = VirtualPet("Fluffy", 50, 70)
        pet.play(-5)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        crypto = Cryptocurrency("Bitcoin", "BTC", 800.0)
        crypto.convert_to_usd(-2, -50000.0)
    except ValueError:
        print('Ошибка: неправильные данные')
