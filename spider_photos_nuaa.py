# -*- coding: utf-8 -*-  
import requests
from PIL import Image
from StringIO import StringIO
import os

#以下为http通信协议的头，cookie为身份认证信息
headers = {'Host':'ded.nuaa.edu.cn',   
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:44.0) Gecko/20100101 Firefox/44.0',
           'Referer':'http://ded.nuaa.edu.cn/JwSys/Manager/Messages.aspx?OPID=01706',
           'Cookie' :'mycookie'}

s=requests.Session()  #创建会话，可以保持cookie
s.headers.update(headers)  #默认headers参数

colleges = ['07','10','16']   #学院
years = ['12']      #年级
specials = ['1','2','3','4','5','6','7','8','9']   #专业
num_classes = ['01','02','03','04','05','06','07']    #班级

def num2str(num):          #将数字转换为字符串 如 1 转换为 '01'
    if ((num>0) & (num<10)):
        return '0'+str(num)
    else:
        return str(num)

for college in colleges:
    for year in years:
        for special in specials:
            for num_class in num_classes:
                error_count=0
                for people in range(1,40):
                    if error_count==3:
                        break
                    student = college + year + special + num_class + num2str(people)   #学号组成方法
                    picpath = college+'\\'+year+'\\'+special+num_class   #图片保存路径
                    pic_url='http://ded.nuaa.edu.cn/JwSys/Manager/Module/EASys/Controls/ImageHandler.ashx?ImageName=%s&BinaryType=xh' % student
                    while True:    #一直到成功发出get请求为止
                        try:
                            r = s.get(pic_url,timeout=40)   #GET命令获取图片
                            break
                        except:
                            print "timeout! Try again..."
                    try:
                        try:
                            Image.open(StringIO(r.content))
                            if not os.path.exists(picpath):
                                os.makedirs(picpath)
                        except:
                            error_count=error_count+1
                            print 'no class!'
                        Image.open(StringIO(r.content)).save('%s/%s.jpg' % (picpath,student))   #保存图片
                        print student+'succesful!'
                    except:
                        print student+'failed!'