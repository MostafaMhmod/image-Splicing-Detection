import numpy as np
import cv2
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


def LBP_3x3(img):
    transformed_img=img

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
            values = thresholded(center, [top_left, top_up, top_right, right, bottom_right, bottom_down, bottom_left, left])
            weights = [1, 2, 4, 8, 16, 32, 64, 128]
            res = 0
            for a in range(0, len(values)):
                res += weights[a] * values[a]

            transformed_img.itemset((x,y), res)

    return transformed_img

def dct_2D(img):
    return fftpack.dct(fftpack.dct(img.T, norm='ortho').T, norm='ortho')



img = cv2.imread("t.jpg")
img1 = cv2.imread("t.jpg",0)
transformed_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y,cr,cb = cv2.split(transformed_img)


blocks = np.zeros(cr.shape)
im_h, im_w = (cr.shape[:2])
bl_h, bl_w = 16, 16

crChannelAfterLBP = LBP_3x3(cr)
dctMatrix=dct_2D(crChannelAfterLBP)



# cv2.imshow('thresholded image', LBP_3x3(cr))


#TRY to apply LBP_3x3 to each block instead of all of it for better results

# for row in np.arange(im_h - bl_h + 1, step=bl_h):
#     for col in np.arange(im_w - bl_w + 1, step=bl_w):
#         print(img[row:row+bl_h, col:col+bl_w])
#         blocks[row:row+bl_h, col:col+bl_w] = LBP_3x3(img[row:row+bl_h, col:col+bl_w])
        # if(row==0 and col ==0):
        #     print(img[row:row+bl_h, col:col+bl_w])
        #     print("+++++++++++++++++++++++++++++")

        
# print(blocks)
# cv2.imshow('img',blocks)

cv2.waitKey(0)
cv2.destroyAllWindows()