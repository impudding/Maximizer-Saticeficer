#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:22:44 2019

@author: yun-chen
"""

import pandas as pd
import seaborn as sns
from statsmodels.stats.anova import AnovaRM

#https://github.com/impudding/Maximizer-Saticeficer/blob/master/data/eye_and_adQuestionaire_maximizer.csv
df_m = pd.read_csv("https://github.com/impudding/Maximizer-Saticeficer/blob/master/data/eye_and_adQuestionaire_maximizer.csv",error_bad_lines=False)
sns.relplot(x='ad_recog',y='total_fix_dur_avr',data=df_m)
