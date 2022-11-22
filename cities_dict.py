def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """ 
    
    return["{}: {}".format(str(i+1), c) for i,c in enumerate(cities)]
print(cities_dict([' Samarkand', ' Tashkent', ' Moscow', 'Buenos Aires', 'New York']))