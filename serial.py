"""Python serial number generator."""


class SerialGenerator:
    """Generates random incrementing serial numbers"""

    def __init__(self, start=0):
        """Initializing starting serial number"""
        self.start = start
        self.current = start
    
    def generate(self):
        """Return next serial number"""
        self.current += 1
        return self.current - 1
    
    def reset(self):
        """Reset original start number"""
        self.current = self.start 

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next_num}>"



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
