# File for all possible errors

class ArraySizeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class EmptyArrayError(Exception):
    def __init__(self, message):
        super().__init__(message)

class OutOfBoundsError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidBorderError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidModulo(Exception):
    def __init__(self, message):
        super().__init__(message)