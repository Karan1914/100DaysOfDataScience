# Eurovision dataset
# Countries gave scores to song performed at the Eurovision 2016
# 2D array of scores
# Rows are countries, columns are songs

# Hierarchical Clustering

# tree like diagram called Dendogram

# steps for Hierarchical clustering
"""
1) in Beginning every country is in own cluster (seprate cluster)
2) At each step, the two closest clusters are merged
3) Continues until all countries in a single cluster
4) This is agglomerative hierarchical clustering
5) Also there is divisive clustering which works the other way
"""
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

mergings = linkage(samples, method='complete') 
# linkage() function to obtain a hierarchical clustering of the grain samples

dendrogram(mergings,labels=country_names,leaf_rotation=90,leaf_font_size=6) 
# dendrogram() to visualize the result. A sample of the grain measurements is provided in the array samples

plt.show()

# with 5 data samples there would be 4 merge operations

# SciPy hierarchical clustering doesn't fit into a sklearn pipeline, 
# so you'll need to use the normalize() function from sklearn.preprocessing instead of Normalizer

from scipy.cluster.hierarchy import fcluster
labels=fcluster(mergings, 15, criterion='distance')

# complete linkage : furthest point distance between two clusters
# single linkage: closest point distance between two clusters