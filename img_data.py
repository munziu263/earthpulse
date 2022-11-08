from PIL import Image
import matplotlib.pyplot as plt
import rasterio
from rasterio.io import DatasetReader
from rasterio import plot
import numpy as np

path = "S2L2A_2022-06-09.tiff"

NORM = lambda data: (data * (255 / np.max(data))).astype(np.uint8)
MAX_SIZE = (100, 100)

dataset: DatasetReader = rasterio.open(path)

rgb = NORM(dataset.read([4, 3, 2]))  # Get and normalise the RGB data
rgb = np.moveaxis(rgb, 0, -1)
red = dataset.read(4).astype("float64")
nir = dataset.read(8).astype("float64")  # Must be floats to allow for division
ndvi = np.where((nir + red) == 0.0, 0, (nir - red) / (nir + red))

# Save the images to file
plt.imsave("ndvi.png", ndvi, format="png")
plt.imsave(
    "rgb.png",
    rgb,
    format="png",
)
img = Image.open("rgb.png", "r")
thumbnail = img.thumbnail(MAX_SIZE)
img.save("thumbnail.png", format="png")

# Because this is at the bottom, images are created when we run main.
attributes = {
    "width": dataset.width,
    "height": dataset.height,
    "band_count": dataset.count,
    "crs": dataset.crs.data["init"],
    "box": dataset.bounds,
}
