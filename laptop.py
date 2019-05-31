class Machine_specs:
    def __init__(self, name, ram, hdd):
        self.__name = name
        self.__ram = ram
        self.__hdd = hdd

    # start of mutator/setter methods
    def set_name(self, name):
        self.__name = name

    def set_ram(self, ram):
        self.__ram = ram

    def set_hdd(self, hdd):
        self.__hdd = hdd

    # end mutator methods

    # start of getter method/accessor
    def get_name(self):
        return self.__name

    def get_ram(self):
        return self.__ram

    def get_hdd(self):
        return self.__hdd

    # end of getter method
