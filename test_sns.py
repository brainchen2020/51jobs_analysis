# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:08:00 2018

@author: brainbot
"""
import pandas as pd
from matplotlib.font_manager import FontProperties
import seaborn as sns
zhfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=zhfont.get_name())
pdf_ = pd.read_csv("phrase_reg.csv",encoding="gb2312")
print(pdf_)
sns.barplot("phrase", "times", palette="RdBu_r", data=pdf_.head(10))