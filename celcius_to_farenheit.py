# define (parent) celsius class
class Celsius:

    # define initializing function
    def __init__(self):

        # by default set value to none
        self._value = None

    # sets value to passed in value from earlier
    def __get__(self, instance, owner):
        return self._value

    # checks for range error for conversion
    def __set__(self, instance, value):
        if not -273.15 <= value <= 1000:
            raise ValueError("Temperature must be between -273.15°C and 1000°C")
        self._value = value


# defines child class Temperature
class Temperature:

    # initiates parent class, this step make it a child class
    celsius = Celsius()

    # init function
    def __init__(self, celsius):

        # sets celsius as a native variable
        self.celsius = celsius

    # defines farenheit conversion and returns
    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32


if __name__ == "__main__":

    # call class and set as variable
    temperature = Temperature(20)

    # print results from our object
    print("Temperature in Celsius:", temperature.celsius)
    print("Temperature in Fahrenheit:", temperature.to_fahrenheit())
