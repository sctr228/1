import random


# class Human:
#     def __init__(self, name='Human'):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passenger(self, human):
#         self.passengers.append(human)
#
#     def print_passengers_names(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers:")
#             for passenger in self.passengers:
#                 print(passenger.name)
#         else:
#             print(f"There are no passengers in {self.brand}")
#
#
# petya = Human('Petya')
# mari = Human('Mari')
# car = Auto('Mercedes')
#
# car.add_passenger(petya)
# car.add_passenger(mari)
# car.print_passengers_names()


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House(house_list)

    def get_pet(self):
        self.pet = Pet(pet_list)

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 10
            self.home.food -= self.pet.food_less

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I bought delicacies')
            self.money -= 15
            self.gladness += 10
            self.satiety += 2
    def chill(self):
        self.gladness += self.house.gladness_adds
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = 'home indexes'
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"fuel - {self.car.fuel}")
        print(f"strength - {self.car.strength}")


    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        elif self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bunkrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
            print(f'I bought a home {self.home.house}')
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f'I don`t have a job, going to get a job {self.job.job} with salary {self.job.salary}')
        if self.pet is None:
            self.get_pet()
            print(f'I bought a pet {self.pet.pet}')
        self.days_indexes(day)
        dice = random.randint(1, 4)

        if self.satiety < 20:
            print(f'I`ll go eat and feed my {self.pet.pet}')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I want to chill, but there is so much mess... \n So I will clean the house')
                self.clean_home()
            else:
                print('Let`s chill')
                self.chill()
        elif self.money < 0:
            print('Start working')
            self.work()
        elif self.car.strength < 15:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print('Let`s chill')
            self.chill()
        elif dice == 2:
            print('Let`s work')
        elif dice == 3:
            print('Cleaning time')
        elif dice == 4:
            print('Time to treats!')
            self.shopping(manage='delicacies')




class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
    def __init__(self, house_list):
        self.house = random.choice(list(house_list))
        self.gladness_adds = house_list[self.house]['gladness_adds']

class Pet:
    def __init__(self, pet_list):
        self.pet = random.choice(list(pet_list))
        self.gladness_adds = pet_list[self.pet]['gladness_adds']


job_list = {
    'Java developer': {'salary': 50, 'gladness_less': 10},
    'Python developer': {'salary': 40, 'gladness_less': 3},
    'C++ developer': {'salary': 45, 'gladness_less': 25},
    'Rust developer': {'salary': 70, 'gladness_less': 1},
}
brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
    'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}
house_list = {
    'Flat': {'gladness_adds': 6},
    'House': {'gladness_adds': 8},
    'Two-story house': {'gladness_adds': 10},
    'Flat in the city center': {'gladness_adds': 12},
}
pet_list = {
    'Cat': {'gladness_adds': 6, 'food_less': 5},
    'Dog': {'gladness_adds': 4, 'food_less': 8},
    'Fish': {'gladness_adds': 3, 'food_less': 3},
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


nick = Human(name='Nick')

for day in range(1, 8):
    if nick.live(day) == False:
        break