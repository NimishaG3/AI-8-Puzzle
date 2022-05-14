import matplotlib.pyplot as plt

nodes_expanded1 = [0, 5, 21, 315, 1891, 12609, 49183, 137406]
nodes_expanded2 = [0, 2, 4, 12, 36, 153, 306, 2664]
nodes_expanded3 = [0, 2, 4, 18, 119, 609, 2664, 16294]

soln_depth = [0, 2, 4, 8, 12, 16, 20, 24]

plt.plot(soln_depth,nodes_expanded1, color = 'r', label = "Uniform Cost Search")
plt.plot(soln_depth,nodes_expanded2, color = 'g', label = "Manhattan Distance")
plt.plot(soln_depth,nodes_expanded3, color = 'b', label = "Misplaced Tile")
plt.title('Nodes Expanded vs. Soln Depth', fontsize = 20)
plt.xlabel('Nodes_expanded')
plt.ylabel('Solution Depth')
plt.legend()
plt.grid()
plt.show()
import matplotlib.pyplot as plt

time1 = [0.00031899999999999984, 0.0014330000000000037, 0.0024249999999999966, 0.04720699999999999, 0.618214, 24.556338, 498.814311, 3193.274857]
time2 = [0.00033099999999999796, 0.0010630000000000014, 0.0016320000000000015, 0.004623999999999996, 0.009269, 0.010894999999999998, 0.029700999999999998, 1.261402]
time3 = [0.00034, 0.0010630000000000014, 0.0013120000000000007, 0.0023979999999999974, 0.021530999999999995, 0.119738, 1.261402, 81.64394300000001]

soln_depth = [0, 2, 4, 8, 12, 16, 20, 24]

plt.plot(soln_depth,time1, color = 'r', label = "Uniform Cost Search")
plt.plot(soln_depth,time2, color = 'g', label = "Manhattan Distance")
plt.plot(soln_depth,time3, color = 'b', label = "Misplaced Tile")
plt.title('Time Taken vs. Soln Depth', fontsize = 20)
plt.xlabel('Time Taken')
plt.ylabel('Solution Depth')
plt.legend()
plt.grid()
plt.show()