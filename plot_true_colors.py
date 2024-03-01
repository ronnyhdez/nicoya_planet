import rasterio
from rasterio.plot import show
import numpy as np
import matplotlib.pyplot as plt

# Open the file
image_path = "planet_images/20240210_161110_08_247d_3B_AnalyticMS.tif"
nicoya_raster = rasterio.open(image_path)

# Read the data
data = nicoya_raster.read()

# Normalize values
def scale_min_max(x):
    """Apply a min-max normalization"""
    return((x - np.nanmin(x)) / (np.nanmax(x) - np.nanmin(x)))

red = scale_min_max(data[2])
blue = scale_min_max(data[0])
green = scale_min_max(data[1])

rgb = np.dstack((red, green, blue))
#plt.figure()
plt.imshow(rgb)
#plt.show()

plt.savefig('export3_rgb.png', bbox_inches='tight')
