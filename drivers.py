from functools import reduce


class Driver(object):
    def __init__(self, name):
        self.name = name
        self.removed = False
        self.car = None

    def set_car(self, car):
        self.car = car

    def remove_car(self):
        self.car = None

    # ANCHOR Отправить заявку на ремонт

    def send_car_for_repair(self, dispatcher):
        if (self.car != None):
            dispatcher.repair_request(self)

    # ANCHOR Завершить рейс и отметить состояние автомобиля

    def complete_flight(self, dispatcher, car_status):
        self.car.status = car_status
        dispatcher.flight_completed(self)

    def __str__(self):
        return f"Name: {self.name}, Removed: {self.removed},\n Car => {self.car}\n"


class Drivers(object):
    def __init__(self):
        self._drivers = [
            Driver('Leonardo'),
            Driver('Donatella'),
            Driver('Mikelangelo'),
            Driver('Rafael')
        ]

    def __len__(self):
        return len(self._drivers)

    def __getitem__(self, position):
        return self._drivers[position]

    def __str__(self):
        return reduce(lambda a, b: str(a)+str(b), self._drivers)

    def append(self, driver: Driver):
        self._drivers.append(driver)

    def remove(self, driver: Driver):
        self._drivers.remove(driver)

    # ANCHOR Поиск свободного водителя

    def get_free(self):
        return next((driver for driver in
                     self._drivers if driver.removed == False), None)
