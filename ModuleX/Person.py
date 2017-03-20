from typing import List

MYPY = False
if MYPY:
    import ModuleX.Car as Car


class Person:

    def __init__(self, name: str, cars: List['Car.Car'] = None) -> None:
        self.name = name  # type: str
        self.cars = cars if cars != None else list()  # type: List[Car.Car]

    def get_cars(self) -> List['Car.Car']:
        return self.cars

    def add_car(self, car: 'Car.Car'):
        return self.cars.append(car)
