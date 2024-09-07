class Car:
    
    color = None
    name = None
    no_of_wheels = None

    def __init__(self, color, name, no_of_wheels)   :
        self.color = color
        self.name = name
        self.no_of_wheels = no_of_wheels

    def drive(self):
        print("dfs")
