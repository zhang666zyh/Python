# -*- encoding:UTF-8 -*-

'''
@File     :   Test03.py
@Time     :   2021/9/18 11:48
@Author   :   张宇航
@Contact  :   zhangzyh666@163.com
@MyWeb    :   https://zhang666zyh.github.io
'''

class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;

    def distance(self,point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2) ** 0.5


def main():
    point1, point2 = Point(3, 4, 5), Point(7, 8, 9)

    point = Point(0,0,0)

    point_Distance = point.distance(point1, point2)
    print(point_Distance)


if __name__ == '__main__':
    main()
