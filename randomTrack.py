from wandering import ComunWandering
from track import Track
from location Location
from django.utils.translation import ugettext_lazy as _

from bokhe.plooting import figure, output_file, show

def walking(location, wandering, steps):
    beginning = location.getLocation(wandering)
    
    for _ in range(steps):
        location.move_wandering(wandering)
        
    return beginnig.distence(location.get_location)