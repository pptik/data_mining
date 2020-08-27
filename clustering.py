import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
from sklearn import preprocessing
print("tes")
dataset = pd.read_csv('Employee_monthly_salary.csv')
data = pd.DataFrame(dataset,columns = ['Age','Net_Pay'])
print(data)
# plt.scatter(data['Age'],data['Net_Pay'])
# plt.xlabel('Age')
# plt.ylabel('GROSS')
# plt.show()

x = data.copy()
kmeans = KMeans(2)
kmeans.fit(x)

clusters = x.copy()
# clusters['cluster_pred'] = kmeans.fit_predict(x)
# plt.scatter(clusters['Age'],clusters['Net_Pay'], c =clusters['cluster_pred'],cmap = 'rainbow')
# plt.xlabel('Age')
# plt.ylabel('Net_Pay')
# plt.show()


x_scaled = preprocessing.scale(x)
print(x_scaled)
wcss = []
for i in range(1,100):
    kmeans = KMeans(i)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)
print(wcss)

# plt.plot(range(1,100),wcss)
# plt.xlabel('Number Of Cluster')
# plt.ylabel('WCSS')
# plt.show()

kmeans_new = KMeans(4)
kmeans.fit(x_scaled)
clusters_new = x.copy()
clusters_new['cluster_pred'] = kmeans_new.fit_predict(x_scaled)
print(clusters_new)

plt.scatter(clusters_new['Age'],clusters_new['Net_Pay'],c =clusters_new['cluster_pred'],cmap='rainbow')
plt.xlabel("Age")
plt.ylabel("Net Pay")
plt.show()