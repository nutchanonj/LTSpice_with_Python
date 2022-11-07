# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:24:46 2022

@author: nutch
"""

# import PyLTSpice
from PyLTSpice.LTSpiceBatch import SimCommander
from PyLTSpice import LTSpice_RawRead

import numpy as np
from numpy.polynomial import Polynomial as poly
import pandas as pd
from scipy.stats import linregress
from scipy import mean

W_list = [10,20,30,40,50]

LTC = SimCommander("N018_Char.asc")

# Read data and store it in Dataframe.
df = pd.DataFrame()
    
# Read data and store it in Dataframe.
LTC.run(run_filename="N018_Char.net")
LTC.wait_completion()
LTR = LTSpice_RawRead.RawRead("N018_Char.raw")
print("Read Success")
Id1 = LTR.get_trace("Id(M1)")
vgs = LTR.get_trace('vgs')
df['vgs'] = vgs.get_wave(0)
step = 0;
for W in W_list:
    df[f"Id(M1)_W={W:.1f}u"] = Id1.get_wave(step)
    step += 1
df = df.astype('float32')

# making polynomial fit, from threshold voltage.
V_tn = 0.400 # from datasheet.
V_end = 0.700 # fit to end of this voltage.
P_list = []
a_list = []
h_list = []
k_list = []
# polynomial eqn: y = a*(x-h)^2 + k

index_start = int(df.index[abs(df['vgs'] - V_tn) < 0.0001].tolist()[0])
index_end = int(df.index[abs(df['vgs'] - V_end) < 0.0001].tolist()[0]) + 1
for W in W_list:
    x = df['vgs'].tolist()[index_start:index_end]
    y = df[f"Id(M1)_W={W:.1f}u"].tolist()[index_start:index_end]
    P = poly.fit(x, y, 2).convert()
    P_list.append(P)
    c,b,a = P.coef
    a_list.append(a)
    h_list.append(-b/(2*a))
    k_list.append(-(b**2 - 4*a*c)/(4*a))
    
# find k' = mu_n*C_ox by slope.
WLratio_list = np.linspace(20, 100, 5)
result_lin = linregress(WLratio_list, a_list)
kn_prime = result_lin.slope * 2
print("V_threshold =", mean(h_list))
print("kn_prime =", kn_prime)
print("R_square =", result_lin.rvalue**2)

