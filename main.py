import cv2 as cv
from PIL import Image
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
SOURCE = config['files Path']['sourceFile']
DESTINATION = config['files Path']['destinationFile']
img = cv.imread(SOURCE,0)
_ = img.shape

for i in range(_[0]):
    for j in range(_[1]):
        if img[i,j] > 200:
            img[i,j] = 255
                  
cv.imwrite(DESTINATION,img)
img = Image.open(DESTINATION)
img = img.convert("RGBA")
datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        if item[0] > 150:
            newData.append((0, 0, 0, 255))
        else:
            newData.append(item)
#             print(item)


img.putdata(newData)
img.save(DESTINATION, "PNG")