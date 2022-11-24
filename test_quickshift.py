import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel
from skimage.segmentation import quickshift
from skimage.segmentation import mark_boundaries
from skimage import io
from skimage.color import rgb2gray

img = io.imread('images/0.jpg')
segments = quickshift(img, kernel_size=9, max_dist=6, ratio=0.5)

fig, ax = plt.subplots()
ax.imshow(mark_boundaries(img, segments))
plt.show()