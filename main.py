import cv2,csv,joblib
import numpy as np
import stitcher

#resizes any images that are to fa- ... i mean large
def find_size(img):
    y = img.shape[0]
    x = img.shape[1]
    for z in range(2,max(x,y)):
        if x < 256 and y < 256:
                return(x,y)
        while y%z == 0 and x%z == 0:
            if x < 256 and y < 256:
                return(x,y)
            y //= z
            x //= z
    while y>256 or x>256:
        y //=2
        x //=2
    return(x,y)

# main script
#look at the print statement to figuire the rest out

file = input('Please enter the name and file extension of your image (example.png): ')

img = cv2.imread(file)

print('If your image is not already smaller than 256px by 256px, it will be downscaled until it is the same or smaller...')

print('Downscaling...')

if img.shape[0] > 256 or img.shape[1] > 256:
    img = cv2.resize(img, dsize=find_size(img), interpolation=cv2.INTER_CUBIC)

print('Downscaled to ' + str(img.shape[1]) + 'px by ' + str(img.shape[0]) + 'px! Importing model...')

model = joblib.load('model.joblib')

print('Model imported! Generating csv...')

header = ['block','x','y']

f = open((file + '.csv'),'w',newline='')

writer = csv.writer(f)

writer.writerow(header)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        rgb = np.flipud(img[y,x])
        block = model.predict([rgb])
        writer.writerow([block[0],x,y])
        f.flush()
    

print('csv generated! Final image being created...')

stitcher.stitch((file + '.csv'),(img.shape[1],img.shape[0]))

print('Image succcessfully created! Exiting program...')