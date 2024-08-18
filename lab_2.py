# import numpy as np
import cv2

# Load images
img_color = cv2.imread('logo.png', cv2.IMREAD_COLOR)
img_gray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

# Check if the images are loaded successfully
if img_color is None:
    print("Error: Could not load color image 'tomato.png'")
if img_gray is None:
    print("Error: Could not load grayscale image 'abc.jpg'")

# Display images
if img_color is not None:
    cv2.imshow('Color Image', img_color)
if img_gray is not None:
    cv2.imshow('Grayscale Image', img_gray)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print shape and first channel of the color image
if img_color is not None:
    print(img_color.shape)
    print(img_color[:, :, 0])
