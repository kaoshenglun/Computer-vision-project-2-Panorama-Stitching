# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:36:46 2017

@author: HGY
"""

import numpy as np
from scipy.io import loadmat


#%% SIFTSimpleMatcher function
def SIFTSimpleMatcher(descriptor1, descriptor2, THRESH=0.7):
    '''
    SIFTSimpleMatcher 
    Match one set of SIFT descriptors (descriptor1) to another set of
    descriptors (decriptor2). Each descriptor from descriptor1 can at
    most be matched to one member of descriptor2, but descriptors from
    descriptor2 can be matched more than once.
    
    Matches are determined as follows:
    For each descriptor vector in descriptor1, find the Euclidean distance
    between it and each descriptor vector in descriptor2. If the smallest
    distance is less than thresh*(the next smallest distance), we say that
    the two vectors are a match, and we add the row [d1 index, d2 index] to
    the "match" array.
    
    INPUT:
    - descriptor1: N1 * 128 matrix, each row is a SIFT descriptor.
    - descriptor2: N2 * 128 matrix, each row is a SIFT descriptor.
    - thresh: a given threshold of ratio. Typically 0.7
    
    OUTPUT:
    - Match: N * 2 matrix, each row is a match. For example, Match[k, :] = [i, j] means i-th descriptor in
        descriptor1 is matched to j-th descriptor in descriptor2.
    '''

    #############################################################################
    #                                                                           #
    #                              YOUR CODE HERE                               #
    #                                                                           #
    #############################################################################
    match = []
    c=0
    N1= descriptor1.shape[0]
    N2= descriptor2.shape[0]
    for i in range(N1):
        tmp = np.tile(descriptor1[i,:],(N2,1))
        dist = np.sqrt((np.square(tmp-descriptor2)).sum(axis=1))
        x_position = np.argmin(dist)
        x = dist[x_position]
        y = min(np.delete(dist,x_position))
        if x < y*THRESH:
            match = np.append(match,[i,x_position])
            c=c+1
    match=np.reshape(match,(c,2))
    #############################################################################
    #                                                                           #
    #                             END OF YOUR CODE                              #
    #                                                                           #
    #############################################################################   
    
    return match
