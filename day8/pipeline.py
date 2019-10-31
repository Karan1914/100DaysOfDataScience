
# piedmont wines dataset
# 178 samples from 3 distinct varieties of red wine : Barolo, Grignolino and Barbera

# need to perform 2 steps 
# StandardScaler and then KMeans

# Use Sklearn pipeline to combine these two steps

from skearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

scaler= StandardScaler()
kmeans= KMeans(n_clusters=3)

from sklearn.pipeline import make_pipeline

pipeline=make_pipeline(scaler,kmeans)

pipeline.fit(samples)

labels= pipeline.predict(samples)

df = pd.DataFrame({'labels':labels, 'varieties':varieties})

ct= pd.crosstab(df['labels'],df['varieties'])

print(ct)