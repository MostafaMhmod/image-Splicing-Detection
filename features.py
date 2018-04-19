import sys
import cv2
import numpy as np
from math import pi as PI
from matplotlib import pyplot as plt
from scipy import fftpack



def thresholded(center, pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out

def get_pixel_else_0(l, idx, idy, default=0):
    try:
        return l[idx,idy]
    except IndexError:
        return default

img = cv2.imread('img.jpg', 0)
transformed_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

for x in range(0, len(img)):
    for y in range(0, len(img[0])):
        center        = img[x,y]
        top_left      = get_pixel_else_0(img, x-1, y-1)
        top_up        = get_pixel_else_0(img, x, y-1)
        top_right     = get_pixel_else_0(img, x+1, y-1)
        right         = get_pixel_else_0(img, x+1, y )
        left          = get_pixel_else_0(img, x-1, y )
        bottom_left   = get_pixel_else_0(img, x-1, y+1)
        bottom_right  = get_pixel_else_0(img, x+1, y+1)
        bottom_down   = get_pixel_else_0(img, x,   y+1 )

        values = thresholded(center, [top_left, top_up, top_right, right, bottom_right,
                                      bottom_down, bottom_left, left])

        weights = [1, 2, 4, 8, 16, 32, 64, 128]
        res = 0
        for a in range(0, len(values)):
            res += weights[a] * values[a]

        transformed_img.itemset((x,y), res)

    print(x)

def get_2D_dct(img):
    return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')

cv2.imshow('image', img)
cv2.imshow('thresholded image', transformed_img)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(transformed_img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
get_2D_dct(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

