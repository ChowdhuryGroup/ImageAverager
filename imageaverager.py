import cv2
from tkinter import Tk
from tkinter.filedialog import askdirectory, asksaveasfile
import os
import numpy as np

def addImages(imgList):
	finalImg = imgList[0]
	for img in imgList[1:]:
		finalImg = cv2.add(finalImg,img)
	return finalImg

def subImages(img1,img2):
	#img1-img2
	# print(cv2.absdiff(img2,img1))
	# print(cv2.subtract(img2,img1))
	# print(np.subtract(img1.astype(np.int16),img2.astype(np.int16)))
	# return cv2.subtract(img2,img1)
	return np.subtract(img1.astype(np.int32),img2.astype(np.int32))

def avgImages(imgList):
	avg_image = imgList[0]
	for i in range(len(imgList)):
	    if i == 0:
	        pass
	    else:
	        alpha = 1.0/(i + 1)
	        beta = 1.0 - alpha
	        #avg_image = cv2.addWeighted(imgList[i], alpha, avg_image, beta, 0.0)
	        avg_image = np.add(imgList[i],avg_image)
	    avg_image = np.divide(avg_image,2)
	return avg_image
def avgImages2(imgList):
	return np.average(imgList,axis=0)
#select path dialogue

path = askdirectory(title='Select Folder',initialdir=os.getcwd())

bkgs = []
durings = []

for shot in os.listdir(path):
	if shot.find(".") == -1:
		images=os.listdir(path+"/"+shot)
		images = [i for i in images if not '.' in i]
		images.sort()
		bkgs.append(cv2.imread(path+"/"+shot+"/"+images[0]+"/"+os.listdir(path+"/"+shot+"/"+images[0])[0],-1))
		durings.append(cv2.imread(path+"/"+shot+"/"+images[1]+"/"+os.listdir(path+"/"+shot+"/"+images[1])[0],-1))

bkgsubbed = []
for i in range(len(bkgs)):
	bkgsubbed.append(subImages(durings[i],bkgs[i]))

result = avgImages2(bkgsubbed)


# cv2.imshow("avged", result)
# cv2.waitKey(0)
cv2.imwrite(asksaveasfile(mode="w",defaultextension=".tiff",title="save avgedsubbedimage").name,result)