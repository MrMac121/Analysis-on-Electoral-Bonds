import tabula
import pandas as pd

df1 = pd.read_csv('electoral_bonds_silo_1.csv')
df2 = pd.read_csv('electoral_bonds_silo_2.csv')

df2 = df2.iloc[:, 3:]
print(df2.dtypes)
df1 = df1.iloc[:, 2:]
print(df1.dtypes)

paid_bonds = df1[df1['Status'] != 'Expired']

paid_bonds = paid_bonds.reset_index()

company_bonds_value1000 = paid_bonds[paid_bonds['Denominations'] == 1000]
company_bonds_value10000 = paid_bonds[paid_bonds['Denominations'] == 10000]
company_bonds_value100000 = paid_bonds[paid_bonds['Denominations'] == 100000]
company_bonds_value1000000 = paid_bonds[paid_bonds['Denominations'] == 1000000]
company_bonds_value10000000 = paid_bonds[paid_bonds['Denominations'] == 10000000]


company_bonds_value1000 = company_bonds_value1000.reset_index()
company_bonds_value10000 = company_bonds_value10000.reset_index()
company_bonds_value100000 = company_bonds_value100000.reset_index()
company_bonds_value1000000 = company_bonds_value1000000.reset_index()
company_bonds_value10000000 = company_bonds_value10000000.reset_index()

party_bonds_value1000 = df2[df2['Denominations'] == 1000]
party_bonds_value10000 = df2[df2['Denominations'] == 10000]
party_bonds_value100000 = df2[df2['Denominations'] == 100000]
party_bonds_value1000000 = df2[df2['Denominations'] == 1000000]
party_bonds_value10000000 = df2[df2['Denominations'] == 10000000]

party_bonds_value1000 = party_bonds_value1000.reset_index()
party_bonds_value10000 = party_bonds_value10000.reset_index()
party_bonds_value100000 = party_bonds_value100000.reset_index()
party_bonds_value1000000 = party_bonds_value1000000.reset_index()
party_bonds_value10000000 = party_bonds_value10000000.reset_index()

bonds_value1000 = pd.merge(company_bonds_value1000, party_bonds_value1000, on='Bond\rNumber')
bonds_value10000 = pd.merge(company_bonds_value10000, party_bonds_value10000, on='Bond\rNumber')
bonds_value100000 = pd.merge(company_bonds_value100000, party_bonds_value100000, on='Bond\rNumber')
bonds_value1000000 = pd.merge(company_bonds_value1000000, party_bonds_value1000000, on='Bond\rNumber')
bonds_value10000000 = pd.merge(company_bonds_value10000000, party_bonds_value10000000, on='Bond\rNumber')

combined_electoral_bonds_data = pd.concat([bonds_value1000, bonds_value10000, bonds_value100000, bonds_value1000000, bonds_value10000000])


combined_electoral_bonds_data = combined_electoral_bonds_data.drop(['level_0', 'Prefix_y', 'index_y', 'Denominations_y'], axis=1) #idk what's going on 

combined_electoral_bonds_data.rename(columns = {'index_x':'index', 'Prefix_x':'Prefix',
                              'Denominations_x':'Denominations'}, inplace = True)

combined_electoral_bonds_data = combined_electoral_bonds_data.reset_index()

print(combined_electoral_bonds_data.dtypes)

combined_electoral_bonds_data.to_csv('combined_electoral_bonds_data.csv')



# denominations = df['Denominations']

# denominations_list = []
#
# for denomination in denominations:
#     denominations_list.append(int(denomination.replace(',', '')))
#
# denomination_list_series = pd.Series(data=denominations_list, name='Denominations')
# print(denomination_list_series)
# df['Denominations'] = denomination_list_series
#
# df.to_csv('electoral_bonds_silo_1.csv')

# expired_bonds = df1[df1['Status'] == 'Expired']
#
# expired_bonds = expired_bonds.reset_index()
#
# expired_bonds.to_csv('expired_bonds.csv')


# Hi this is a pull request

