import VehicleClass
import numpy as np

# Sample Test Cases
def test_vehicle():
    car = VehicleClass.Car()
    minivan = VehicleClass.Minivan()
    truck = VehicleClass.Truck()

    # # Test cases for get_next_speed
    car_speeds = np.array([10, 30, 50])
    car_headways = np.array([5, 10, 20])
    print("Car Speed Test Cases:", car.get_next_speed(car_speeds, car_headways))
    
    # Minivan test cases
    minivan_speeds = np.array([10, 25, 40])
    minivan_headways = np.array([5, 10, 20])
    print("Minivan Speed Test Cases:", minivan.get_next_speed(minivan_speeds, minivan_headways))
    
    # Truck test cases
    truck_speeds = np.array([10, 20, 35])
    truck_headways = np.array([5, 10, 20])
    print("Truck Speed Test Cases:", truck.get_next_speed(truck_speeds, truck_headways))

    # Test cases for get_safe_score
    current_headway = np.array([0.5, 2, 3, 10])
    relative_speed = np.array([1, 2, 2, -1]) # Cover no risk, high risk, moderate risk, safe
    print("Car Safety Score:", car.get_safe_score(current_headway, relative_speed))
    print("Minivan Safety Score:", minivan.get_safe_score(current_headway, relative_speed))
    print("Truck Safety Score:", truck.get_safe_score(current_headway, relative_speed))


if __name__ == "__main__":
    test_vehicle()

