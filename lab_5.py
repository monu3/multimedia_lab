import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Define coordinates for the M shape
x = [-2, -1, 0, 1, 2]
y = [-2, 2, 0, 2, -2]
ax.plot(x, y, color='blue', linewidth=20, solid_capstyle='round')

# Load and place icons on the M
icon_size = 0.5  # Size of the icons

# Coordinates for placing icons on the M
icon_positions = [
    (-1.5, 1.5),  # Top left
    (0, 0),       # Middle
    (1.5, 1.5),   # Top right
    (-1.5, -1.5), # Bottom left
    (1.5, -1.5)   # Bottom right
]

# Paths to the icons
icons = [
    "/Users/monusiddiki/Downloads/camara.png",
    "/Users/monusiddiki/Downloads/audio.png",
    "/Users/monusiddiki/Downloads/music.png",
    "/Users/monusiddiki/Downloads/video.png",
    "/Users/monusiddiki/Downloads/microphone.png"
]

# Plot each icon at the specified position
for (x_pos, y_pos), icon_path in zip(icon_positions, icons):
    try:
        img = Image.open(icon_path)
        img = img.resize((int(icon_size * 100), int(icon_size * 100)))
        ax.imshow(img, extent=[x_pos-icon_size/2, x_pos+icon_size/2, y_pos-icon_size/2, y_pos+icon_size/2])
    except FileNotFoundError:
        print(f"Icon {icon_path} not found. Make sure the path is correct.")

# Customize the plot
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')  # Hide the axes

# Show the logo
plt.show()