####
# This script is an example of RGB plot using matplotlib.pyplot.imshow().
####
import numpy as np
import matplotlib.pyplot as plt

## Part 1: generate data arrays for plot

M, N = 300, 400  # array dimensions

# coordinates on image, shape: (M, N)
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, M)
X, Y = np.meshgrid(x, y)

# rgb arrays, shape: (M, N)
# value range: (0, 1)
red = 1 - X
green = Y
blue = X

# combine rgb arrays for plot
rgb = np.zeros([M, N, 3])
rgb[:,:,0] = red
rgb[:,:,1] = green
rgb[:,:,2] = blue
print(rgb.shape)  # array shape: (M, N, 3) for RGB plot

## Part 2: RGB plot
plt.imshow(rgb)
plt.show()

####