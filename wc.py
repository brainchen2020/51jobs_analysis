from matplotlib.font_manager import FontProperties
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

###.filter(regex="技术").columns

def search_wrods(df,args):
    result_words=[]
    result_values=[]
    for index, row in df.iterrows():
        if len(args) == 0:
            result_words.append(row[0])
            result_values.append(row[1])
        for i in  range(len(args)):
            if args[i] in row[0]:
                #print(row[0])
                #print(row[1])
                result_words.append(row[0])
                result_values.append(row[1])


    return result_words,result_values
def plot(words,values,head):
    pdf=pd.DataFrame({"key":words,
                      "value":values})
    zhfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)
    plt.figure(figsize=[14,20])
    sns.set(font=zhfont.get_name())
    sns.barplot("key", "value", palette="RdBu_r", data=pdf.head(head))
    plt.show()

search_arr=["技术","代码","模型"]
df =pd.read_csv('phrase_reg.csv',header=None,encoding="utf-8")
words,values=search_wrods(df,[])
plot(words,values,20)