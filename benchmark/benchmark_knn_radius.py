from ard_kmeans import ardkmeans
from ard_kmeans.utils import silhouette

def run(data, k=3, runs=10):
    scores = []
    for _ in range(runs):
        c, cl = ardkmeans(data, k)
        scores.append(silhouette(data, cl, c))
    return sum(scores)/len(scores)

from examples.sample_data import uneven, touching, imbalanced, elongated


print("Uneven:", run(uneven))
print("Touching:", run(touching))
print("Imbalanced:", run(imbalanced))
print("Elongated:", run(elongated))
