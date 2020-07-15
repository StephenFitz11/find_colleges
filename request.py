import requests
import csv

api_key = "AIzaSyAOrDZfZisyJ5bUTtXysK9Td2r3Gpvx9Qw"

csv_path = "G:\college_finder_py\colleges.csv"
file = open(csv_path, newline='')
reader = csv.reader(file)

header = next(reader)
colleges = [row for row in reader]



for college in colleges[:2]:
    college_name_formatted = college[1].replace(" ", "%")
    base_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={college_name_formatted}&inputtype=textquery" \
               "&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="

    # r = requests.get(base_url + api_key)
    # data = r.json()
    # print(data)

    print(college[:25])











