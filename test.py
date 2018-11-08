from matplotlib.font_manager import FontProperties
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pdf_=pd.read_csv("phrase_reg.csv",header=None)


zhfont = FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf', size=14)
plt.figure(figsize=[14,20])
sns.set(font=zhfont.get_name())
print(pdf_)
sns.barplot(0, 1, palette="RdBu_r", data=pdf_.head(20))
#sns.barplot(0, 1, palette="RdBu_r", data=pdf_.head(-10))

plt.show()