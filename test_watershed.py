import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel
from skimage.segmentation import watershed
from skimage.segmentation import mark_boundaries
from skimage import io
from skimage.color import rgb2gray

img = io.imread('images/8.jpg')

gradient = sobel(rgb2gray(img))
segments_watershed = watershed(gradient, markers=250, compactness=0.001)

fig, ax = plt.subplots()
ax.imshow(mark_boundaries(img, segments_watershed))
plt.show()