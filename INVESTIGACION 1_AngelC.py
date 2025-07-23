import matplotlib.pyplot as plt
x1 = [1, 1]
y1 = [0, 5]
x2 = [1, 2.5, 2.5, 1]
y2 = [5, 5, 3.5, 3.5]
x3 = [1, 2.5]
y3 = [3.5, 0]
plt.plot(x1, y1, color='red', linewidth=3)
plt.plot(x2, y2, color='red', linewidth=3)
plt.plot(x3, y3, color='red', linewidth=3)
plt.title("Inicial de mi nombre: Rafael")
plt.axis('equal')
plt.axis('off')
plt.show()
