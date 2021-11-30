from PIL import Image,ImageFilter
import functools
state = Image.open("Alabama.png")
(x,y) = state.size
while x>2000 and y>2000:
    x = x//10
    y = y//10

state = state.resize((x,y))
start = state.filter(ImageFilter.FIND_EDGES)
bands = start.split()
onecolor = bands[2]
newmap = onecolor.point(lambda x: 255 if x<100 else 0) #https://opensource.com/article/20/8/edit-images-python

newmap.save("ALoutline.png")
