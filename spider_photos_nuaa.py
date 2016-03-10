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

colleges = ['15']
years = ['12']
specials = ['2']
num_classes = ['02']

def num2str(num):
    if ((num>0) & (num<10)):
        return '0'+str(num)
    else:
        return str(num)

for college in colleges:
    for year in years:
        for special in specials:
            for num_class in num_classes:
                for people in range(1,40):
                    student = college + year + special + num_class + num2str(people)
                    r = requests.get('http://ded.nuaa.edu.cn/JwSys/Manager/Module/EASys/Controls/ImageHandler.ashx?ImageName=%s&BinaryType=xh' % student,headers=headers,timeout=20)   #GET命令获取图片
                    picpath = college+'\\'+year+'\\'+special+num_class
                    try:
                    #Image.open(StringIO(r.content)).show()    # 显示图片
                        try:
                            print student
                            Image.open(StringIO(r.content))
                            if not os.path.exists(picpath):
                                os.makedirs(picpath)
                        except:
                            print 'aa'
                        Image.open(StringIO(r.content)).save('%s/%s.jpg' % (picpath,student))   #保存图片
                        print student+'succesful!'
                    except:
                        print 'error'