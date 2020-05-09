# author @AkshatSurolia
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\akroc\\Desktop\\Spotify PCA\\traingdata.csv")
print(df.head())
print(df.describe())
df.drop(['time_signature', 'mode', 'key','duration_ms'], axis=1, inplace=True)
print(df.head())
# Standardization is important in PCA since it is a variance maximizing exercise.
# It projects your original data onto directions which maximize the variance.
from sklearn.preprocessing import StandardScaler
x = df.values #returns a numpy array
x_scaled = StandardScaler().fit_transform(x)
 
df_scaled = pd.DataFrame(x_scaled, columns=df.columns)
print(df_scaled.head())
 # Calculate a PCA manually
# calculate the mean vector
mean_vector = x_scaled.mean(axis=0)
print(mean_vector)
# calculate the covariance matrix
cov_mat = np.cov((x_scaled).T)
print(cov_mat.shape)
print(cov_mat)
# calculate the eigenvectors and eigenvalues of our covariance matrix for the dataset
eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
# Print the eigen vectors and corresponding eigenvalues
# in order of descending eigenvalues
for i in range(len(eig_val_cov)):
    eigvec_cov = eig_vec_cov[:,i]
    print('Eigenvector {}: \n{}'.format(i+1, eigvec_cov))
    print('Eigenvalue {} from covariance matrix: {}'.format(i+1, eig_val_cov[i]))
    print(50 * '-')

# the percentages of the variance captured by each eigenvalue
# is equal to the eigenvalue of that components divided by
# the sum of all eigen values
explained_variance_ratio = eig_val_cov/eig_val_cov.sum()
explained_variance_ratio_srt = sorted(explained_variance_ratio, reverse=True)
print(explained_variance_ratio_srt)

# Scree Plot
plt.plot(np.cumsum(explained_variance_ratio_srt))
plt.title('Scree Plot')
plt.xlabel('Principal Component (k)')
plt.ylabel('% of Variance Explained <= k')
plt.show()

# scikit-learn's version of PCA
from sklearn.decomposition import PCA
# Like any other sklearn module, we first instantiate the class
pca = PCA(n_components=6, random_state=42)
# fit the PCA to our data
pca.fit(x_scaled)

print(pca.components_)
print(pca.explained_variance_ratio_)
np.sum(pca.explained_variance_ratio_)
print(pca.transform(x_scaled))
print(pca.score(x_scaled))