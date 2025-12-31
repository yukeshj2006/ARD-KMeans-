import math

def distance(p1, p2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def sse(centroids, clusters):
    total = 0
    for i, c in enumerate(clusters):
        for p in c:
            total += distance(p, centroids[i])**2
    return total

def silhouette(data, clusters, centroids):
    labels = {}
    for idx, c in enumerate(clusters):
        for p in c:
            labels[tuple(p)] = idx
    def intra(p, cid):
        c = clusters[cid]
        if len(c) <= 1:
            return 0
        return sum(distance(p, q) for q in c if q != p) / (len(c) - 1)
    def nearest(p, cid):
        best = float("inf")
        for ocid, c in enumerate(clusters):
            if ocid == cid or not c:
                continue
            avg = sum(distance(p, q) for q in c) / len(c)
            best = min(best, avg)
        return best
    scores = []
    for p in data:
        cid = labels[tuple(p)]
        a = intra(p, cid)
        b = nearest(p, cid)
        if max(a, b) == 0:
            scores.append(0)
        else:
            scores.append((b - a) / max(a, b))
    return sum(scores) / len(scores)
