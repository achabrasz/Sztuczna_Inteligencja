import numpy as np

def initialize_centroids_forgy(data, k):
    # TODO implement random initialization
    centroids = np.random.choice(data.shape[0], k, replace=False)
    return centroids

def initialize_centroids_kmeans_pp(data, k):
    # TODO implement kmeans++ initizalization
    centroids = []
    centroids.append(data[np.random.randint(data.shape[0])])
    for _ in range(1, k):
        distances = []
        for point in data:
            distances.append(np.min([np.sqrt(np.sum(abs(point - centroid)**2)) for centroid in centroids]))
        distances = np.array(distances)
        probabilities = distances ** 2 / np.sum(distances ** 2)
        new_centroid = data[np.random.choice(data.shape[0], p=probabilities)]
        centroids.append(new_centroid)

    return np.array(centroids)

def assign_to_cluster(data, centroid):
    # TODO find the closest cluster for each data point
    cluster = np.zeros(data.shape[0], dtype=int)
    for i in range(data.shape[0]):
        distances = np.zeros(len(centroid))
        for j in range(len(centroid)):
            distances[j] = np.sqrt(np.sum(abs(data[i] - centroid[j])**2))
        cluster[i] = np.argmin(distances)
    return cluster

def update_centroids(data, assignments):
    centroid = []
    # TODO find new centroids based on the assignments
    for i in np.unique(assignments):
        centroid.append(np.mean(data[assignments==i], axis=0))
    return centroid

def mean_intra_distance(data, assignments, centroids):
    centroids = np.array(centroids)
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

