import matplotlib.pyplot as plt

time1 = [0.00031899999999999984, 0.0014330000000000037, 0.0024249999999999966, 0.04720699999999999, 0.618214, 24.556338, 498.814311, 3193.274857]
time2 = [0.00033099999999999796, 0.0010630000000000014, 0.0016320000000000015, 0.004623999999999996, 0.009269, 0.010894999999999998, 0.029700999999999998, 73]
time3 = [0.00034, 0.0010630000000000014, 0.0013120000000000007, 0.0023979999999999974, 0.021530999999999995, 0.119738, 1.261402, 81.64394300000001]

soln_depth = [0, 2, 4, 8, 12, 16, 20, 24]

plt.plot(time1,soln_depth, color = 'r', label = "Uniform Cost Search")
plt.plot(time2,soln_depth, color = 'g', label = "Manhattan Distance")
plt.plot(time3,soln_depth, color = 'b', label = "Misplaced Tile")
plt.title('Time Taken vs. Soln Depth', fontsize = 20)
plt.xlabel('Time Taken')
plt.ylabel('Solution Depth')
plt.legend()
plt.grid()
plt.show()