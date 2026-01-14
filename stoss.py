import matplotlib.pyplot as plt

xnums = [5,6,7]
ynums = [2,2,2]

def plot(xnum, ynum):
    pointsold = []
    for x in range(0, xnum):
        pointsold.append([x, 0])
        pointsold.append([x, ynum-1])

    for y in range(0, ynum):
        pointsold.append([0, y])
        pointsold.append([xnum-1,y])

    points = []
    for point in pointsold:
        if point not in points:
            points.append(point)

    plt.scatter(*zip(*points))
    for point1 in points:
        for point2 in points:
            if point1[0] != point2[0] and point1[1] != point2[1]:
                x = [point1[0], point2[0]]
                y = [point1[1], point2[1]]
                plt.plot(x, y)

for i in range(len(xnums)):
    print(i)
    plt.subplot(len(xnums),1,i+1)
    plot(xnums[i], ynums[i])

plt.show()
