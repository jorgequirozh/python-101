#pip3 install pandas
import pandas as pd

data = {
    "name" : ["Amy", "Jackie", "Sue"],
    "grades" : [90, 84, 76]
}

df = pd.DataFrame(data)

print(df)
#multiply all grade by 1.2

df["grades"] = df["grades"].apply(lambda x: x * 1.2)

print(df)
