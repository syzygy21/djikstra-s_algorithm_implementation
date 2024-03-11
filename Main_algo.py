import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import heapq
from IPython.display import clear_output
from google.colab.patches import cv2_imshow




def algorithm(start , goal) :
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('assets/test.mp4', fourcc, 10, (1200, 500))
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
        #add check for goal state
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
