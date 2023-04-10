#Aseel Ibrahim

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def get_automobile_input():
    print("Lets get some information")
    year = input("What year was the car made? ")
    make = input("What brand is the car? ")
    model = input("What is the model of the car? ")
    doors = input("How many doors does the car have (2 or 4)? ")
    roof = input("Does the car have a solid or sun roof? ")

    automobile = Automobile("car", year, make, model, doors, roof)
    return automobile


def print_automobile_info(automobile):
    print("Here is the information about your car:")
    print("Type: " + automobile.vehicle_type)
    print("Year: " + automobile.year)
    print("Make: " + automobile.make)
    print("Model: " + automobile.model)
    print("Number of doors: " + automobile.doors)
    print("Roof type: " + automobile.roof)


if __name__ == "__main__":
    automobile = get_automobile_input()
    print_automobile_info(automobile)