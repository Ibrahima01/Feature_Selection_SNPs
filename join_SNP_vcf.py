import pandas as pd

# Charger les données
data= pd.read_csv('GSE_clean_data_DI.csv', sep='\t')
ref=pd.read_csv('modifie.vcf', sep='\t')

ref = ref[["ID", "REF"]]

# Jointure des données SNP et phénotype sur la colonne "ID"
gse_ref = data.merge(ref, on="ID")

gse_ref.to_csv("gse_ref.csv", sep="\t", index=False)
