from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open an image file
img = Image.open(r'deg_60\\image2.tiff')

# Convert the image to a NumPy array
img_array = np.array(img)

print(img_array.shape)  # Prints the dimensions of the image array