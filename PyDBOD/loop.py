# -*- coding: utf-8 -*-
"""
@author: Miguel Ángel López Robles
"""


import numpy as np
from sklearn.neighbors import NearestNeighbors
from scipy.special import erf
from base import base

'''
# function to load a data file 
def load_data(data_file, sep = ','):
    f = open(data_file,'r')
    lines = f.readlines()
    result = []
    for line in lines:
        line = line.split(sep)
        if '@' not in line[0]:
            if line[len(line)-1] == 'negative\n':
                line[len(line)-1] = '0'
            else:
                line[len(line)-1] = '1'
            result.append(np.array(line,dtype=np.float))
    
    result = np.array(result)
    #print("result")
    #print(result)
    return result
    
# LoOP function
def loop(data, k=20, lamda=3):

    nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(data)
    distances, indices = nbrs.kneighbors(data)

    
    n_points = distances.shape[0]




    #calculate the standar distances 
    standar_distances = np.sqrt( np.sum( np.power(distances,2), axis=1 ) / n_points )

    #calculate the probabilistic distances
    p_distances = lamda * standar_distances
    #print("distancias probabilisticas")
    #print(p_distances)

    #calculate the probabilistic Local Outlier Factor
    plof = p_distances /  [ np.sum([p_distances[j] for j in indices[i] ]) for i in indices]
    #we eliminate the -1 because we assume that the data is distributed from 0

    print("plof")
    print(plof)
    #calculate de normalized probabilistic local outlier factor
    nplof = lamda * np.sqrt( np.mean( np.power( plof, 2) ) )

    #apply the Gaussian Error Function to obtain the Local Outlier Probability
    
    loop = np.maximum(0, erf( plof / ( nplof * np.sqrt(2) ) ) )
    print(loop)

    

    return loop



'''

class LOOP(base):

    def __init__(self,  k=20, lamda=3):
        self.k = k
        self.lamda = lamda
    
    def fit_predict(self, data):
        
        nbrs = NearestNeighbors(n_neighbors= self.k, algorithm='ball_tree').fit(data)
        distances, indices = nbrs.kneighbors(data)

        
        n_points = distances.shape[0]




        #calculate the standar distances 
        standar_distances = np.sqrt( np.sum( np.power(distances,2), axis=1 ) / n_points )

        #calculate the probabilistic distances
        p_distances = self.lamda * standar_distances
        #print("distancias probabilisticas")
        #print(p_distances)

        #calculate the probabilistic Local Outlier Factor
        plof = p_distances /  [ np.sum([p_distances[j] for j in indices[i] ]) for i in indices]
        #we eliminate the -1 because we assume that the data is distributed from 0

        print("plof")
        print(plof)
        #calculate de normalized probabilistic local outlier factor
        nplof = self.lamda * np.sqrt( np.mean( np.power( plof, 2) ) )

        #apply the Gaussian Error Function to obtain the Local Outlier Probability
        
        loop = np.maximum(0, erf( plof / ( nplof * np.sqrt(2) ) ) )
        print(loop)

        

        return loop
