class location:
    
    def __init__(self):
        self.location_wandering = {}
        
    def add_wandering(self, wandering, track):
        self.location_wandering[wanderings] = track
        
    def move_wandering(self, wardering):
        delta_x, delta_y = wandering.walk()
        location_now = self.location_wandering[wandering]
        new_location = location_now.move(delta_x, delta_y)
        
        self.location_wandering[wandering] = new_location

    def get_location(self, wandering):
        return self.location_wandering[wandering]