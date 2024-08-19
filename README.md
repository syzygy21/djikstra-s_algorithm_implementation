## Dijkstra's algorithm implementation for a path planning problem
The code uploaded implements the Dijkstra's algorithm on a workspace of size 1200 * 500 mm which consists of obstacles. The code returns the shortest path from a specific start to a goal location which is collision free. 
A padding of 5 mm is given around each obstacle while planning because the assumption is that the robot in the workspace is of 5 mm radius. This is visible in the following GIF which visualizes the exploration of the workspace
and also shows the path found. 

The 5 mm padding is also set at the boundary of the workspace which decreases the effective area to 1194 * 494. The user can input a specific start and goal location for path finding and there are also checks added to the code
that specify to the user if the locations entered are appropriate or not by checking if the lie outside of workspace or if they lie in an obstacle.

<img src="https://github.com/user-attachments/assets/e68c528b-ecc5-434c-b529-4670d457d9c1" width="500" alt="test">

