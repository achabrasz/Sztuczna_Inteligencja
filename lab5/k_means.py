import numpy as np

def initialize_centroids_forgy(data, k):
    # TODO implement random initialization
    centroids = np.random.choice(data.shape[0], k, replace=False)
    return centroids

def initialize_centroids_kmeans_pp(data, k):
    # TODO implement kmeans++ initizalization
    centroids  = []
    for i in range(k):
        if i == 0:
            centroids.append(np.random.choice(data.shape[0], 1, replace=False))
        else:
            distances = np.zeros(data.shape[0])
            for j in range(data.shape[0]):
                distances[j] = np.sqrt(np.sum(abs(data - data[j])))
            prob = distances / np.sum(distances)
            centroids.append(np.random.choice(data.shape[0], 1, replace=False, p=prob))
    return centroids

def assign_to_cluster(data, centroid):
    # TODO find the closest cluster for each data point
    cluster = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        distances = np.zeros(len(centroid))
        for j in range(len(centroid)):
            distances[j] = np.sqrt(np.sum(abs(data[i] - centroid[j])))
        cluster[i] = np.argmin(distances)
    return cluster

def update_centroids(data, assignments):
    # TODO find new centroids based on the assignments

    return None

def mean_intra_distance(data, assignments, centroids):
    return np.sqrt(np.sum((data - centroids[assignments, :])**2))

def k_means(data, num_centroids, kmeansplusplus= False):
    # centroids initizalization
    if kmeansplusplus:
        centroids = initialize_centroids_kmeans_pp(data, num_centroids)
    else: 
        centroids = initialize_centroids_forgy(data, num_centroids)

    
    assignments  = assign_to_cluster(data, centroids)
    for i in range(100): # max number of iteration = 100
        print(f"Intra distance after {i} iterations: {mean_intra_distance(data, assignments, centroids)}")
        centroids = update_centroids(data, assignments)
        new_assignments = assign_to_cluster(data, centroids)
        if np.all(new_assignments == assignments): # stop if nothing changed
            break
        else:
            assignments = new_assignments

    return new_assignments, centroids, mean_intra_distance(data, new_assignments, centroids)         

