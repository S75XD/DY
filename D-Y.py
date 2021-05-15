#المكتبات المستخدمه
from pafy import new
import os,pyfiglet
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
#pip install pafy
#install youtube.dl
#pip install pyfiglet==0.7
#=======3=============
print('''
[1]Checkers YouTube-S-تشيكرز يتيوب
[2]Download video-7-تحميل مقطع MP3
[3]Download the video of the highest quality-5-تحميل المقطع اعلى جوده
[4]Knowing the qualities-X-معرفة الجودات
[5]Download libraries-D-تحميل المكتبات
''')
#الكود المستخدم
A5 = input('ضع رقم الاداة  to 5 -->: ')

if A5 == '1':
    url = input('enter you link here: ')
    video = new(url)
    print(video)
    
#XD
elif A5 == '2':
    url = input('enter you link here: ')
    video = new(url)
    audio = video.audiostreams
    audio[0].download()

#S75XD
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
        

elif A5 =='5':
    os.system('pip install pafy')
    os.system('pip install youtube_dl')
    os.system('pip install pyfiglet==0.7')
    
#تم
logg = pyfiglet.figlet_format("Done")
print(logg)

######################################
