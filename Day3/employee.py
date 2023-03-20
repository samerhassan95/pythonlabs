from person import Person
import re
from car import Car

class Employee(Person):

    def __init__(self,name,money,id,car,distanceToWork):
        super(Employee,self).__init__(name,money)
        self.id = id
        self.car = None
        self.distanceToWork = distanceToWork
        self.__salary=1000
        self.__mail=None
    def work(self,hours):
        if (hours==8):
            self._mood='happy'
        elif (hours>8):
            self._mood='tired'
        else:
            self._mood='lazy'

    def drive(self, distance):
        if self._car.fuelRate == 0:
            self.refuel()
        self._car.run(distance, self._car.velocity)

    def refuel(self,gasAmount=100):
        self._car.fuelRate(gasAmount)

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self,newSalary):
        if(newSalary<1000):
            print('cannot be under 1000')
        else:
            self.__salary=newSalary

    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self,newMail):
        pattern=r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if(re.fullmatch(pattern,newMail)):
            self.__mail=newMail
        else:
            print('email not matched')