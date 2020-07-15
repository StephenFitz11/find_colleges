import requests


def query_maps(query_string):
    """Takes a string, formats it and querys google places API"""
    input_formatted = query_string.replace(" ", "%")
    base_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={input_formatted}&inputtype=textquery" \
               "&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="
    api_key = "AIzaSyAOrDZfZisyJ5bUTtXysK9Td2r3Gpvx9Qw"
    r = requests.get(base_url + api_key)
    return r.json()



