import pandas as pd
import numpy as np
import tabula as tb

# df = tb.read_pdf('ruHb53PTjj.pdf', pages='all', multiple_tables=False)
#
# df = df[0]
#
# print(df.dtypes)
#
# # df = df[df['Denominations' != 'Denominations']]
# # denominations = df['Denominations']
#
# df = df[df['Sr No.'] != 'Sr No.']
# df = df.reset_index()
# denominations = df['Denominations']
#
# denominations_list = []
# for denomination in denominations:
#     denominations_list.append(int(denomination.replace(',', '')))
#
# denomination_list_series = pd.Series(data=denominations_list, name='Denominations')
# print(denomination_list_series)
# df['Denominations'] = denomination_list_series
#
# print(df['Denominations'])
#
# df.to_csv('electoral_bonds_silo_2.csv')

# df = pd.read_csv('electoral_bonds_silo_2.csv')
# df_new = df.iloc[:, 1:]
#
# money_amount = df_new.groupby('Name of the Political Party')['Denominations'].sum()
#
# money_amount.to_csv('party_money_amount_sum.csv')


