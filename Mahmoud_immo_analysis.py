import pandas as pd 


df = pd.read_csv('data_26_column.csv')

selected_columns = df.loc[:,'Terrace surface']
#--------------------------
# cleaning Terrace and Terrace surface
filter = df["Terrace surface"] != "None"
df['Terrace surface'] = df[filter]["Terrace surface"].str.replace(r'\D', '',regex = True)
filt = df['Terrace surface'].isnull()
df.loc[filt,'Terrace surface'] = 'None'
df['Terrace surface']
df.loc[filter,'Terrace'] = 'Yes'
df.loc[df['Terrace'] == 'Yes', 'Terrace'] = 1
df.loc[df['Terrace'] == 'None', 'Terrace'] = 0
print(df['Terrace'].head(50))
#-----------------------------
# filter Garden and Garden surface
filter_G = df["Garden surface"] != "None"
df['Garden surface'] = df[filter_G]["Garden surface"].str.replace(r'\D', '',regex = True)
filt = df['Garden surface'].isnull()
df.loc[filt,'Garden surface'] = 'None'
df['Garden surface']
df.loc[filter_G,'Garden'] = 'Yes'
df.loc[df['Garden'] == 'Yes', 'Garden'] = 1
df.loc[df['Garden'] == 'None', 'Garden'] = 0
#print(df['Garden'].head(50))
df['Garden surface'].head(50)
#-------------------------------
#Garden and Garden surface
filter_G = df["Garden surface (m²)"].isnull()
df.loc[~filter_G,'Garden'] = 'Yes'
df.loc[df['Garden'] == 'Yes', 'Garden'] = 1
df.loc[df["Garden"].isnull(), 'Garden'] = 0
df.loc[df["Garden surface (m²)"].isnull(),'Garden surface (m²)'] = 0
#-----------------------------------------------
#Terrace and Terrace surface
filter_G = df["Terrace surface (m²)"].isnull()
df.loc[~filter_G,'Terrace'] = 'Yes'
df.loc[df['Terrace'] == 'Yes', 'Terrace'] = 1
df.loc[df["Terrace"].isnull(), 'Terrace'] = 0
df.loc[df["Terrace surface (m²)"].isnull(),'Terrace surface (m²)'] = 0
#-------------prices
df['Price'] = df["Price"].str.replace(r'€ ','',regex = True)
df['Price'] = df["Price"].str.replace(r' [0-9]+ €$','',regex = True)
df['Price'] = df["Price"].str.replace(r'(^\D+ )','',regex = True)
df['Price'] = df["Price"].str.replace(r' (\D+ )','',regex = True)
df['Price'] = df["Price"].str.replace(r'\D','',regex = True)
df['Price'].head(50)
#-------------------------------------------------------
# filter_G = sf["Garden surface"].isnull()
# sf['Garden surface'] = sf[filter_G]["Garden surface"].str.split(' ').str[0]
# filt = sf['Garden surface'].isnull()
# sf.loc[filt,'Garden surface'] = 'None'

# sf['Garden surface']
# sf.loc[filter_G,'Garden'] = 'Yes'
# #sf['Garden surface'].head(50)
# #sf['Garden'].head(50)

# sf.loc[sf['Garden'] == 'Yes', 'Garden'] = 1
# sf.loc[sf['Garden'] == 'None', 'Garden'] = 0
# sf['Garden'].head(50)
#-------------------------------------