import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns

print("res")
employee = pd.read_csv("Employee_monthly_salary.csv")
employee = employee.drop(["EmpID","Date_of_Birth","Join_Date","Tenure_in_org_in_months","Deduction_percentage"],axis=1)
employee.head()
print(employee)

driver_x = employee.iloc[:, 1:9]
driver_x.head()


print()

print(driver_x)

#Klasifikasi Gender

# genders = employee.Gender.value_counts()
# sns.set_style("darkgrid")
# plt.figure(figsize=(10,4))
# sns.barplot(x=genders.index, y=genders.values)
# plt.show()

# Klasifikasi Umur
age18_25 = employee.Age[(employee.Age <= 25) & (employee.Age >= 18)]
age26_35 = employee.Age[(employee.Age <= 35) & (employee.Age >= 26)]
age36_45 = employee.Age[(employee.Age <= 45) & (employee.Age >= 36)]
age46_55 = employee.Age[(employee.Age <= 55) & (employee.Age >= 46)]
age55above = employee.Age[employee.Age >= 56]

x = ["18-25","26-35","36-45","46-55","55+"]
y = [len(age18_25.values),len(age26_35.values),len(age36_45.values),len(age46_55.values),len(age55above.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=x, y=y, palette="rocket")
plt.title("Number of Customer and Ages")
plt.xlabel("Age")
plt.ylabel("Number of Customer")
plt.show()

# plt.scatter(employee.Gender, employee.Age, s =10, c = "c", marker = "o", alpha = 1)
# plt.show()