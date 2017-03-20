import ModuleX.Car as Car
from typing import List
class Person:
	def __init__(self, name:str, cars:List[Car]=None):
		self.name = name #type:Str
		self.cars = cars if cars != None else list() #type: List[Car]

	def get_cars(self)-> List[Car]:
		return self.cars

	def add_car(self, car:Car):
		return self.cars.append(car)

if __name__ == '__main__':
	pass