import pandas as pd
import numpy as np

df = pd.read_excel("colleges_excel.xlsx")
df2 = df.head(1)


# inserts column after column 2 with no values
df2.insert(2, "address", "")
df2.insert(3, "city", "")
df2.insert(4, "state", "")
df2.insert(5, "zip", "")
df2.insert(6, "nearest_hub", "")
df2.insert(6, "miles", np.nan)

indexer = 0
for college in range(len(df2)):
    formatted_name = df2.at[college, 'institution_name'].replace(" ", "%")
    print(formatted_name)









