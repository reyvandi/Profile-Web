import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

x2 = np.array([2, 2, 8, 1, 5, 8, 12, 9, 7, 3, 11, 4, 14, 12])
y2 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

plt.scatter(x1, y1, color='hotpink', label="Dataset 1")
plt.scatter(x2, y2, color='#88c999', label="Dataset 2")

plt.legend()
plt.show()