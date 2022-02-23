from wandering import comunWandering
from track import Track
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    beginning = location.get_location(wandering)
    
    for _ in range(steps):
        location.move_wandering(wandering)
        
    return beginnging.distance(location.get_location(wandering))

def simulate_walk(steps, number_attemps_, type_wandering):
    wandering = type_wandering(name = 'Kayn')
    origen = Track(0,0)
    
    for _ in range(number_attemps):
        location = location()
        location.add_wandering(wandering, origen)
        simulations_walk = walking(location, wandering, steps)
        distances.append(round((simulations_walk, 1)))
    return distances

def graph(x, y):
    graphics = figure(tittle='Camino del errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x.y, legend='Distancia')
    show(graphics)
    
def main(distances_walk, numbet_attemps, type_wandering):
    average_walks_distance = []
    
    for steps in distances_walk:
        distances = simulate_walk(steps, number_attemps_, type_wandering)
        middle_distances = round(sum(distances) / len(distances), 4)
        max_distance = round(distances)
        min_distance = round(distances)
        average_walks_distance.append(middle_distance)
        
        print(f'{wandering.type_wandering.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {middle_distances}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')
    graph(distances_walk, average_walks_distance)
    
    if __name__ == '__main':
        distances_walk = [10,100,1000,1000]
        numbet_attemps = 10 
        main(distances_walk, numbet_attemps, comunWandering(name))
    