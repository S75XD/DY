#المكتبات المستخدمه
from pafy import new 
import pyfiglet
#=======1===============

#حقوق مستر اكس دي
print('''

 /$$      /$$           /$$   /$$ /$$$$$$$ 
| $$$    /$$$          | $$  / $$| $$__  $$
| $$$$  /$$$$  /$$$$$$ |  $$/ $$/| $$  \ $$
| $$ $$/$$ $$ /$$__  $$ \  $$$$/ | $$  | $$
| $$  $$$| $$| $$  \__/  >$$  $$ | $$  | $$
| $$\  $ | $$| $$       /$$/\  $$| $$  | $$
| $$ \/  | $$| $$      | $$  \ $$| $$$$$$$/
|__/     |__/|__/      |__/  |__/|_______/ 
                                           
                                                                                      
''')
print('''
=========================
=      My rights        =
=     snap:ss75sa       =
=    twitter:@S75XD     =
=   telegram:@S75XD     =
========================= 
''')
#=========2============

#لازم تحمل الموجودين
#print("1-pip install pafy")
#print("2-install youtube.dl")
#=======3=============
print('''
[1]تشيكرز يتيوب
[2]تحميل مقطع MP3
[3]تحميل المقطع اعلى جوده
[4]تحميل المقطع مع اختيار الجوده
''')
#الكود المستخدم
A5 = input('ضع رقم الاداة  to 4 -->: ')

if A5 == '1':
    url = input('enter you link here: ')
    video = new(url)
    print(video)


elif A5 == '2':
    url = input('enter you link here: ')
    video = new(url)
    audio = video.audiostreams
    audio[0].download()


elif A5 =='3':
    url = input('enter you link here: ')
    video = new(url)
    dl = video.getbest()
    dl.download()


elif A5 =='4':
    url = input('enter you link here: ')
    video = new(url)
    stream = video.streams
    for i in stream:
        print(i)


#تم
logg = pyfiglet.figlet_format("Done")
print(logg)
