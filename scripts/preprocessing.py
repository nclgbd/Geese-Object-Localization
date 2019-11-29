import cv2 as cv
import numpy as np
import os

PRE_PATH = 'preprocessed_geese/'
POST_PATH = 'geese/images/'
def process_images():
    num = 1
    for goose in os.listdir(PRE_PATH):
        file = os.path.join(PRE_PATH, goose)
        old_file = cv.imread(file)
        prefix = get_prefix(num) + str(num)
        cv.imwrite(prefix+'.jpg', old_file)
        print(prefix)
        num += 1
        
def get_prefix(num):
    length = 5
    prepend = '0' * (length - len(str(num)))
    return prepend
    
        
process_images()