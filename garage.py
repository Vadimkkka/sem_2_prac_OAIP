from functools import reduce


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.status = True
        self.on_repair = False

    def __str__(self):
        return f"Color: {self.color}, brand: {self.brand}, Status: {self.status}, On repair: {self.on_repair}"


class Garage:
    def __init__(self):
        self._cars = [
            Car('white', 'Porsche'),
            Car('red', 'BMW'),
            Car('brown', 'Mercedes'),
            Car('yellow', 'Lamborgini'),
        ]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]

    def __str__(self):
        return reduce(lambda a, b: str(a)+str(b), self._cars)

    def append(self, car: Car):
        self._cars.append(car)

    def remove(self, car: Car):
        self._cars.remove(car)

    # ANCHOR Поиск свободного автомобиля

    def get_free(self):
        return next((car for car in
                     self._cars if car.on_repair == False), None)
