import numpy as np

# Charger les données à partir du fichier CSV
df = np.genfromtxt('gse_ref.csv', delimiter='\t')

# Convertir le DataFrame pandas en un tableau NumPy
arr = df.values

# Sélectionner les colonnes pertinentes
snp_columns = arr[:, 1:-1]
reference_allele = arr[:, -1]

# Condition 1: snp[0] == snp[1] == reference_allele
condition1 = (snp_columns[:, 0] == snp_columns[:, 1]) & (snp_columns[:, 0] == reference_allele)

# Condition 2: snp[0] != snp[1] and (snp[0] == reference_allele or snp[1] == reference_allele)
condition2 = (snp_columns[:, 0] != snp_columns[:, 1]) & ((snp_columns[:, 0] == reference_allele) | (snp_columns[:, 1] == reference_allele))

# Appliquer les conditions et attribuer les valeurs appropriées
arr[condition1, 1:-1] = 0
arr[condition2, 1:-1] = 1
arr[~(condition1 | condition2), 1:-1] = 2

# Créer un nouveau DataFrame à partir du tableau NumPy
df_transformed = pd.DataFrame(arr, columns=df.columns)

# Enregistrer le tableau NumPy dans un fichier CSV
np.savetxt('gse_ref_numpy_transformed.csv', arr, delimiter='\t', fmt='%s')
