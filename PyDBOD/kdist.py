# -*- coding: utf-8 -*-
"""
@author: Miguel Ángel López Robles
"""



import numpy as np
from sklearn.neighbors import NearestNeighbors
from operator import itemgetter

from PyDBOD.base import Base


class KDIST(Base):
    def __init__(self, k=20, t=1.5):
        self.k = k
        self.t = t

    def fit_predict(self, data):
        n = data.shape[0]
        nbrs = NearestNeighbors(n_neighbors= self.k, algorithm='ball_tree').fit(data)
        distances, indices = nbrs.kneighbors(data)

        #calculate de mean of the neigbours
        max_distances = np.max(distances, axis =1)

        #identify the mean because we need sort it
        id_mean =   [   (i,max_distances[i]) for i in range(n)    ] 
        print(id_mean)
        #sort the mean distances
        sort_mean = sorted(id_mean, key=itemgetter(1))
        
        print(sort_mean)
        
        diferencia = np.array([sort_mean[i][1] - sort_mean[i-1][1] for i in range(1, n) ])
        print(diferencia)
        print(np.amax(diferencia))
        T = np.amax(diferencia) * self.t
        

        ##find the cut point
        i = 0
        encontrado = False
        
        while( (i < n-1) and ( not encontrado) ):
            if diferencia[i] >= T:
                print("entro")
                encontrado=True
            else:
                i = 1 +i

        kdist = np.zeros(n)
        print(i)
        for j in range(i,n):
            kdist[ sort_mean[j][0]] = 1
        
        #meandist = np.array(mean_distances >= T, dtype=np.int)

        return kdist