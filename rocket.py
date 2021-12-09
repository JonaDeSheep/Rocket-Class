# Jonathan Chung
# Assignment 10.1: Your Own Class
# Purpose: To create a class that refills and burns fuel for a rocket, calculates the Thrust-to-Weight Ratio (TWR), returns the amount of fuel the rocket currently has, and returns the burn time as the rocket is burning all of its current fuel
# I received help from Cooper Cantrell (my roommate)
class Rocket:
    
    # This class variable "dry_weight" stores a number that represents the rocket's dry weight
    dry_weight = 2000
    # This class variable "fuel_density" stores a number that represents the rocket's fuel density
    fuel_density = 1
    def __init__(self):
        # This data variable "self.__fuel_level" stores a number that represents the rocket's fuel level
        self.__fuel_level = 20000
        # This data variable "self.__burn_rate" stores a number that represents the rocket's burn rate
        self.__burn_rate = 100
        # This data variable "self.__thrust" stores a number that represents the rocket's thrust
        self.__thrust = 25000
    
    def refuel(self,fuel):
        
        # This data variable "max" stores a number of the maximum fuel level the rocket can take in
        max = 20000
        # If the starting fuel level and the added fuel is greater than the maximum fuel limit the rocket can take in . . .
        # Then the program will print that the user overfilled the rocket's fuel level by the extra amount of rocket fuel they poured in
        # The program would also set the rocket's fuel level to the maximum limit number
        if self.__fuel_level + fuel > max:
            print(f"You overfilled by {(self.__fuel_level + fuel) - max} units of fuel.")
            self.__fuel_level = max
        # Else, the rocket's fuel level would be added by the newly poured fuel level
        else:
            self.__fuel_level += fuel
        # Returns the final rocket's fuel level
        return self.__fuel_level
    
    def get_fuel(self):
        # Returns the current rocket's fuel level
        return self.__fuel_level
    
    def burn(self,time):
        # This data variable "min" stores a number of the minimum fuel level the rocket can take in
        min = 0
        # The rocket's fuel level would be substracted by the product of the rocket's burn rate and the amount of time the rocket burned fuel
        self.__fuel_level -= time * self.__burn_rate
        # If the rocket's fuel level is less than 0, which is the minimum fuel level the rocket can take in . . .
        # Then, the program would print that the user overburned the rocket, in seconds, by the extra amount of fuel it had burned past the minimum level
        # The program would also set the rocket's fuel level to the minimum limit number
        if self.__fuel_level < 0:
            print(f"You overburned by {self.__fuel_level / -(self.__burn_rate)} seconds.")
            self.__fuel_level = min
        # Else, the program skips this else statement
        else:
            pass
        # Returns the final rocket's fuel level
        return self.__fuel_level
    
    def TWR(self):
        # This data variable "weight" stores the answer to the equation: The rocket's dry weight added by the product of the rocket's fuel density and fuel level
        weight = self.dry_weight + (self.fuel_density * self.__fuel_level)
        # This data variable "TWR" stores the answer to the equation: The rocket's thrust divided by the weight of the rocket
        TWR = self.__thrust / weight
        # Returns the final outcome of the variable "TWR"
        return TWR

    def burn_time(self):
        # Returns the outcome to the equation: The rocket's fuel level divided by the burn rate (which gives the fuel burning time of the rocket)
        return self.__fuel_level/self.__burn_rate

def main():
    
    # This variable stores the class "Rocket()"
    x = Rocket()
    # While the TWR is less than the fixed operand measured in Newtons, the current fuel level will be repeatedly burned with time set as 1 which will increase the TWR
    # The main function is able to access the TWR method from the class "Rocket" by using the syntax "object_name.data_attribute_name", with the "object_name" being the class "Rocket" and the "data_attribute_name" being the method "TWR()"
    # With this accessed method, the while loop will be able to check to see if the returned value from the method "TWR()" is less than the fixed operand
    # If the equation returns True, then the while loop will activate the line of code "x.burn(1)", which accesses the "burn" method from the class "Rocket" using the same syntax along with its passed numeric argument "1"
    while x.TWR() < 2.2:
        x.burn(1)
    # While the TWR is greater than the fixed operand measured in Newtons, the current fuel level will be repeatedly poured with the added fuel set as 1 which will decrease the TWR
    # The main function is able to access the TWR method from the class "Rocket" by using the syntax "object_name.data_attribute_name", with the "object_name" being the class "Rocket" and the "data_attribute_name" being the method "TWR()"
    # With this accessed method, the while loop will be able to check to see if the returned value from the method "TWR()" is greater than the fixed operand
    # If the equation returns True, then the while loop will activate the line of code "x.refuel(1)", which accesses the "refuel" method from the class "Rocket" using the same syntax along with its passed numeric argument "1"
    while x.TWR() > 2.2:
        x.refuel(1)
    # Prints the rocket's TWR
    # The main function is able to access the TWR method from the class "Rocket" by using the syntax "object_name.data_attribute_name", with the "object_name" being the class "Rocket" and the "data_attribute_name" being the method "TWR()"
    # The returned value of the accessed method "TWR()" will appear at the end of the printed string
    print(f"The rocket's TWR is {x.TWR()}")
    # Prints the rocket's current fuel level
    # The main function is able to access the get_fuel method from the class "Rocket" by using the syntax "object_name.data_attribute_name", with the "object_name" being the class "Rocket" and the "data_attribute_name" being the method "get_fuel()"
    # The returned value of the accessed method "get_fuel()" will appear at the end of the printed string
    print(f"The rocket's current fuel level is {x.get_fuel()}")
    # Prints the rocket's burn time
    # The main function is able to access the burn_time method from the class "Rocket" by using the syntax "object_name.data_attribute_name", with the "object_name" being the class "Rocket" and the "data_attribute_name" being the method "burn_time()"
    # The returned value of the accessed method "burn_time()" will appear at the end of the printed string
    print(f"The amount of time for the rocket to burn all of its fuel is {x.burn_time()}")

# The main function executes here
if __name__ == '__main__':
    main()