from drivers import Driver, Drivers
from garage import Garage
from flights import Flights


class Dispatcher(object):
    def __init__(self):
        self.flights = Flights()
        self.drivers = Drivers()
        self.garage = Garage()
        self.distribute_applications()

    # ANCHOR Распределение рейсов

    def distribute_applications(self):
        for index, flight in enumerate(self.flights):
            if flight.status == "wait":
                driver = self.drivers.get_free()
                car = self.garage.get_free()
                if driver != None and car != None:
                    self.garage.remove(car)
                    self.drivers.remove(driver)
                    self.flights[index].launch(driver, car)

    # ANCHOR Обработка запроса на ремонт автомобиля

    def repair_request(self, driver: Driver):
        driver.car.on_repair = True
        self.garage.append(driver.car)
        driver.car = None
        self.flights.search_by_driver(driver).set_free()
        self.drivers.append(driver)

    # ANCHOR Отстранение водителя

    def remove_driver_from_work(self, driver: Driver):
        if driver.car != None:
            self.garage.append(driver.car)
            driver.car = None
            self.flights.search_by_driver(driver).set_free()
        driver.removed = True
        self.drivers.append(driver)

    # ANCHOR Отметить завершение рейса

    def flight_completed(self, driver: Driver):
        self.flights.search_by_driver(driver).finish()
        self.drivers.append(driver)
