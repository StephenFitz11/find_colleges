from math import radians, cos, sin, asin, sqrt
import hub_coord as hc


# the haversine formula for finding th miles between two sets of lat & longs
def haversine(lon1, lat1, lon2, lat2):
    """returns distance in miles"""
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth in miles
    return c * r

# returns the closest hub as ['hub', int(distance)]
# hub locations based on separate file not included in project. imported from hub_coord
def find_hub(input_lat, input_long):
    """Return the closest hub to the input lat/long"""
    hub_lat_longs = hc.hub_lat_longs

    distances = 1000000000
    city = ''
    for place in hub_lat_longs:
        distance = haversine(input_long, input_lat, hub_lat_longs[place][1], hub_lat_longs[place][0])
        if distance < distances:
            distances = distance
            city = place

    return [city, round(distances)]

