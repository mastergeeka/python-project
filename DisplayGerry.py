import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps, ImageColor


usa = Image.open("USLabels.png")
grid = np.array(usa)
print(grid.ndim)
(y,x,z) = grid.shape
print(grid.dtype)
#plt.figure(figsize=((y/40),(x/40)))
#plt.imshow(grid) 
