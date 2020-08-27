import pandas as pd
data = pd.read_excel(r'/Users/PPTIK/dev/datamaining/data.xlsx')
df = pd.DataFrame(data,columns = ['NAMA','NIM','KELAS'])
print(df)