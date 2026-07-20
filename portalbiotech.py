import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#Importing the datafile and making sure it ha trasferred properly 
datafile = pd.read_csv("/Users/vesoelisabeth/Downloads/portal_ds_task/peptide_retention.csv")
print(datafile.head(10))


#Creating a dataframe
labels = ('ID', 'PeptideSequence','Modifications', 'RetentionTime')
df= pd.DataFrame(datafile, columns=labels)

#Questions I can explore: 
#Do PTM contribute to the retention longevity
#Does acetylation have a larger impact than oxidation
#How does PTM of specific amino acids influence the retention time
#Maybe play around with the prediction of future PTMs
#Maybe compare the data to the DeepLC performance

#Step 1: Data cleaning
df.fillna("", inplace=True)
duplicate_count = df.duplicated(subset=["ID"]).sum()
print("Number of duplicate IDs:", duplicate_count)

print("Inspecting Sequences and Modifications")
print(df[['PeptideSequence', 'Modifications']].head(10))


#Step 2: Does acetylation have a larger impact than oxidation?

df['acetyl'] = df['Modifications'].str.contains('acetyl', case=False, na=False)
df['oxidation'] = df['Modifications'].str.contains('oxid', case=False, na=False)

def category_row(row):
    if row['acetyl']:
        return 'Acetylation'
    elif row['oxidation']:
        return 'Oxidation'
    elif row['Modifications'] == "" or pd.isna(row['Modifications']):
        return 'Unmodified'
    else:
        return 'Other PTM'

df['PTM_Category'] = df.apply(category_row, axis=1)

print(df['PTM_Category'].value_counts())


#Do PTMs affect the retention time?
summary = df.groupby("PTM_Category")["RetentionTime"].describe()
print(summary)

print(df.groupby('PTM_Category')['RetentionTime'].mean())
print(df.groupby('PTM_Category')['RetentionTime'].agg(['mean','median','std','count']))

df.boxplot(column="RetentionTime", by="PTM_Category", figsize=(8,6))
plt.ylabel('Retention Time')
plt.xticks(rotation=20)
plt.show()


#Step 3: Is acetylation or oxidation associated with larger retention times?

acetyl = df[df['PTM_Category']=='Acetylation']['RetentionTime']
oxid = df[df['PTM_Category']=='Oxidation']['RetentionTime']

print('Acetyl mean:', acetyl.mean())
print('Oxidation mean:', oxid.mean())


groups = [
    df[df['PTM_Category']=='Acetylation']['RetentionTime'],
    df[df['PTM_Category']=='Oxidation']['RetentionTime'],
    df[df['PTM_Category']=='Unmodified']['RetentionTime']
]

plt.violinplot(groups, showmeans=True, showmedians=True)
plt.xticks([1,2,3], ['Acetylation','Oxidation','Unmodified'])
plt.ylabel('Retention Time')
plt.show()

#Step 4: How does PTM of specific amino acids influence the retention time?
# OR Does the position of the PTM matter?

df['PeptideLength'] = df['PeptideSequence'].str.len()
df['Position'] = df['Modifications'].str.extract(r'(\d+)\|')
df['Position'] = pd.to_numeric(df['Position'])


def get_modif_aa(row):
    if pd.isna(row['Position']):
        return None
    return row['PeptideSequence'][int(row['Position']) - 1]
                                          
df['Modified_aa'] = df.apply(get_modif_aa, axis=1)

print(df['Modified_aa'].value_counts())

print(df.groupby('Modified_aa')['RetentionTime'].agg(['count', 'mean', 'median']))