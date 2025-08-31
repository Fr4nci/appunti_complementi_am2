import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import numpy as np

colors = ["#6e6eab", "#dbdbea", "#f1a3f1"]  # viola scuro → viola medio → viola chiaro
violet_cmap = LinearSegmentedColormap.from_list("violet", colors)

# Grid per x e y
x = np.linspace(-15, 15, int(5000*1.5))
y = np.linspace(-15, 15, int(5000*1.5))
X, Y = np.meshgrid(x, y)

# Funzione sinc traslata: f(x,y) = sin(r)/r, con r = sqrt((x-1)^2 + y^2)
R = np.sqrt((X-1)**2 + Y**2)
Z = 100 * (np.sin(R) / R)
Z[R == 0] = 1  # definizione sinc(0) = 1

# Plot 3D
fig = plt.figure(figsize=(30, 45))
ax = fig.add_subplot(111, projection="3d")

# Superficie con colormap
surf = ax.plot_surface(X, Y, Z, cmap=violet_cmap, edgecolor="none", alpha=0.85)

# Rimuove la scatola 3D
ax.grid(False)
ax.xaxis.pane.set_visible(False)
ax.yaxis.pane.set_visible(False)
ax.zaxis.pane.set_visible(False)
ax.xaxis.line.set_visible(False)
ax.yaxis.line.set_visible(False)
ax.zaxis.line.set_visible(False)

# Labels (senza ticks)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Vista simile a quella di pgfplots
ax.view_init(elev=40, azim=40)

# Salva come PDF
output_path = "superficie.eps"
plt.savefig(output_path, format='eps', dpi=1200)
plt.close()
