from bs4 import BeautifulSoup
import os
import requests
import re
from openpyxl import Workbook

#init_sheet
wb=Workbook()
sheet=wb.create_sheet("job_",index=0)
sheet.column_dimensions['A'].width = 6
sheet.column_dimensions['B'].width = 20
sheet.column_dimensions['C'].width = 20
sheet.column_dimensions['D'].width = 12
sheet.column_dimensions['E'].width = 15
sheet.column_dimensions['F'].width = 30
sheet.column_dimensions['G'].width = 100
sheet.column_dimensions['H'].width = 10
##clwer_web
url_all=["https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
			]


for j in range(72):
    url=url_all[j]
    t=requests.get(url,stream=True, timeout = 500).text.encode("iso-8859-1").decode("gbk").encode("utf-8")
    soup=BeautifulSoup(t,"html.parser")
    t1=soup.find_all("a", attrs={'target':'_blank'})
    t3=soup.find_all("span",class_="t3")
    t4=soup.find_all("span",class_="t4")
    t5=soup.find_all("span",class_="t5")

    for i in range(3,103):
        if(i%2!=0):
            gourp=[]
            gourp.append(t5[int(i/2)].text.strip())#发布时间
            gourp.append(t1[i].get('title'))#职位名
            gourp.append(t1[i+1].get("title"))#公司名
            gourp.append(t3[int(i/2)].text.strip())#工作地点
            gourp.append(t4[int(i/2)].text.strip())#薪资
            
            print("第"+str(j+1)+"页第"+str(int(i/2))+"个....")
            context=""
            type_=""
            url=t1[i].get('href')
            check_normal_url=re.search(".html",url)
            if check_normal_url:
                    html=requests.get(url,stream=True, timeout = 500).text
                    s=BeautifulSoup(html,"html.parser")
                    ltype=s.find("p",class_="msg ltype").text.strip()
                    re_type=ltype.split("|",5)
                    for n in range(1,len(re_type)-2):
                            type_=type_+re_type[n]+"|"
                            #print(type_)
                    for item in s.find_all("div",class_="bmsg job_msg inbox"):
                            context=str(item.text.strip()).encode("utf-8",errors="ignore")
                    gourp.append(type_)#要求类型
                    gourp.append(context)#职位信息
                    gourp.append(t1[i].get('href'))#子链接
                    try:
                            sheet.append(gourp)
                            raise print(t1[i].get('href')+"  "+t1[i].get('title'))
                    except Exception:
                            pass   
    n_page= soup.find_all("li",class_="bk")
    url_all.append(n_page[-1].a.get("href"))
    print(n_page[-1].a.text.strip()+"  "+str(j+2))
wb.save('51jobs.xlsx')
 
