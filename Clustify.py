# Learning about Clustering with the K-Means algorithm
# Also practicing using Github in conjunction with Visual Studio Code
# We follow the steps explained in datacamp.com tutorial:
# https://www.datacamp.com/tutorial/k-means-clustering-python

# 1. Dataset Load
import pandas as pd
df = pd.read_csv('spotify_songs.csv', usecols = ['tempo', 'energy', 'danceability'])
print(df.head())  # Added to be able to print in VS Code


# 2. Visualize the Data
import seaborn as sns
sns.scatterplot(data=df, x='tempo', y='energy', hue='danceability')

# We need to add the following to display the chart in VS Code:
import matplotlib.pyplot as plt
plt.show()


# 3. We normalize data (we skip trainig/test data split for now)
from sklearn import preprocessing
data_norm = preprocessing.normalize(df)


# 4. Fitting and Evaluating the model (let's arbitrarily choose number of clusters = 3)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0, n_init='auto')
kmeans.fit(data_norm)


# 5. We visualize the data we just fit
sns.scatterplot(data=df, x='tempo', y='energy', hue=kmeans.labels_)
plt.show()


# 6. We visualize distribution of danceability
sns.boxplot(x = kmeans.labels_, y = df['danceability'])
plt.show()


# 7. Calculating Silhouette Score
from sklearn.metrics import silhouette_score
sil_score = silhouette_score(data_norm, kmeans.labels_, metric='euclidean')


# 8. Choosing the best number of clusters
K = range(2, 8)  # We explore a K range between 2 and 7
fits = []
scores = []
for k in K:
    # Train the model for current value of k on training data
    model = KMeans(n_clusters=k, random_state=0, n_init='auto').fit(data_norm)

    # Append the model to fits
    fits.append(model)

    # Append the silhouette score to scores
    scores.append(silhouette_score(data_norm, model.labels_, metric='euclidean'))


# 9. Plotting elbow to evaluate the best number of clusters
sns.lineplot(x=K, y=scores)
plt.show()


# 10. We could visually look at a few different values of k (let's choose 5 for now)
# We should change the value once we run the script and see the elbow chart
sns.scatterplot(data = df, x = 'tempo', y = 'energy', hue = fits[3].labels_)
plt.show()