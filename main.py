# ----------------------------------------------------------
# 5. Задача на взаимодействие между классами. Разработать систему «Автобаза». 
# Диспетчер распределяет заявки на Рейсы между Водителями и назначает для этого Автомобиль. 
# Водитель может сделать заявку на ремонт. 
# Диспетчер может отстранить Водителя от работы. 
# Водитель делает отметку о выполнении Рейса и состоянии Автомобиля. 
# ----------------------------------------------------------
from dispatcher import Dispatcher

dispatcher1 = Dispatcher()

print(dispatcher1.flights)
dispatcher1.remove_driver_from_work(dispatcher1.flights[0].driver)
dispatcher1.flights[1].driver.send_car_for_repair(dispatcher1)
dispatcher1.distribute_applications()
dispatcher1.flights[0].driver.complete_flight(dispatcher1, True)
print(dispatcher1.flights)
