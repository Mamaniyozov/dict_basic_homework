def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """ 
towns = [{'name': 'Manchester', 'population': 58241}, 
         {'name': 'Coventry', 'population': 12435}, 
         {'name': 'South Windsor', 'population': 25709}]

names       = []
populations = []

for town in towns:
    names.append(town["name"])
    populations.append(town["population"])

print("Name of towns in the city are:", names)
print("Population of each town in the city are:", populations)