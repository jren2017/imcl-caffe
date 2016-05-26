import skimage.io as skio
import os
import caffe
import random

IMG = "C:\\Users\\zhang\\Pictures\\Camera Roll\\10.jpg"

SIZE = 170
def load_image(img_path):
    if not os.path.exists(img_path):
        print '\tfile not exist {}'.format(img_path)
        return False
    img = caffe.io.load_image(img_path)
    return img

def cut_img(img_path):
    img = load_image(img_path)
    lenth = len(img[0,:,0])
    width = len(img[:,0,0])
    x = random.randint(0, width - SIZE)
    y = random.randint(0, lenth - SIZE)
    print x,y
    img = img[x:x+SIZE,y:y+SIZE,:]
    return img

def read_img(img_path):
    img = cut_img(img_path)
    skio.imshow(img)
    skio.show()

if __name__ == '__main__':
    read_img(IMG)