# Possibly errors that may occur.

class InvalidNumofNodesError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidNodeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidWeightError(Exception):
    def __init__(self, message):
        super().__init__(message)