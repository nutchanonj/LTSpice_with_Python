# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:52:56 2022

@author: nutch
"""

# import PyLTSpice
from PyLTSpice.LTSpiceBatch import SimCommander
from PyLTSpice import LTSpice_RawRead

# import
import pandas as pd
from scipy.stats import linregress

Vgs_list = [0.4,0.5,0.6,0.7]

LTC = SimCommander("P018_Char.asc")

# Read data and store it in Dataframe.
df = pd.DataFrame()
    
# Read data and store it in Dataframe.
LTC.run(run_filename="P018_Char.net")
LTC.wait_completion()
LTR = LTSpice_RawRead.RawRead("P018_Char.raw")
print("Read Success")
Id1 = LTR.get_trace("Id(M1)")
vds = LTR.get_trace('vds')
df['vds'] = vds.get_wave(0)
step = 0;
for Vgs in Vgs_list:
    df[f"Id(M1)_Vgs={Vgs:.1f}"] = Id1.get_wave(step)
    step += 1
df = df.astype('float32')

# making linear fit.
V_start = 0.60 # fit from start of this Vds voltage.
V_end = 0.70 # fit to end of this Vds voltage.
L_list = []
a_list = []
b_list = []
yintc_list = []
# linear eqn: a*x + b = y

index_start = int(df.index[abs(df['vds'] - V_start) < 0.0001].tolist()[0])
index_end = int(df.index[abs(df['vds'] - V_end) < 0.0001].tolist()[0]) + 1
for Vgs in Vgs_list:
    x = df['vds'].tolist()[index_start:index_end]
    y = df[f"Id(M1)_Vgs={Vgs:.1f}"].tolist()[index_start:index_end]
    L = linregress(x,y)
    L_list.append(L)
    b = L.intercept; a = L.slope;
    a_list.append(a)
    b_list.append(b)
    V_A = -b/a
    yintc_list.append(V_A)
    print(f"For Vgs={Vgs:.1f} V, Early voltage is V_A={V_A:.2f} V")
