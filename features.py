import numpy as np
import cv2

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


def LBP(img):
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

img = cv2.imread("t.jpg")
img1 = cv2.imread("t.jpg",0)
transformed_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y,cr,cb = cv2.split(transformed_img)

# cv2.imshow('thresholded image', LBP(cr))

blocks = np.zeros(transformed_img.shape)
im_h, im_w = (transformed_img.shape[:2])
bl_h, bl_w = 16, 16

print(transformed_img[0])
print("++++++++++++++++")
print(img[0])
cv2.imshow('thresholded image', LBP(img1))


#TRY to apply LBP to each block instead of all of it 

# for row in np.arange(im_h - bl_h + 1, step=bl_h):
#     for col in np.arange(im_w - bl_w + 1, step=bl_w):
#         print(img[row:row+bl_h, col:col+bl_w])
#         blocks[row:row+bl_h, col:col+bl_w] = LBP(img[row:row+bl_h, col:col+bl_w])
        # if(row==0 and col ==0):
        #     print(img[row:row+bl_h, col:col+bl_w])
        #     print("+++++++++++++++++++++++++++++")

        
# print(blocks)
# cv2.imshow('img',blocks)
cv2.waitKey(0)
cv2.destroyAllWindows()