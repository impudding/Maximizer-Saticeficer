#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:10:22 2019

@author: yun-chen
"""
import pandas as pd
import researchpy as rp
import seaborn as sns
import scipy.stats as stats

import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats.multicomp

df = pandas.read_csv("https://raw.githubusercontent.com/impudding/Maximizer-Saticeficer/master/saticeficer-ad-questionaire.csv")

# ad recognotion
ad_recog_data = rp.summary_cont(df.groupby(['size', 'RL', 'hashtag']))['ad_recog']
display(ad_recog_data)

# brand attitude
brand_data = rp.summary_cont(df.groupby(['size', 'RL', 'hashtag']))['brand']
display(brand_data)

# purchase intention
purch_intent_data = rp.summary_cont(df.groupby(['size', 'RL', 'hashtag']))['purch_intent']
display(purch_intent_data)

#intention to spread eWOM
eWOM_data = rp.summary_cont(df.groupby(['size', 'RL', 'hashtag']))['eWOM']
display(eWOM_data)

#intention to purchase
purchase_data = rp.summary_cont(df.groupby(['size', 'RL', 'hashtag']))['purchase']
display(purchase_data)