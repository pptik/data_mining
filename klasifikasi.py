import pandas as pa

students_grades = pa.read_excel(r'/Users/PPTIK/dev/datamaining/data.xlsx')
df = pa.DataFrame(students_grades,columns=['NAMA','NISN','BIOLOGI','FISIKA','SEJARAH','EKONOMI'])
print(df)

ipa_grades = (df['BIOLOGI'] + df['FISIKA'])
ips_grades = (df['SEJARAH'] + df['EKONOMI'])

print("")
# print(ipa_grades)
# print(ips_grades)

df.loc[ipa_grades<ips_grades,'KELAS'] = 'IPS'
df.loc[ipa_grades>ips_grades,'KELAS'] = 'IPA'

print(df)

df.to_excel('./klasifikasi.xlsx',sheet_name='kelas',index=False)
print("data has been export")