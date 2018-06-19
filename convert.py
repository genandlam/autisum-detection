#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:54:41 2018

@author: genevieve
"""

import scipy.io
import numpy as np

data = scipy.io.loadmat("autism_diag_train.mat")
for i in data: 
    
       if i== "diag_train_dys4":
           train_dys4=data[i]
       if i== "diag_train_nos3":
           train_nos3=data[i]
       if i=='diag_train_pdd2':
           train_pdd2=data[i]
       if i=='diag_train_typ1':
           train_typ1=data[i]
train_data=[]           
train_data=np.concatenate(( train_dys4,train_nos3, train_pdd2,train_typ1),axis=0)

print (train_data.shape[0])      

data = scipy.io.loadmat("autism_diag_devel.mat")
for i in data: 
    
       if i== "diag_devel_dys4":
           devel_dys4=data[i]
       if i== "diag_devel_nos3":
           devel_nos3=data[i]
       if i=='diag_devel_pdd2':
           devel_pdd2=data[i]
       if i=='diag_devel_typ1':
           devel_typ1=data[i]
devel_data=[]           
devel_data=np.concatenate(( devel_dys4,devel_nos3, devel_pdd2,devel_typ1),axis=0)

print (devel_data.shape[0])   
    
#for i in data:
#    if'__'not in i and 'readme' not in i:
#         np.savez(outfile, data[key])
        
        
#data = scipy.io.loadmat("autism_diag_test.mat")
#for i in data:
#    if'__'not in i and 'readme' not in i:
#        np.savetxt(("autism_diag_test"+".csv"),data[i],delimiter=',')
    

