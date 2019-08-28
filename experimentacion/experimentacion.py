
#from PyDBOD import load
from PyDBOD import load, lof, loop, ldof, pinn_lof, outres, odin, meandist, kdist
import numpy as np
from sklearn.metrics import roc_curve, auc
from pyod.models.loci import LOCI


files = np.array(["ecoli4.dat","ecoli-0-1-3-7_vs_2-6.dat",
                "glass2.dat","glass4.dat","glass5.dat","glass-0-1-6_vs_2.dat","glass-0-1-6_vs_5.dat",
                "page-blocks-1-3_vs_4.dat","shuttle-c0-vs-c4.dat","shuttle-c2-vs-c4.dat",
                "vowel0.dat","yeast4.dat","yeast5.dat","yeast6.dat","yeast-0-5-6-7-9_vs_4.dat",
                "yeast-1-2-8-9_vs_7.dat","yeast-1-4-5-8_vs_7.dat",
                "yeast-1_vs_7.dat","yeast-2_vs_4.dat","yeast-2_vs_8.dat"])

rep_rand = 5
np.random.seed(0)
## we can't use a loop, because we use paramater for each call.

### file0

data = load.load_data(files[0], sep = ', ')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=84)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=119, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=128)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=100, t=2, s=2, h =100)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=45, t=24)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=41, t=0.04)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=60, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


result = np.array(file_result)
print('hi')
##############################################################################
## file1

data = load.load_data(files[1], sep = ',')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=84)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=119, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=128)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=100, t=2, s=2, h =100)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=22, t=6)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=20, t=0.08)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=41, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


result = np.vstack((result,np.array(file_result)))
print('hi')


##############################################################################
## file2

data = load.load_data(files[2], sep = ', ')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=24)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=24, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=25, n= 15)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=40, t=1, s=1, h =40)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)



#ODIN
algorith = odin.ODIN(k=30, t=20)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=20, t=0.7)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=22, t=1.4)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file3

data = load.load_data(files[3], sep = ', ')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=165)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=166, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=180, n= 20)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=40, t=1, s=1, h =40)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=142, t=45)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=140, t=0.2)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=100, t=0.08)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file4

data = load.load_data(files[4], sep = ', ')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=19)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=23, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=21, n= 20)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=45, t=2, s=2, h =45)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN 
algorith = odin.ODIN(k=36, t=10)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=55, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=80, t=0.08)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')
##############################################################################
## file5

data = load.load_data(files[5], sep = ',')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=22)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=26, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=25, n= 20)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=30, t=2, s=2, h =33)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN 
algorith = odin.ODIN(k=30, t=18)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=30, t=1.2)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=20, t=1.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')


##############################################################################
## file6

data = load.load_data(files[6], sep = ',')  # k = 20
file_result = []

#lof
algorith = lof.LOF(k=21)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=22, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=22)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=18, t=2, s=2, h =19)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN 
algorith = odin.ODIN(k=21, t=9)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=22, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=20, t=0.12)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')


##############################################################################
## file7

data = load.load_data(files[7], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=300)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=310, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=315)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=300, t=2, s=2, h =310)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN 125
algorith = odin.ODIN(k=332, t=100)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=300, t=0.0008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=300, t=0.0015)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


result = np.vstack((result,np.array(file_result)))
print('hi')


##############################################################################
## file8

data = load.load_data(files[8], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=200)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=210, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=240)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=200, t=2, s=2, h =210)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN 
algorith = odin.ODIN(k=600, t=124)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=210, t=0.0008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=210, t=0.0008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file9

data = load.load_data(files[9], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=18)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=19, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=20)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=20, t=2, s=2, h =21)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN 
algorith = odin.ODIN(k=35, t=7)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=20, t=0.0008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=20, t=0.0008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file10

data = load.load_data(files[10], sep = ', ')  
file_result = []

#lof

algorith = lof.LOF(k=28)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=39, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=50)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=38, t=2, s=2, h =41)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN 
algorith = odin.ODIN(k=150, t=91)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=95, t=0.5)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=79, t=0.8)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')
##############################################################################
## file11

data = load.load_data(files[11], sep = ', ')  
file_result = []

#lof

algorith = lof.LOF(k=140)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=120, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=110)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=85, t=2, s=2, h =101)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN 
algorith = odin.ODIN(k=100, t=52)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=53, t=1.5)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=53, t=1.5)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file12

data = load.load_data(files[12], sep = ', ')  
file_result = []

#lof

algorith = lof.LOF(k=200)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=210, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=250)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=110, t=2, s=2, h =120)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN
algorith = odin.ODIN(k=117, t=41)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=155, t=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=155, t=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')



##############################################################################
## file13

data = load.load_data(files[13], sep = ', ')  
file_result = []

#lof

algorith = lof.LOF(k=310)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=390, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=390)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=330, t=2, s=2, h =350)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=312, t=208)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=316, t=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=316, t=0.02)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file14

data = load.load_data(files[14], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=200)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=290, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=390)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=250, t=2, s=2, h =300)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN
algorith = odin.ODIN(k=180, t=129)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=66, t=0.007)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=56, t=0.008)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')



##############################################################################
## file15

data = load.load_data(files[15], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=75)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=83, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=195)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=270, t=2, s=2, h =280)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN
algorith = odin.ODIN(k=75, t=30)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=190, t=0.025)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=190, t=0.02)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file16

data = load.load_data(files[16], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=35)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=13, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=19)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=192, t=2, s=2, h =200)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)


#ODIN
algorith = odin.ODIN(k=50, t=30)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=22, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=22, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)



#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')
##############################################################################
## file17

data = load.load_data(files[17], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=25)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=35, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=65)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=22, t=2, s=2, h =28)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=50, t=29)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=95, t=0.08)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=96, t=0.12)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')



##############################################################################
## file18

data = load.load_data(files[18], sep = ',')  
file_result = []

#lof

algorith = lof.LOF(k=275)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=295, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=275)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=142, t=2, s=2, h =148)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=295, t=157)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=210, t=0.024)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=250, t=0.031)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

##############################################################################
## file19

data = load.load_data(files[19], sep = ', ')  
file_result = []

#lof

algorith = lof.LOF(k=30)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#loop
algorith = loop.LOOP(k=28, lamda= 3)
coef = algorith.fit_predict(data[:,:-1])
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#ldof
algorith = ldof.LDOF(k=25)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#pinn_lof
algorith = pinn_lof.PINN_LOF(k=102, t=2, s=2, h =110)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

'''
#outres
algorith = outres.OUTRES(epsilon=15, alpha=0.01)
coef = algorith.fit_predict(data[:,:-1])
coef = np.absolute(1- coef)
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)
'''
file_result.append(0)

#ODIN
algorith = odin.ODIN(k=55, t=13)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#MeanDIST
algorith = meandist.MeanDIST(k=22, t=0.1)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

#kDIST
algorith = kdist.KDIST(k=30, t=0.032)
coef = algorith.fit_predict(data[:,:-1])
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)


#LOCI
clf = LOCI()
clf.fit(data[:,:-1])
coef= clf.decision_scores_
coef = np.abs(coef)
coef = (coef - coef.min()) / (coef.max() - coef.min())
fpr, tpr, _ = roc_curve(data[:,-1],coef)
roc_auc = auc(fpr, tpr)
file_result.append(roc_auc)

result = np.vstack((result,np.array(file_result)))
print('hi')

import pandas as pd

#dataset = pd.DataFrame({ 'Fichero':files, 'LOF':result[:,0],'LOOP':result[:,1],'LDOF':result[:,2],'PINN-LOF':result[:,3], 'OUTRES':np.repeat('-',result.shape[0]),
 #                       'LOCI':result[:,5] })

dataset = pd.DataFrame({ 'Fichero':files, 'LOF':result[:,0],'LOOP':result[:,1],'LDOF':result[:,2],'PINN-LOF':result[:,3], 'OUTRES':np.repeat('-',result.shape[0]), 
'ODIN':result[:,5], 'MeanDIST':result[:,6], 'kDIST':result[:,7], 'LOCI':result[:,8] })

#dataset['OUTRES'] = np.repeat('-',result.shape[0])


dataset.to_html('resultados.html')
print(result)