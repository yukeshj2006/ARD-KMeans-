import math
import random
import numpy as np

def distance(p1, p2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def compute_local_radius(point, data, k=5):
    d = [distance(point, q) for q in data if q != point]
    d.sort()
    k = min(k, len(d))
    return sum(d[:k]) / k

def neighbors(R, c, data):
    return [p for p in data if distance(p, c) < R]

def densest(neigh, R, data):
    best = neigh[0]
    best_count = -1
    for p in neigh:
        count = sum(1 for q in data if distance(p, q) < R)
        if count > best_count:
            best_count = count
            best = p
    return best

def init_centroids(data, k):
    centroids = [random.choice(data)]
    for _ in range(k - 1):
        dist_sq = [min(distance(p, c)**2 for c in centroids) for p in data]
        candidate = data[np.argmax(dist_sq)]
        R = compute_local_radius(candidate, data, k=5)
        neigh = neighbors(R, candidate, data)
        refined = densest(neigh, R, data)
        if refined in centroids:
            refined = candidate
        centroids.append(refined)
    return centroids

def assign_to_clusters(centroids, data):
    clusters = [[] for _ in centroids]
    for p in data:
        idx = min(range(len(centroids)), key=lambda j: distance(p, centroids[j]))
        clusters[idx].append(p)
    return clusters

def update_centroids(clusters, data):
    new_c = []
    for c in clusters:
        if not c:
            new_c.append(random.choice(data))
            continue
        dim = len(c[0])
        mean = [sum(p[i] for p in c)/len(c) for i in range(dim)]
        new_c.append(mean)
    return new_c

def has_converged(c1, c2, tol=1e-4):
    for a, b in zip(c1, c2):
        for x, y in zip(a, b):
            if abs(x - y) > tol:
                return False
    return True

def ardkmeans(data, k):
    centroids = init_centroids(data, k)
    for _ in range(1000):
        clusters = assign_to_clusters(centroids, data)
        new_centroids = update_centroids(clusters, data)
        if has_converged(new_centroids, centroids):
            break
        centroids = new_centroids
    return centroids, clusters
