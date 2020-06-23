from drivers import Driver
from garage import Car
from functools import reduce


class Flight(object):
    def __init__(self, route: str):
        self.route = route
        self.status = "wait"
        self.driver = None

    # ANCHOR Запуск рейса

    def launch(self, driver: Driver, car: Car):
        driver.car = car
        self.driver = driver
        self.status = "in way"

    # ANCHOR Завершение рейса

    def finish(self):
        self.status = "completed"

    # ANCHOR Приостановка рейса

    def set_free(self):
        self.driver = None
        self.status = 'wait'

    def __str__(self):
        return f"Route: {self.route}\nStatus: {self.status}\nDriver =>\n {self.driver}\n"


class Flights(object):
    def __init__(self):
        self._flights = [
            Flight("Minsk -> Moscow"),
            Flight("Vitebsk -> Warsaw"),
            Flight("Kiev -> Grodno")
        ]

    def __len__(self):
        return len(self._flights)

    def __getitem__(self, position):
        return self._flights[position]

    def __str__(self):
        return reduce(lambda a, b: str(a)+str(b), self._flights)

    # ANCHOR Поиск рейса по водителю

    def search_by_driver(self, driver):
        return next((flight for flight in
                     self._flights if flight.driver == driver), None)
