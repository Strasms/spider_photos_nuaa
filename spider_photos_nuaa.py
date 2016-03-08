# -*- coding: utf-8 -*-  
import requests
import urllib
from PIL import Image
from StringIO import StringIO

#以下为http通信协议的头，cookie为身份认证信息
headers = {'Host':'ded.nuaa.edu.cn',   
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Language':'en-US,en;q=0.5',
           'Accept-Encoding':'gzip, deflate',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:44.0) Gecko/20100101 Firefox/44.0',
           'Referer':'http://ded.nuaa.edu.cn/JwSys/Manager/Messages.aspx?OPID=01706',
           'Cookie' :'mycookie'}

r = requests.get('http://ded.nuaa.edu.cn/JwSys/Manager/Module/EASys/Controls/ImageHandler.ashx?ImageName=151210101&BinaryType=xh',headers=headers,timeout=10)   #GET命令获取图片

Image.open(StringIO(r.content)).show()    # 显示图片
Image.open(StringIO(r.content)).save('me.jpg')   #保存图片