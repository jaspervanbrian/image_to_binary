from PIL import Image
import numpy as np
from math import ceil
import time

# Default size is 10
size = 10

# Open the image
img = Image.open('image.png')

# Convert the image to black and white using PIL
img = img.convert('1')

# Resize the image to default size
img = img.resize((size, size))

# Convert the image to a NumPy array
pixel_array = np.array(img)

# Flatten the array to a 1D array
pixel_array_1_0 = pixel_array.flatten()

# Convert the 1s and 0s to integers
pixel_array_1_0 = pixel_array_1_0.astype(int)

# Counting 10 and printing in a line
def text_img(n, pixel_array, inversed=False):
    for i in range(size):
        print("")
        for j in range(len(pixel_array[i])):
            if inversed:
                if pixel_array[i][j]:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            else:
                if pixel_array[i][j]:
                    print(" ", end=" ")
                else:
                    print("*", end=" ")

# Counting 10 and printing in a line
def img_in_1_0(n, pixel_array_1_0):
    for i in range(ceil(len(pixel_array_1_0) / n)):
        print(*pixel_array_1_0[i*n:(i+1)*n])

# Print the resulting pixel array
print("Text Representation of Image:")
text_img(size, pixel_array)

print("\n")
print("Inversed:")
text_img(size, pixel_array, inversed=True)

print("\n")
print("Image in Binary:")
img_in_1_0(size, pixel_array_1_0)

# Pause output to prevent the terminal from closing instantly
for pause_in_seconds in [120]:
    print()
time.sleep(pause_in_seconds)
