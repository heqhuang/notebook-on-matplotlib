####
# This script is an example of using HSV & HSL color systems from colorsys library.
####
import numpy as np
import matplotlib.pyplot as plt
import colorsys

## Part 1: HSL and HSV data arrays to plot

M, N = 400, 400  # array dimensions
# coordinates on image, shape: (M, N)
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, M)
X, Y = np.meshgrid(x, y)
Radius = np.sqrt(X**2+Y**2)
Angle = np.arctan2(Y, X).transpose()[::-1,:]%(2*np.pi)

# hsl & hsv data, value range: (0, 1)
hue = Angle/(2*np.pi)
saturation_hsv = Radius
saturation_hsl = X * 0 + 1
lightness = Radius
value = X * 0 + 1

# a circle aperture to plots
# data plotted in RGBA format
Aperture = np.heaviside(1-Radius, 1)

## Part 2: HSL/HSV to RGB conversion
rgb_from_hsv = np.ones([M, N, 4])  #initialize data array
rgb_from_hsv[:,:,3] = Aperture
rgb_from_hls = np.ones([M, N, 4])
rgb_from_hls[:,:,3] = Aperture

for i in range(M):  # use iteration instead of broadcast to convert HSL/HSV to RGB
    for j in range(N):
        h = hue[i, j]
        s_hsv= saturation_hsv[i, j]
        s_hsl = saturation_hsl[i, j]
        l = lightness[i, j]
        v = value[i, j]
        rgb_from_hsv[i,j,0:3] = colorsys.hsv_to_rgb(h,s_hsv,v)
        rgb_from_hls[i,j,0:3] = colorsys.hls_to_rgb(h,l,s_hsl)  # NOTE: the order of parameters is HLS, not HSL

## Part 3: plots
plt.imshow(rgb_from_hsv)
plt.axis('off')
plt.show()

plt.imshow(rgb_from_hls)
plt.axis('off')
plt.show()

####