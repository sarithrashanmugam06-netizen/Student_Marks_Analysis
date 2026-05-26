import pandas as pd

df= pd.read_csv(r"D:\Datasets\Student_Marks.csv")

print(df)

#summarise data
print(df.describe())
print(df.info())

#Average mark
average = df["Marks"].mean()
print(average)

#Highest mark
hight_mark = df["Marks"].max()
print(hight_mark)

#80 above mark

condition= df["Marks"]>80
print(condition)
