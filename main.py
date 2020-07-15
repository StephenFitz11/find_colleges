import pandas as pd
import numpy as np

import query_request as q

df = pd.read_excel("colleges_excel.xlsx")
df2 = df.head(1)


# inserts column after column 2 with no values
df2.insert(2, "address", "")
df2.insert(3, "city", "")
df2.insert(4, "state", "")
df2.insert(5, "zip", "")
df2.insert(6, "nearest_hub", "")
df2.insert(6, "miles", np.nan)
test_query = {'candidates': [{'formatted_address': '1616 McCormick Dr, Largo, MD 20774, United States', 'geometry': {'location': {'lat': 38.91265, 'lng': -76.847599}, 'viewport': {'northeast': {'lat': 38.91400772989272, 'lng': -76.84637122010727}, 'southwest': {'lat': 38.91130807010727, 'lng': -76.84907087989272}}}, 'name': 'University of Maryland Global Campus', 'photos': [{'height': 4160, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111893958710339021352">Jesse Varsalone</a>'], 'photo_reference': 'CmRaAAAA83UBJs4sByTWNXUxuPc5C800INKMzaLRL5K-R0Uk3czjMIEdXuM-DZ5XgtrhKQ0T4Nz7jeHff1q-07jXbvt1PlVLFZmhV4vhH5RliTjgXzVbt_xJrwBcbQxOP0wQzfSGEhCWMK8aOLBwGIDOcvhxJLewGhSU4p4GnwUwy-E8FgKWhk9CS9XwqQ', 'width': 2340}], 'rating': 3}], 'status': 'OK'}

indexer = 0
for college in range(len(df2)):
    # query = q.query_maps(df2.at[college, 'institution_name'])
    print(test_query)
    deconstructed_address = test_query["candidates"][0]['formatted_address'].split(',')
    df2.at[college, "address"] = deconstructed_address[0]
    df2.at[college, "city"] = deconstructed_address[1]
    df2.at[college, "state"] = deconstructed_address[2].split(" ")[1]
    df2.at[college, "zip"] = deconstructed_address[2].split(" ")[2]
    print(df2.loc[college, ['address', 'city', "state", "zip"]])










