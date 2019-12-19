import matplotlib
import matplotlib.style as mplstyle
import matplotlib.pyplot as plot
import numpy as np
import math

mplstyle.use(['dark_background', 'ggplot', 'fast'])
A = 10
xs = np.arange(-30,30,0.2)
ys = A*np.sin(xs)/xs

fig, ax = plot.subplots()
ax.plot(xs, ys)

plot.show()

