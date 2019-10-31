# t-SNE Hierarchical clustering

# used for 2-d maps
""" stands for t-distributed stochastic neighbor embedding
maps samples from high dimensional space to 2D or 3D space
Map approximately preserves nearness of samples
Great for inspecting datasets

"""

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
model = TSNE(learning_rate=100)
# different learning rate for different datasets
# wrongchoice : points bunch together
# try values between 50 and 200


transformed = model.fit_transform(samples) 
# tsne only has this method
# this means you can't extend the map to include new data samples
# must start over each time

xs=transformed[:,0]
ys=transformed[:,1]

plt.scatter(xs,yx,c=species)
plt.show()