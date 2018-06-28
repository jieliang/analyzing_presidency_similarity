# app.py passes user input from index.html to
# function get_similar_presidents in this file. Resulting list of
# similar presidents is then returned to app.py

import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np


filename = '/home/jieliang/proj4/flask_test/data/flask_data.pkl'
authors_indices,lsa_vecs,sample_lsa_tfidf_data,presidents = pickle.load(open(filename, 'rb'))

'''
returns a scaled vector representing given author in topic space
'''
def get_author_vec(topic_data, author):
    indices = authors_indices[author]
    author_vec=sum(topic_data[indices,:])/len(indices)
    return StandardScaler().fit_transform(author_vec.reshape(-1, 1))

# a list of scaled vectors each representing a president in given topic space
president_topic_vecs = lsa_vecs

'''
returns a list of presidents most similar to given author
'''
def get_similar_presidents(author, num_similar_presidents):

    nn = NearestNeighbors(n_neighbors=num_similar_presidents+1, metric='cosine', algorithm='brute')
    vecs = president_topic_vecs
    author_vec = get_author_vec(sample_lsa_tfidf_data,author)

    nn.fit(vecs)

    results = nn.kneighbors(np.array(author_vec).reshape(1, -1))

    similar_presidents_indices= results[1][0]
    return ' ,'.join([presidents[i] for i in similar_presidents_indices if presidents[i]!=author][:num_similar_presidents])



#def make_soft_prediction(president):
#    return get_similar_presidents(president,3)
