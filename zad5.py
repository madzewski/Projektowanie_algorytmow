import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import copy
import numpy as np

def e_dist(v, w):
    return math.sqrt((v[0] - w[0]) ** 2 + (v[1] - w[1]) ** 2)

def holes(N, K, D):
    holes = {}
    for d in range(int(K/D)+1):
        for p in range(int(N/D)+1):
            holes[(D*d,D*p)] = False 
    return holes


def plot_net(N, K, D):
    for y in range(int(K/D)+1):
        plt.plot([y*D,y*D],[0,N], 'k:')
    for x in range(int(N/D)+1):
        plt.plot([K,0],[x*D,x*D], 'k:') 
    
    

def plot_holes(N, K, D, b):
    for d in range(int(K/D)+1):
        for p in range(int(N/D)+1):
            if (D*d,D*p) in b:
                if b[(D*d,D*p)] == True:
                    plt.plot([D*d],[D*p], 'ro')
                else:
                    plt.plot([D*d],[D*p], 'ko')
            else:
                print("Brak wierzchołka")
    plt.show()


def boreholes(S,R,all_b):
    not_used_b = copy.copy(all_b)
    used_b = [(0,0)]
    not_used_b.pop((0,0))
    all_b[0,0] = True
    for x in range(R-1):
        if not_used_b:
            h = max_dist(not_used_b.keys(), used_b, S)
            if h == ():
                break
            used_b.append(h)
            not_used_b.pop(h)
            all_b[h] = True
        else:
            break
    return all_b


def max_dist(not_used_b, used_b, S):
    temp_max_dist = 0
    temp_b = ()
    for x in not_used_b:
        temp_dist = []
        control = False
        for z in used_b:
            if e_dist(z, x) < S:
                control = True
                break
            else:
                temp_dist.append(e_dist(z, x))
        if control == True:
            continue
        temp_mean = np.min(temp_dist)
        if temp_mean > temp_max_dist:
            temp_max_dist = temp_mean
            temp_b = x
    return temp_b
    

N, K = (6,6)
D = 2
S = 1
R = 10
all_b = holes(N,K,D)
b = boreholes(S, R, all_b)
plot_net(N,K,D)
plot_holes(N, K, D, b)
