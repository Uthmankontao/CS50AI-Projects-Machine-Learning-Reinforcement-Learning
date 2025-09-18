#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:48:05 2020

@author: berar
"""

import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    
    def __init__(self):
        self.K=10 # on crée un bandit avec 10 bras --> les 10 leviers du bandit manchot
        np.random.seed(5) # pour obtr tjr le meme rslt.
        self.variance = np.random.randint(-1,2,size=self.K) # ensuite dans un tbl de taille = au nbre de bras on mets
        # aleatoirement des valeurs entieres entre -1 et 1
        self.biais = np.random.poisson(3,self.K) # tableau de taille 10 tiré d'une loi poisson  de taille 3. cela fixe un biais de recompense pour chaque bras
        while sum(self.biais == self.biais.max()) != 1 : # force la condition qu’un seul bras a le biais maximum (pas plusieurs)
            self.biais = np.random.poisson(3,self.K)
  
    def get_arm(self,k):
        """simule la recompense quand on tire le bras k.
        La récompense est un nombre aléatoire tiré d’une
        loi de Poisson de moyenne 6 + variance[k], puis on ajoute le biais du bras k.""" 

        reward  = np.random.poisson(6+self.variance[k]) + self.biais[k]
        return reward


if __name__ == "__main__":
    K=10
    T=500
    bandits = [[]]
    for k in range(K-1):
        bandits.append([]) # bandits est donc une liste de 10 listes dont une par bras pour stocker les récompenses observées

    myBandit = Bandit()

    for t in range(T):
        k = np.random.randint(0,K)
        reward = myBandit.get_arm(k)
        print(k,reward)
        bandits[k].append(reward)
    

    fig = plt.figure()
    plt.violinplot(bandits)
    plt.show()
