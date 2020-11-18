from pafy import new
print("program by MrXD")
print("snap:ss75sa")
url = input('enter you link here: ')
video = new(url)
dl = video.getbest()
dl.download()
