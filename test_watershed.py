import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel
from skimage.segmentation import watershed
from skimage.segmentation import mark_boundaries
from skimage import io
from skimage.color import rgb2gray

img = io.imread('images/1.jpg')

gradient = sobel(rgb2gray(img))
segments = watershed(gradient, markers=250, compactness=0.0007)

fig, ax = plt.subplots()
ax.imshow(mark_boundaries(img, segments))
plt.show()