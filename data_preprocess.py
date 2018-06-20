#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:54:41 2018

@author: genevieve
"""

import scipy.io
import numpy as np

def convert_data():
    data = scipy.io.loadmat("autism_diag_train.mat")
    for i in data:
     if'__'not in i and 'readme' not in i:
        np.savetxt(("autism_diag_train"+".csv"),data[i],delimiter=',')
    
    data = scipy.io.loadmat("autism_diag_devel.mat")
    for i in data:
     if'__'not in i and 'readme' not in i:
        np.savetxt(("autism_diag_devel"+".csv"),data[i],delimiter=',')
    
    data = scipy.io.loadmat("autism_diag_test.mat")
    for i in data:
     if'__'not in i and 'readme' not in i:
        np.savetxt(("autism_diag_test"+".csv"),data[i],delimiter=',')
    

def retrieve_data(x):
    
    for i in x:
        data = scipy.io.loadmat(i)
        a=np.array([])
        for j in data:
           
           if'__'not in j and 'readme' not in j:
              if a.size==0 :
                 a=data[j]
                 
              else :
                 a= np.concatenate(( a,data[j]),axis=0)
                 
                 
        print (a.shape[0]) 
        if(i =="autism_diag_train.mat"):
            
            train_data=a
        if(i=="autism_diag_devel.mat"):
            
            devel_data=a     
        if(i=="autism_diag_test.mat"):
            
            test_data=a 
#        
#      
    return(train_data,devel_data,test_data)
    
#for i in data:
#    if'__'not in i and 'readme' not in i:
#         np.savez(outfile, data[key])
        
        

if __name__ == '__main__':
    convert_data()
    x=["autism_diag_train.mat","autism_diag_devel.mat","autism_diag_test.mat"]
    #train_data,devel_data,test_data=retrieve_data(x)

