import pandas as pd
import numpy as np
import long_lat as ll

# imports the function wrote in query_request
import query_request as q

# Reads the excel sheet as a pandas data frame
df = pd.read_excel("colleges_excel.xlsx")

# Inserts column after column n with no values \
# dataframe.insert("column_index, "value to insert")
df.insert(2, "address", "")
df.insert(3, "city", "")
df.insert(4, "state", "")
df.insert(5, "zip", "")
df.insert(6, "nearest_hub", "")
# uses Numpy to insert NaN values, thus formatting column as int/float
df.insert(7, "miles", np.nan)

# takes each row for the length of the dataframe
for college in range(len(df)):
    # queries the Google Places API with the custoom query_maps function using the institution_name as the query string
    query = q.query_maps(df.at[college, 'institution_name'])
    try:
        # Separates the "address, city, st zip" into ["address", "city", "state zip"]
        deconstructed_address = query["candidates"][0]['formatted_address'].split(',')
        df.at[college, "address"] = deconstructed_address[0]
        df.at[college, "city"] = deconstructed_address[1]
        df.at[college, "state"] = deconstructed_address[2].split(" ")[1]
        df.at[college, "zip"] = deconstructed_address[2].split(" ")[2]

        # pulls the lat and long from the data returned by the query
        lat = query["candidates"][0]["geometry"]['location']['lat']
        long = query["candidates"][0]["geometry"]['location']['lng']

        # finds the closest hub and returns it using the custom find hub function
        hub = ll.find_hub(lat, long)

        # sets the miles column & nearest hub to the hub return by the query
        df.at[college, 'miles'] = float(hub[1])
        df.at[college, 'nearest_hub'] = hub[0]

        # prints the index of the loop so you know its working
        print(college)

    # excepts index errors in the query so code can continue to run.
    except IndexError:
        print("There was an index error a " + df.loc[college, 'institution_name'])
        pass

# writes the dataframe to an excel sheet using pandas
df.to_excel("colleges_with_hubs.xlsx", sheet_name="colleges")











