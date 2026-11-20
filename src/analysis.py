import pandas as pd

data={"name":["Ravi","Priya","Kumar"],"city":["Chennai","Madurai","Chennai"]}
df=pd.DataFrame(data)
print(df)
print("Total Chennai:", len(df[df["city"]=="Chennai"]))