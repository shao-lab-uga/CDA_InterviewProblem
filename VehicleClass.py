import numpy as np

class Vehicle:
    def __init__(self, mass, max_speed, max_acceleration):
        """
        Base class for all vehicles.
        :param mass: Mass of the vehicle (kg)
        :param max_speed: Maximum speed (m/s)
        :param acceleration: Acceleration (m/s²)
        :param headway: Distance to the leading vehicle (m)
        :param relative_speed: Speed difference with the leading vehicle (m/s)
        """
        self.mass = mass
        self.max_speed = max_speed
        self.max_acceleration = max_acceleration

    def get_next_speed(self, current_speed, current_headway):
        """
        Determines the vehicle's next speed using the car-following model:
        current_acceleration = a_max * (1 - (v / v_max)^4 - ((2 + 2*v) / s)^2)
        :param current_speed: Current speed (m/s), can be float or numpy array
        :param current_headway: Current headway/gap (m), can be float or numpy array
        :return: Next speed (m/s), same type as inputs
        """
        # Calculate current acceleration using the formula
        current_acceleration = self.max_acceleration * (
            1 - np.power(np.maximum(current_speed, 0) / self.max_speed, 4) -
            np.power((2 + 2 * np.maximum(current_speed, 0)) / np.maximum(current_headway, 0.1), 2)
        )
        current_acceleration = np.clip(current_acceleration, -self.max_acceleration, self.max_acceleration)
        # Update speed using Euler integration (dt = 1s)
        next_speed = current_speed + current_acceleration
        
        # Ensure speed stays within bounds
        next_speed = np.clip(next_speed, 0, self.max_speed)
        
        return next_speed


    def get_safe_score(self, headway, relative_speed):
        """
        Computes the safety score based on Time-to-Collision (TTC).
        :param headway: Current headway/gap (m), can be float or numpy array
        :param relative_speed: Speed difference with the leading vehicle (m/s), can be float or numpy array
        :return: Safety score (0, 50, 100), same type as inputs
        """
        
        # Compute TTC where relative_speed > 0
        ttc = np.divide(headway, relative_speed, where=relative_speed>0)

        # Assign safety scores
        score = np.where(ttc > 3, 100, 0)
        score = np.where((ttc >= 1) & (ttc <= 3), 50, score)

        score = np.where(ttc < 1, 0, score)
        # No risk if not approaching, relative_speed <= 0 then score = 100
        score = np.where(relative_speed <= 0, 100, score)
        return score


# Subclasses for different vehicle types
class Car(Vehicle):
    def __init__(self):
        super().__init__(mass=1500, max_speed=53.6448, max_acceleration=8)


class Minivan(Vehicle):
    def __init__(self):
        super().__init__(mass=3000, max_speed=44.704, max_acceleration=5)


class Truck(Vehicle):
    def __init__(self):
        super().__init__(mass=8000, max_speed=35.7632, max_acceleration=3)

