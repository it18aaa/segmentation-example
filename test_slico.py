import matplotlib.pyplot as plt
import numpy as np
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage import io

img = io.imread('images/0.jpg')

segments_slic = slic(img, n_segments=250, compactness=15, sigma=1, start_label=1, slic_zero = True)
print(f'SLIC number of segments: {len(np.unique(segments_slic))}')
fig, ax = plt.subplots()
ax.imshow(mark_boundaries(img, segments_slic, color=(1., 1., 1.)))
plt.show()