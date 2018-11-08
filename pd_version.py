import pandas as pd
import re
from collections import Counter
import seaborn as sns
import numpy as np
from matplotlib.font_manager import FontProperties




def translate(str):
    # print("origon data:"+str.decode("utf-8","ignore"))
    line = str.strip().decode('utf-8','ignore') #解码成unicode
    p2 = re.compile(u'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    outStr= "".join(p2.split(line)).strip()
    return outStr

## 指定列 usecols
## 指定表 sheet_name
## 指定表头 header
d = pd.read_excel("51jobs.xlsx",sheet_name=0,header=None,usecols=[6])
## 读行row shape[0]
## 读列column shape[1]

#print(d.values[0])
str_arr=""
for item in range(d.shape[0]-1):
    temp = ''.join(d.values[item])
    str_arr=str_arr+translate(temp.encode("utf-8"))
    
### 每一个function都会有Arguments（），这里面可以按shift+Tab
#print(Counter(str_arr))

#print(OrderedCounter(str_arr).keys())

dictionary_list_key=[]
dictionary_list_value=[]
dictionary_list=[]

for key , value in Counter(str_arr).items():
#    dictionary_list_key.append(key.encode("utf-8","ignore"))
    dictionary_list_value.append(int(value))
    temp=[key,value]
    dictionary_list.append(temp)
   

#print(dictionary_list_key)
#print(dictionary_list_value)
list_=sorted(dictionary_list,key=lambda dictionary_list:dictionary_list[1], 
             reverse=True)

#print(list_[0:10])
list_key=[]
list_value=[]
for i in range(30):
    list_key.append(list_[i][0])
    list_value.append(list_[i][1])
    
#print(dictionary_list)
#arr = np.array([dictionary_list_key,dictionary_list_value],
#               dtype=[('x', 'U25'), ('y', int)])
#print(list_key) 
#print(list_value)
df = pd.DataFrame({'col_key':list_key,
                  'col_value':list_value})
    
##处理seaborn 中文乱码问题
myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name())
sns.barplot("col_key", "col_value", palette="RdBu_r", data=df)
## sep 分个符
#wdf= pd.read_csv("wc_clear_phrase.csv",encoding="gb2312",sep='/')
#print(wdf)
