import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel
from skimage.segmentation import felzenszwalb
from skimage.segmentation import mark_boundaries
from skimage import io
from skimage.color import rgb2gray

img = io.imread('images/8.jpg')
segments = felzenszwalb(img, scale=100, sigma=0.5, min_size=150)

fig, ax = plt.subplots()
ax.set_title("Felzenszwalb Segmentation")
ax.imshow(mark_boundaries(img, segments))
plt.show()