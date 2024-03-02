# %%

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import numpy as np
import matplotlib.pyplot as plt

image_path = "planet_images/20240210_161110_08_247d_3B_AnalyticMS.tif"
nicoya_raster = rasterio.open(image_path)

def scale(band):
    return band / 10000

blue, green, red, nir = nicoya_raster.read()

blue_scaled = scale(blue)
green_scaled = scale(green)
red_scaled = scale(red)

rgb = np.dstack((red, green, blue))

rgb

plt.imshow(rgb)

plt.savefig('export_rgb.png', bbox_inches='tight')

# %%
blue, green, red, nir = nicoya_raster.read()

data = np.dstack((red, green, blue))

norm = (data * (255 / np.max(data))).astype(np.uint8)
plt.imshow(norm)

# plt.savefig('export2_rgb.png', bbox_inches='tight')

min_val = data[0].min()
max_val = data[0].max()
print(min_val, max_val)

# %%
