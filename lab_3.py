import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate circle points
def circle_points(radius, num_points=100):
    theta = np.linspace(0, 2*np.pi, num_points)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return x, y

# Function to generate triangle points
def triangle_points(base, height, num_points=100):
    x = np.zeros(num_points)
    y = np.zeros(num_points)
    third = num_points // 3
    x[:third] = np.linspace(-base/2, base/2, third)
    y[:third] = -height / 2
    x[third:2*third] = np.linspace(base/2, 0, third)
    y[third:2*third] = np.linspace(-height/2, height, third)
    x[2*third:] = np.linspace(0, -base/2, num_points - 2*third)
    y[2*third:] = np.linspace(height, -height/2, num_points - 2*third)
    return x, y

# Function to generate rectangle points
def rectangle_points(width, height, num_points=100):
    num_points_side = num_points // 4
    x = np.concatenate([
        np.linspace(-width/2, width/2, num_points_side),
        np.full(num_points_side, width/2),
        np.linspace(width/2, -width/2, num_points_side),
        np.full(num_points_side, -width/2)
    ])
    y = np.concatenate([
        np.full(num_points_side, -height/2),
        np.linspace(-height/2, height/2, num_points_side),
        np.full(num_points_side, height/2),
        np.linspace(height/2, -height/2, num_points_side)
    ])
    return x, y

# Interpolation function
def interpolate_points(points1, points2, t):
    x1, y1 = points1
    x2, y2 = points2
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2
    return x, y

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

# Generate shape points
circle = circle_points(1, num_points=100)
triangle = triangle_points(2, 2, num_points=100)
rectangle = rectangle_points(2, 1, num_points=100)
line, = ax.plot([], [], 'b-')

# Update function for animation
def update(frame):
    if frame < 100:
        t = frame / 100.0
        x, y = interpolate_points(circle, triangle, t)
    elif frame < 200:
        t = (frame - 100) / 100.0
        x, y = interpolate_points(triangle, rectangle, t)
    else:
        t = (frame - 200) / 100.0
        x, y = interpolate_points(rectangle, circle, t)
    line.set_data(x, y)
    return line,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 300), blit=True, interval=50)
plt.show()
