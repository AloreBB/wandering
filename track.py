class track:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def move(self, delta_x, delta_y):
        return track(self.x + delta_x, self.y + delta_y)
    
    def distancie