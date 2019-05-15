class Square(object):

    VESI = 0
    TASANKO = 1
    METSA = 2
    AAVIKKO = 3
    VUORISTO = 4
    
    def __init__(self, type):
        self._set_type(type)

    def get_type(self):
        return self._type

    def _set_type(self, type):
        if type in [Square.VESI, Square.TASANKO, Square.METSA, Square.AAVIKKO, Square.VUORISTO]:
            self._type = type
        else:
            raise ValueError("Vaara maaston tyyppi")

    type = property(get_type)