#pip3 install pandas
import pandas as pd

data = {
    "name" : ["Amy", "Jackie", "Sue"],
    "grades" : [90, 84, 76]
}

df = pd.DataFrame(data)

print(df)
