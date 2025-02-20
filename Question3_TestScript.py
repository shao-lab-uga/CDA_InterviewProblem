import MyVehicleClass


# Sample Test Cases
def test_vehicle():
    car = MyVehicleClass.Car()
    minivan = MyVehicleClass.Minivan()
    truck = MyVehicleClass.Truck()

    current_speed = 20
    current_headway = 50
    relative_speed = 5

    print("Car Speed:", car.get_speed(current_speed, current_headway))
    print("Car Safety Score:", car.get_safe_score(current_headway, relative_speed))

    print("Minivan Speed:", minivan.get_speed(current_speed, current_headway))
    print("Minivan Safety Score:", minivan.get_safe_score(current_headway, relative_speed))

    print("Truck Speed:", truck.get_speed(current_speed, current_headway))
    print("Truck Safety Score:", truck.get_safe_score(current_headway, relative_speed))


# Run the test function
test_vehicle()

pass
