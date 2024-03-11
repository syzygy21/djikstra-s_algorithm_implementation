import cv2
import numpy as np
import matplotlib.pyplot as plt

# x1_hexagon, y1_hexagon = 800 , 250
# x2_hexagon, y2_hexagon = 725 , 379
# x3_hexagon, y3_hexagon = 575 , 379
# x4_hexagon, y4_hexagon = 500 , 250
# x5_hexagon, y5_hexagon = 574 , 120
# x6_hexagon, y6_hexagon = 725 , 120

pts_hexagon = draw_hexagon(155 , (650 , 250))


# Coordinates of the first polygon
x1_polygon1, x2_polygon1, y1_polygon1, y2_polygon1 = 94 , 179 , 94 , 499

# Coordinates of the second polygon
x1_polygon2, x2_polygon2, y1_polygon2, y2_polygon2 = 269 , 354 , 0 , 404

x1_polygon3, x2_polygon3, y1_polygon3, y2_polygon3 = 894 , 1104 , 44 , 129

x1_polygon4, x2_polygon4, y1_polygon4 , y2_polygon4 = 1014 , 1104 , 119 , 379

x1_polygon5, x2_polygon5, y1_polygon5 , y2_polygon5 = 894 , 1104 , 369 , 454


# x1_line1, x2_line1, y1_line1, y2_line1 = 0, 5, 0, 500

# x1_line2, x2_line2, y1_line2, y2_line2 = 0, 1200, 0, 5

# x1_line3, x2_line3, y1_line3, y2_line3 = 1195 , 1200 , 0 , 500

# x1_line4, x2_line4, y1_line4, y2_line4 = 0 , 1200 , 490 , 500


# pts_line1 = np.array([[x1_line1, y1_line1], [x2_line1, y1_line1], [x2_line1, y2_line1], [x1_line1, y2_line1]], np.int32)
# pts_line1 = pts_line1.reshape((-1, 1, 2))

# pts_line2 = np.array([[x1_line2, y1_line2], [x2_line2, y1_line2], [x2_line2, y2_line2], [x1_line2, y2_line2]], np.int32)
# pts_line2 = pts_line2.reshape((-1, 1, 2))

# pts_line3 = np.array([[x1_line3, y1_line3], [x2_line3, y1_line3], [x2_line3, y2_line3], [x1_line3, y2_line3]], np.int32)
# pts_line3 = pts_line3.reshape((-1, 1, 2))

# pts_line4 = np.array([[x1_line4, y1_line4], [x2_line4, y1_line4], [x2_line4, y2_line4], [x1_line4, y2_line4]], np.int32)
# pts_line4 = pts_line4.reshape((-1, 1, 2))


pts_polygon3 = np.array([[x1_polygon3, y1_polygon3], [x2_polygon3, y1_polygon3], [x2_polygon3, y2_polygon3], [x1_polygon3, y2_polygon3]], np.int32)
pts_polygon3 = pts_polygon3.reshape((-1, 1, 2))

pts_polygon4 = np.array([[x1_polygon4, y1_polygon4], [x2_polygon4, y1_polygon4], [x2_polygon4, y2_polygon4], [x1_polygon4, y2_polygon4]], np.int32)
pts_polygon4 = pts_polygon4.reshape((-1, 1, 2))

pts_polygon5 = np.array([[x1_polygon5, y1_polygon5], [x2_polygon5, y1_polygon5], [x2_polygon5, y2_polygon5], [x1_polygon5, y2_polygon5]], np.int32)
pts_polygon5 = pts_polygon5.reshape((-1, 1, 2))
# Create a blank image with size 1190x490
img_check = np.zeros((500, 1200 , 3), dtype=np.uint8)

# Define the vertices of the first polygon
pts_polygon1 = np.array([[x1_polygon1, y1_polygon1], [x2_polygon1, y1_polygon1], [x2_polygon1, y2_polygon1], [x1_polygon1, y2_polygon1]], np.int32)
pts_polygon1 = pts_polygon1.reshape((-1, 1, 2))

# Define the vertices of the second polygon
pts_polygon2 = np.array([[x1_polygon2, y1_polygon2], [x2_polygon2, y1_polygon2], [x2_polygon2, y2_polygon2], [x1_polygon2, y2_polygon2]], np.int32)
pts_polygon2 = pts_polygon2.reshape((-1, 1, 2))


# pts_hexagon = np.array([[x1_hexagon, y1_hexagon], [x2_hexagon, y2_hexagon], [x3_hexagon, y3_hexagon],
#                         [x4_hexagon, y4_hexagon], [x5_hexagon, y5_hexagon], [x6_hexagon, y6_hexagon]], np.int32)
# pts_hexagon = pts_hexagon.reshape((-1, 1, 2))

# Fill the first polygon with white color
cv2.fillPoly(img_check, [pts_polygon1], (255 , 255 , 255))

# Fill the second polygon with white color
cv2.fillPoly(img_check, [pts_polygon2], (255 , 255 , 255))


cv2.fillPoly(img_check, [pts_polygon3], (255 , 255 , 255))

cv2.fillPoly(img_check, [pts_polygon4], (255 , 255 , 255))

cv2.fillPoly(img_check, [pts_polygon5], (255 , 255 , 255))

cv2.fillPoly(img_check, [pts_hexagon], (255 , 255 , 255))

# cv2.fillPoly(img, [pts_line1], 255)
# cv2.fillPoly(img, [pts_line2], 255)
# cv2.fillPoly(img, [pts_line3], 255)
# cv2.fillPoly(img, [pts_line4], 255)
# Plot the result using matplotlib
plt.figure(2)
plt.imshow(img_check, cmap='gray', origin='lower')
plt.title('image_check')
plt.show()
