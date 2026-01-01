# ARD-KMeanspp
ARD-KMeans++ is an enhanced centroid initialization strategy for the K-Means clustering algorithm.
It extends the standard KMeans++ initializer with a local density–based refinement step designed to improve stability and cluster quality on uneven, imbalanced, and elongated datasets.

This is the official v1 implementation using a local k-nearest-neighbor (kNN) radius to guide the density-aware centroid refinement.

Overview

Standard KMeans++ chooses new centroids based on distance from existing centroids.
While effective, it still frequently selects points from:

sparse cluster boundaries
elongated structures
low-density regions
imbalanced datasets

ARD-KMeans++ reduces these issues by applying a refinement step:

KMeans++ selects a candidate centroid based on distance.
ARD computes a local adaptive radius around that candidate.
All points within this radius form a neighborhood.
The densest point in that neighborhood replaces the candidate.
This produces more stable and representative initial centroids.

Improvements Over KMeans++

Based on controlled synthetic dataset tests, ARD-KMeans++ demonstrates:

Approximately 0.2–0.3% improvement in silhouette score on uneven-density datasets
Approximately 3–5% reduction in SSE on imbalanced datasets
Similar or slightly improved performance on elongated clusters
Stable performance on touching clusters
These gains come solely from improved centroid initialization; the K-Means iteration stage remains unchanged.

Algorithm Summary

For each centroid to be selected:
1.Use KMeans++ distance-based sampling to propose a candidate.
2.Compute a local radius based on the candidate’s k nearest neighbors.
3.Select the densest point inside this radius.
4.Add this refined point as the next centroid.
5.Add this refined point as the next centroid.
6.After initialization, the algorithm proceeds with standard K-Means.


Limitations

Like KMeans++, ARD-KMeans++ is sensitive to highly overlapping clusters.
The refinement radius is local but still controlled by a single parameter k.
Performance depends on neighborhood structure, and may not always outperform KMeans++.

Future Work

The next version (v2) may explore:
multi-scale radius estimation
adaptive density scoring
curvature-aware radius
hybrid shape-based initialization
faster neighbor search structures
