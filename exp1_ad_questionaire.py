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

# maximizer
df_m = pandas.read_csv("https://raw.githubusercontent.com/impudding/Maximizer-Saticeficer/master/data/ad-questionaire-maximizer.csv")

print('\nMAXIMIZER\n')
# ad recognotion
ad_recog_data = rp.summary_cont(df_m.groupby(['size', 'RL', 'hashtag']))['ad_recog']
print('ad recognition\n')
display(ad_recog_data)
#ad_recog_data.to_csv('m_out.csv', sep='\t', encoding='utf-8')

model = ols('ad_recog ~ C(size)*C(RL)*C(hashtag)', df_m).fit()
# Seeing if the overall model is significant
print(f"\nOverall model F({model.df_model: .0f},{model.df_resid: .0f}) = {model.fvalue: .3f}, p = {model.f_pvalue: .4f}")

# brand attitude
brand_data = rp.summary_cont(df_m.groupby(['size', 'RL', 'hashtag']))['brand']
print('brand attitude\n')
display(brand_data)
#brand_data.to_csv('m_out.csv', sep='\t', encoding='utf-8')
model = ols('brand ~ C(size)*C(RL)*C(hashtag)', df_m).fit()
# Seeing if the overall model is significant
print(f"\nOverall model F({model.df_model: .0f},{model.df_resid: .0f}) = {model.fvalue: .3f}, p = {model.f_pvalue: .4f}")

# purchase intention
purch_intent_data = rp.summary_cont(df_m.groupby(['size', 'RL', 'hashtag']))['purch_intent']
print('purchase intention\n')
display(purch_intent_data)

#intention to spread eWOM
eWOM_data = rp.summary_cont(df_m.groupby(['size', 'RL', 'hashtag']))['eWOM']
print('intention to spread eWOM\n')
display(eWOM_data)

#intention to purchase
purchase_data = rp.summary_cont(df_m.groupby(['size', 'RL', 'hashtag']))['purchase']
print('intention to purchase\n')
display(purchase_data)


print('\nSATICEFICER\n')

# saticeficer
df_s = pandas.read_csv("https://raw.githubusercontent.com/impudding/Maximizer-Saticeficer/master/data/ad-questionaire-saticeficer.csv")

# ad recognotion
ad_recog_data = rp.summary_cont(df_s.groupby(['size', 'RL', 'hashtag']))['ad_recog']
print('ad recognition\n')
display(ad_recog_data)

# brand attitude
brand_data = rp.summary_cont(df_s.groupby(['size', 'RL', 'hashtag']))['brand']
print('brand attitude\n')
display(brand_data)

# purchase intention
purch_intent_data = rp.summary_cont(df_s.groupby(['size', 'RL', 'hashtag']))['purch_intent']
print('purchase intention\n')
display(purch_intent_data)

#intention to spread eWOM
eWOM_data = rp.summary_cont(df_s.groupby(['size', 'RL', 'hashtag']))['eWOM']
print('intention to spread eWOM\n')
display(eWOM_data)

#intention to purchase
purchase_data = rp.summary_cont(df_s.groupby(['size', 'RL', 'hashtag']))['purchase']
print('intention to purchase\n')
display(purchase_data)














