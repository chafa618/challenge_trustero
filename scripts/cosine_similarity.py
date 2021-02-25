import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosine_matrix(vectors_list):
    cosine_matrix = cosine_similarity(vectors_list)
    np.fill_diagonal(cosine_matrix, 0)
    return cosine_matrix

def cosine_one_many(vector,vectors_list):
    sum_vectors = [vector] + vectors_list
    matrix = cosine_matrix(sum_vectors)
    return list(matrix[0,1:])