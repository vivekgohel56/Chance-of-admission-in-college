# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:11:10 2020

@author: 91926
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class heatmap():
    def __init__(self, file_name):
        self.file_name = file_name
    def corrmat(self):
        rf = self.file_name
        df = pd.read_csv(rf)
        cormat = df.corr()
        f, ax = plt.subplots(figsize=(12, 9))
        hmp = sns.heatmap(cormat, vmax=.8, square=True);
        return hmp