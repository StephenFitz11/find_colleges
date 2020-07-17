import requests
import config as cf


def query_maps(query_string):
    """Takes a string, formats it and queries the Google Places API"""
    # replaces spaces with % for the query string
    input_formatted = query_string.replace(" ", "%")

    # base url for querying the Places API
    base_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={input_formatted}&inputtype=textquery" \
               "&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="
    # makes the request and returns the JSON
    r = requests.get(base_url + cf.API_key)
    return r.json()


