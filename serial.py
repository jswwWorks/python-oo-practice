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
        """Initializes starting point for serial numbers"""
        self.current = start

        # This will be static
        self.start = start

    def generate(self):
        """Generate serial number, incrementing by 1."""
        self.result = self.current
        self.current += 1

        return self.result



    def reset(self):
        """Reset the serial number to initial value."""
        self.current = self.start

    def __repr__(self):
        return (f"This is starting point for the serial num {self.start}")


