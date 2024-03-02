# Script to calculate and plot VIs

"""
 - jupyter kernell dies when running this code.
 - Idea is to get the workflow to calculate VIs from arrays
"""

import rasterio
from rasterio.plot import show
import numpy as np
from matplotlib import pyplot as plt

# Read image
image_path = "planet_images/20240210_161110_08_247d_3B_AnalyticMS.tif"
nicoya_raster = rasterio.open(image_path)

blue, green, red, nir = nicoya_raster.read()

## EVI

"""
First, we need to create an empty array that has the same
shape as the arrays we already read from the image.

Then, we have to populate the empty array with the new
calculated values.
"""

evi = np.zeros(blue.shape)
evi = 2.5 * (nir-red) / (nir + 5 * red - 7.5 * blue + 1)
print(evi)

plt.figure()
plt.hist(evi.flatten())
plt.savefig('hist_evi.png', bbox_inches = 'tight')
ds = None 

## Now, let's plot the new image and save it!
plt.imshow(evi)
plt.savefig('export_evi.png', bbox_inches = 'tight')


## NDVI
ndvi = np.zeros(blue.shape)
ndvi = (nir - red) / (nir + red)

plt.imshow(ndvi)
plt.savefig('export_ndvi.png', bbox_inches = 'tight')


