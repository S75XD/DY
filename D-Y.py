#المكتبات المستخدمه
from pafy import new 
import pyfiglet
#=======1===============

#حقوق مستر اكس دي
log = pyfiglet.figlet_format("by MrXD")
print(log)
#=========2============

#لازم تحمل الموجودين
#print("1-pip install pafy")
#print("2-install youtube.dl")
#=======3=============

#الكود المستخدم
url = input('enter you link here: ')
video = new(url)
dl = video.getbest()
dl.download()
