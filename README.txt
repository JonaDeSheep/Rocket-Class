Class Description: The purpose of the class “Rocket” is to perform these specific tasks that involve the interaction with a rocket: Refill the fuel, burn the fuel, calculate and return the Thrust-to-Weight ratio (TWR), calculate and return the fuel burning time, and return the current fuel level. These functions are important as they all return statistical results that would allow scientists to determine how to make their rocket fly efficiently without much room for error.


Class and Data Variables Descriptions: 

There are two class variables in the class “Rocket”: “dry_weight” and “fuel_density”

“dry_weight” stores an operand that represents the rocket’s dry weight
“fuel_density” stores an operand represents the rocket’s fuel density

There are 3 data variables in the class “Rocket”: “self.__fuel_level”, “self.__burn_rate”, and “self.__thrust”

“self.__fuel_level” stores an operand represents the rocket’s starting fuel level
“self.__burn_rate” stores an operand represents the rocket’s burn rate
“self.__thrust” stores an operand represents the rocket’s thrust


Methods Descriptions:

The method “refuel()” requires an argument called “fuel”, which stores an operand that represents the additional fuel level that will be poured into the rocket’s fuel tank, and the argument “self”. This “fuel” will be added into the rocket’s current fuel level and the method would set the new fuel level equal to the maximum capacity of the fuel tank (which is represented as “max”) only if the added fuel overflows the rocket’s fuel tank. This method would return the new fuel level of the rocket.

The method “get_fuel()” only requires the argument “self”. This method returns the current fuel level of the rocket.

The method “burn()” requires an argument called “time”, which stores an operand that represents the amount of seconds the rocket burned its fuel, and the argument “self”. This “time” will be multiplied by the burn rate of the rocket and then the rocket’s fuel level will be subtracted by the answer to the product. This method would then set the new fuel level equal to the minimum capacity of the fuel tank (which is represented as “min”) only if the fuel tank overburns and this method returns the new fuel level.

This method “TWR()” only requires the argument “self”. Within this method, the variable “weight” will store the answer to the equation: the rocket’s dry weight added by the product of the rocket’s fuel density and fuel level. This method returns the answer to the quotient of the rocket’s thrust and its weight, which is the rocket’s TWR.

This method “burn_time()” only requires the argument “self”. This method returns the quotient of the rocket’s fuel level and its burn rate, which is the amount of time in seconds the rocket would take to burn all of its fuel.


Demo Program Description: In this demo program, scientists from a space station are testing how much fuel must be given to the rocket in order to achieve the desired TWR that the rocket must precisely reach. For this situation, the desired TWR the scientists want the rocket to reach is 2.2 Newtons. In order to know how much fuel the rocket must hold, the scientists use a test machine that closely approximates the amount of fuel the rocket needs to reach towards this TWR by using the methods of burning the fuel and refueling the fuel tank. To demonstrate this test machine scenario, the main function uses a while loop to check and see if the rocket’s current TWR is less than 2.2 Newtons. If the equation results in being true, then the while loop will continuously activate the burn method from the class “Rocket”, which will continuously deplete the fuel level of the rocket until the equation is dissatisfied. The main function can skip this entire while loop if the equation returns False when first executed and moves on to the next while loop. This statement checks to see if the TWR of the rocket is greater than 2.2. If the equation results in being true, then the while loop will continuously activate the refuel method from the class “Rocket”, which will continuously add to the fuel level of the rocket until the equation is dissatisfied. This process of either refueling and burning fuel will continue until the rocket’s TWR is closely approximated to 2.2. Afterwards, the main function will print the rocket’s TWR, current fuel, and burn time.


Instructions: To run the demo program, in the while loops, the user can set the operand that represents the projected TWR level the rocket must reach to any number they sought to enter except for negative numbers and can also set the arguments in “x.burn()” and “x.refuel()” located inside the while loops as any number they sought to enter except for negative numbers (however, this action is not recommended as a higher number than 1 does lead to a more inaccurate result). Once the user finishes entering their desired operands into the demo program, the program will be ready to run in the terminal.
