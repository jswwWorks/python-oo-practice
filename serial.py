class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """Initializes starting value for serial numbers & current value"""
        self.current = start

        # This will be static
        self.start = start

        # set two variables to the same value in python:
        # self.current = self.start = start

    def __repr__(self):
        """Helpful way to see contents of class instance"""
        return (f"This is starting point for the serial num {self.start}")

    def generate(self):
        """Generate serial number from current value
        Additional serial numbers incremement by 1 from current value. """

        self.result = self.current # Just make this a variable and not a property

        # result = self.current
        # properties should be limited to the dunder init

        self.current += 1
        return self.result

    def reset(self):
        """Reset the serial number to initial start value."""
        self.current = self.start