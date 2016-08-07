import os
import sys
from PIL import Image

def resize(folder, fileName):
    filePath = os.path.join(folder, fileName)
    im = Image.open(filePath)
    pix = im.load()
    w, h  = im.size
    for wi in range(w):
        for hi in range(h):
	    if pix[wi,hi] >0:
		pix[wi,hi]=1
    #newIm = im.resize((int(w*factor), int(h*factor)))
    # i am saving a copy, you can overrider orginal, or save to other folder
    #newPath = filePath[:-9] + ".png" 
    im.save(filePath)

def bulkResize(imageFolder):
    imgExts = ["png", "bmp", "jpg"]
    for path, dirs, files in os.walk(imageFolder):
	
        for fileName in files:
	    #print (fileName[:-4])
            ext = fileName[-3:].lower()
            if ext not in imgExts:
                continue

            resize(path, fileName)

if __name__ == "__main__":
    imageFolder=sys.argv[1] # first arg is path to image folder
    #resizeFactor=float(sys.argv[2])/100.0# 2nd is resize in %
    bulkResize(imageFolder)
