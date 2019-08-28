# -*- coding: utf-8 -*-
"""
@author: Miguel Ángel López Robles
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
#from PyDBOD.lof import LOF

import sys
sys.path.append("..")
from odin import ODIN
from load import load_data


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


y = np.zeros(200,dtype=np.int)
y_outlier = np.ones(20,dtype=np.int)
y = np.append(y, y_outlier)

# use my class
odin = ODIN(t=5)
coef = odin.fit_predict(X)
#print(coef)


'''
probedata = clf.fit_predict(data)
print(clf.threshold_)
'''
color = np.array(['k','b'])


plt.title("Outlier Detection using Indegree Number (ODIN)")
plt.scatter(X[:, 0], X[:, 1], color=color[y], s=3., label='Data points')
# plot circles with radius proportional to the outlier scores

plt.scatter(X[:, 0], X[:, 1], s=200 * coef, edgecolors='r',
            facecolors='none', label='Outlier scores')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
#plt.xlabel("prediction errors: %d" % (n_errors))
legend = plt.legend(loc='upper left')
legend.legendHandles[0]._sizes = [10]
legend.legendHandles[1]._sizes = [20]
plt.show()

'''
y = np.zeros(200)
y_outlier = np.ones(20)
y = np.append(y, y_outlier)

'''
fpr, tpr, _ = roc_curve(y,coef)
roc_auc = auc(fpr, tpr)

print(roc_auc)
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ODIN')
plt.legend(loc="lower right")
plt.show()




import os
os.chdir("..")
###############################
## load a file

data = load_data("./data/shuttle-c0-vs-c4.dat")  # k = 20
#data = load_data("./data/glass5.dat", sep = ', ') #k=19
#data = load_data("./data/ecoli-0-1-3-7_vs_2-6.dat") #k=25
#data = load_data("./data/yeast5.dat", sep = ', ')

odin = ODIN(k=600, t=124)
coef = odin.fit_predict(data[:,:-1])
#coef_n = (coef - coef.min()) / (coef.max() - coef.min())
#print(coef)
#print(coef_n)

fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)

print(roc_auc)
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ODIN')
plt.legend(loc="lower right")
plt.show()