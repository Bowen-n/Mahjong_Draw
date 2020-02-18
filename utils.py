import cv2

import os

src = './res'
target = './res_test'
files = os.listdir(src)
for file in files:
    full_path = os.path.join(src, file)
    img = cv2.imread(full_path)
    resized = cv2.resize(img, (41, 53))
    tar_path = os.path.join(target, file)
    cv2.imwrite(tar_path, resized)

img = cv2.imread('./test.png')
print(img.shape)