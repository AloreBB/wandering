import random

class wandering:
    def __init__ (self,name):
        self.name = name
    
class comunWandering(wandering):
    def __init__(self,name):
        super().__init__(name)
        
    def walk():
        return random.choise([(0,1),(0.-1),(1,0),(-1,0)])