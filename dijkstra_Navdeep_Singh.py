#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
def draw_hexagon(side_length, centroid):
    angle = 60  
    angles_rad = np.radians([(60 * i + 90) for i in range(6)]) 
    x = centroid[0] + side_length * np.cos(angles_rad)
    y = centroid[1] + side_length * np.sin(angles_rad)
    points = np.array([[int(x[i]), int(y[i])] for i in range(6)], np.int32)
    points = points.reshape((-1, 1, 2))
    return points


# In[20]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
# x1_hexagon, y1_hexagon = 800 , 250
# x2_hexagon, y2_hexagon = 725 , 379
# x3_hexagon, y3_hexagon = 575 , 379
# x4_hexagon, y4_hexagon = 500 , 250
# x5_hexagon, y5_hexagon = 574 , 120
# x6_hexagon, y6_hexagon = 725 , 120

pts_hexagon = draw_hexagon(150 , (650 , 250))


# Coordinates of the first polygon
x1_polygon1, x2_polygon1, y1_polygon1, y2_polygon1 = 99 , 174 , 99 , 499

# Coordinates of the second polygon
x1_polygon2, x2_polygon2, y1_polygon2, y2_polygon2 = 274 , 349 , 0 , 399

x1_polygon3, x2_polygon3, y1_polygon3, y2_polygon3 = 899 , 1099 , 49 , 124

x1_polygon4, x2_polygon4, y1_polygon4 , y2_polygon4 = 1019 , 1099 , 124 , 374

x1_polygon5, x2_polygon5, y1_polygon5 , y2_polygon5 = 899 , 1099 , 374 , 449


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
img_ori = np.zeros((500, 1200 ,3), dtype=np.uint8)

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
cv2.fillPoly(img_ori, [pts_polygon1], (255 , 255 , 255))

# Fill the second polygon with white color
cv2.fillPoly(img_ori, [pts_polygon2], (255 , 255 , 255))


cv2.fillPoly(img_ori, [pts_polygon3], (255 , 255 , 255))

cv2.fillPoly(img_ori, [pts_polygon4], (255 , 255 , 255))

cv2.fillPoly(img_ori, [pts_polygon5], (255 , 255 , 255))

cv2.fillPoly(img_ori, [pts_hexagon], (255 , 255 , 255))

# cv2.fillPoly(img, [pts_line1], 255)
# cv2.fillPoly(img, [pts_line2], 255)
# cv2.fillPoly(img, [pts_line3], 255)
# cv2.fillPoly(img, [pts_line4], 255)
# Plot the result using matplotlib
plt.figure(1)
plt.imshow(img_ori, cmap='gray', origin='lower')
plt.title('image_ori')
plt.show()
# cv2_imshow(img_ori)


# sample_points = [(800 , 50)]

# # Check if the sampled points are in the white or black region
# for point in sample_points:
#     x, y = point
#     pixel_value = img[y, x]  # Note: img[y, x] is used due to NumPy array indexing

#     if x >= 0 and x <= 4 and y >= 0 and y <= 499 :
#         print(f"Point {point} is in the obstacle region.(here 1)")
#     elif x >= 0 and x <= 1199 and y >= 0 and y <= 4 :
#         print(f"Point {point} is in the obstacle region.(here 2)")
#     elif x >= 1194 and x <= 1199 and y>= 0 and y <= 499:
#         print(f"Point {point} is in the obstacle region.(here 3)")
#     elif x >= 0 and x <= 1199 and y >= 489 and y <= 499:
#         print(f"Point {point} is in the obstacle region.(here 4)")
#     elif pixel_value == 255:
#         print(f"Point {point} is in the obstacle region.(here 5)")
#     else:
#         print(f"Point {point} is in the free region.(here 6)")


# In[21]:


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


# In[22]:


def possible_moves(tup):
    x , y = tup
    return [(x, y + 1) , (x, y - 1) , (x + 1, y) , (x - 1, y) , (x + 1, y + 1) , (x - 1, y + 1) , (x + 1, y - 1) , (x - 1, y - 1)] , [1 , 1 , 1 , 1 , 1.4 , 1.4 , 1.4 , 1.4]

def is_move_legal(tup):
    x , y = tup
    pixel_value = img_check[y, x]
    pixel_value = tuple(pixel_value)
    if x >= 0 and x <= 4 and y >= 0 and y <= 499 :
        #print(f"Point {point} is in the obstacle region.(here 1)")
        return False
    elif x >= 0 and x <= 1199 and y >= 0 and y <= 4 :
        #print(f"Point {point} is in the obstacle region.(here 2)")
        return False
    elif x >= 1195 and x <= 1199 and y>= 0 and y <= 499:
        #print(f"Point {point} is in the obstacle region.(here 3)")
        return False
    elif x >= 0 and x <= 1199 and y >= 495 and y <= 499:
        #print(f"Point {point} is in the obstacle region.(here 4)")
        return False
    elif pixel_value == (255 , 255 , 255):
        #print(f"Point {point} is in the obstacle region.(here 5)")
        return False
    else:
        #print(f"Point {point} is in the free region.(here 6)")
        return True


# In[23]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import heapq






def algorithm(start , goal) :
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    ##Please change the path here
    out = cv2.VideoWriter('Downloads/test.mp4', fourcc, 10, (1200, 500))
    queue_open =  [(0 , start)]

    heapq.heapify(queue_open)

    visited = {}

    info_dict = {start : ((None , None) , 0)}
    # frame_list = []
    iter = 0
    # move_list = []
    reached = 0
    while queue_open :
        element = heapq.heappop(queue_open)
        c_2_c , node = element
        info = info_dict[node]
        parent , c_2_c_p = info
        visited[node] = parent
        if (node == goal) :
            path = [goal]
            while goal != start :
                parent = visited[goal]
                path.append(parent)
                goal = parent
            path.reverse()
            #print(path)
            for point in path:
                x , y = point
                cv2.circle(img_ori , (x , y) , 1 , (0 , 0 , 255) , -1)
            print('reached')
            img_ori_copy = img_ori.copy()
            flipped_vertical = cv2.flip(img_ori_copy, 0)
            reached = 1
            for i in range (100):
                out.write(flipped_vertical)
            break
        moves, cost = possible_moves(node)
        for move , c_value in zip(moves , cost) :
            Bool = is_move_legal(move)
            if (Bool == True and move not in visited):
                x , y = move
                cv2.circle(img_ori , (x , y) , 1 , (255 , 0 , 0) , -1)
                # move_list.append(move)
                if (iter % 10000) == 0 :
                    img_ori_copy = img_ori.copy()
                    flipped_vertical = cv2.flip(img_ori_copy, 0)
                    out.write(flipped_vertical)
                # cv2.circle(img_ori, (x, y), 1, (255 , 0 ,  0), -1)
                # frame_list.append(img_ori)
                # plt.imshow(img_ori, cmap='gray', origin='lower')
                # plt.title('image_ori')
                # plt.show()
                # plt.pause(0.1)
                # plt.clf()
                #x , y = move
                #print(x , y)
                #img_ori[y , x] = [255 , 0 , 0] #colour pixel blue
                # cv2_imshow(img_ori)
                # clear_output(True)
                #out.write(img_ori)
                #output_path = f"assets/image_{iteration}.jpg"
                #cv2.imwrite(output_path , img_ori)
                if move in info_dict :
                    info = info_dict[move]
                    parent , c_2_c_p = info
                    c_2_c_n = c_2_c + c_value
                    if (c_2_c_n < c_2_c_p):
                        info_dict[move] = (node , c_2_c_n)
                        queue_open = [(k, v) for k, v in queue_open if v != move]
                        heapq.heapify(queue_open)
                        heapq.heappush(queue_open , (c_2_c_n , move))
                elif move not in info_dict :
                    info_dict[move] = (node , c_2_c + 1)
                    heapq.heappush(queue_open , (c_2_c + 1 , move))
        iter += 1


    out.release()
    return visited, reached


start_x = int(input("Enter the start x position: "))
start_y = int(input("Enter the start y position: "))
goal_x = int(input("Enter the goal x position: "))
goal_y = int(input("Enter the goal y position: "))

start = (start_x , start_y)
goal = (goal_x , goal_y)
Bool1 = is_move_legal(start)
Bool2 = is_move_legal(goal)

if Bool1 == True and Bool2 == True :
    print('correct positions entered algo is executing')
    visited , reached = algorithm (start , goal)
    if reached == 1 :
        print('Path is available')
    else  :
        print('Did not reach')
else :
    print('please run the code cell again and enter valid start and goal positions')


# In[ ]:




