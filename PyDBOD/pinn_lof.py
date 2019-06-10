# -*- coding: utf-8 -*-
"""
@author: Miguel Ángel López Robles
"""


import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import DistanceMetric
import matplotlib.pyplot as plt
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



# PINN-LOF function
def pinn_lof(data, k=20, t=2, s=1, h = 20):
    n = data.shape[0]
    m = data.shape[1]


    ##########
    ## RP
    p1 = 1/(2*s)
    p0 = 1 - 1/s
    #first, we do the random project
    r = np.array([ np.random.choice( [1,0,-1],p = [p1, p0, p1]) for i in range(m*t)] )
    r = np.reshape(r,(m, t))

    #r = np.fromfunction( generator_n(s), (data.shape[0],t) )
    y = np.dot(data,r)
    #print(x)
    #print(y.shape)
    #print(y)
    #print(r)

    ################
    ## PINN
    c_nbrs = NearestNeighbors(n_neighbors=h, algorithm='ball_tree').fit(y)

    ### find the h-nearest-neighbours in the projection
    c_distances, c_indices = c_nbrs.kneighbors(y)


    ### map the points is easy because we use the indices
    distances= np.array([])
    distances = np.reshape(distances,(-1,k))

    indices= np.array([],dtype= np.int)
    indices = np.reshape(indices,(-1,k))

    for i in range(n):
        ##calculate the k-neighbor in the local neighbours
        nbrs = NearestNeighbors(n_neighbors=k, algorithm='ball_tree').fit(data[ c_indices[i]])
        l_distances, l_indices = nbrs.kneighbors( np.reshape(data[i],(-1,m)) )

        #we have indices of the local neighbors, need the indices of the data
        #print(l_indices)
        l_indices = c_indices[i,l_indices]
        l_indices = np.reshape(l_indices,(1,k))
        #print(l_indices)

        l_distances = np.reshape(l_distances,(1,k))
        #print(l_distances)
        distances = np.concatenate( (distances, l_distances), axis=0)
        indices = np.concatenate( (indices, l_indices), axis=0)
        
    print("hi")
    print(distances.shape)
    print(distances)

    print("hi")
    print(indices.shape)
    print(indices)

    #######
    ###LOF
    n_points = distances.shape[0]
    reach_d = [ [ max( (distances[i, j], distances[indices[i,j],k-1] ) ) for j in range(k) ] for i in range(n_points) ]
    reach_d = np.array(reach_d)

    ave_reach_d = np.mean(reach_d,axis=1)
    
    meany = 1 / np.array( [ [ ave_reach_d[i] for i in indices[j]] for j in range(n_points)] )
    meany = np.mean(meany,axis=1)
    #print("Mean y in Lx")
    #print(meany)

    lof = ave_reach_d * meany

    return lof



x = np.linspace(0,100,100)

x = np.reshape(x,(-1,20))




########################
### test with data generated
##################
np.random.seed(42)

# Generate train data
X_inliers = 0.3 * np.random.randn(100, 2)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]

# Generate some outliers
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
X = np.r_[X_inliers, X_outliers]

n_outliers = len(X_outliers)
ground_truth = np.ones(len(X), dtype=int)
ground_truth[-n_outliers:] = -1


# use my function
coef = pinn_lof(X,k=20)
#print(coef)



probedata = clf.fit_predict(data)
print(clf.threshold_)


plt.title("Local Outlier Factor (LOF)")
plt.scatter(X[:, 0], X[:, 1], color='k', s=3., label='Data points')
# plot circles with radius proportional to the outlier scores
radius = (coef - coef.min()) / (coef.max() - coef.min())
plt.scatter(X[:, 0], X[:, 1], s=500 * coef, edgecolors='r',
            facecolors='none', label='Outlier scores')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
#plt.xlabel("prediction errors: %d" % (n_errors))
legend = plt.legend(loc='upper left')
legend.legendHandles[0]._sizes = [10]
legend.legendHandles[1]._sizes = [20]
plt.show()




# Generate train data
X_inliers = 0.3 * np.random.randn(100, 200)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]

# Generate some outliers
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 200))
X = np.r_[X_inliers, X_outliers]

n_outliers = len(X_outliers)
ground_truth = np.ones(len(X), dtype=int)
ground_truth[-n_outliers:] = -1


# use my function
coef = pinn_lof(X,k=20)
#print(coef)
'''



class PINN_LOF(base):
    def __init__(self, k=20, t=2, s=1, h =20):
        self.k = k
        self.t = t
        self.s = s
        self.h =h

    
    def fit_predict(self, data):
        
        n = data.shape[0]
        m = data.shape[1]


        ##########
        ## RP
        p1 = 1/(2* self.s)
        p0 = 1 - 1/ self.s
        #first, we do the random project
        r = np.array([ np.random.choice( [1,0,-1],p = [p1, p0, p1]) for i in range(m*self.t)] )
        r = np.reshape(r,(m, self.t))

        #r = np.fromfunction( generator_n(s), (data.shape[0],t) )
        y = np.dot(data,r)
        #print(x)
        #print(y.shape)
        #print(y)
        #print(r)

        ################
        ## PINN
        c_nbrs = NearestNeighbors(n_neighbors=self.h, algorithm='ball_tree').fit(y)

        ### find the h-nearest-neighbours in the projection
        c_distances, c_indices = c_nbrs.kneighbors(y)


        ### map the points is easy because we use the indices
        distances= np.array([])
        distances = np.reshape(distances,(-1,self.k))

        indices= np.array([],dtype= np.int)
        indices = np.reshape(indices,(-1, self.k))

        for i in range(n):
            ##calculate the k-neighbor in the local neighbours
            nbrs = NearestNeighbors(n_neighbors=self.k, algorithm='ball_tree').fit(data[ c_indices[i]])
            l_distances, l_indices = nbrs.kneighbors( np.reshape(data[i],(-1,m)) )

            #we have indices of the local neighbors, need the indices of the data
            #print(l_indices)
            l_indices = c_indices[i,l_indices]
            l_indices = np.reshape(l_indices,(1,self.k))
            #print(l_indices)

            l_distances = np.reshape(l_distances,(1,self.k))
            #print(l_distances)
            distances = np.concatenate( (distances, l_distances), axis=0)
            indices = np.concatenate( (indices, l_indices), axis=0)

        #######
        ###LOF
        n_points = distances.shape[0]
        reach_d = [ [ max( (distances[i, j], distances[indices[i,j],self.k-1] ) ) for j in range(self.k) ] for i in range(n_points) ]
        reach_d = np.array(reach_d)

        ave_reach_d = np.mean(reach_d,axis=1)
        
        meany = 1 / np.array( [ [ ave_reach_d[i] for i in indices[j]] for j in range(n_points)] )
        meany = np.mean(meany,axis=1)
        #print("Mean y in Lx")
        #print(meany)

        lof = ave_reach_d * meany

        return lof
