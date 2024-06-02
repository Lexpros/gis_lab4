import matplotlib.pyplot as plt
from figures import SIZE, BLUE, GRAY, RED
from shapely.plotting import plot_polygon, plot_line, plot_points
from shapely import Polygon, MultiPolygon
import shapely
import numpy as np

fig = plt.figure(1, figsize=SIZE, dpi=90)

ax = plt.gca()
crds1 = [(61, 33), (135, 29), (119, 25), (199, 13), (206, 20), (274, 21), (294, 27),
         (221, 33), (239, 42), (127, 45), (107, 41), (107, 38)]
crds2 = [(99, 81), (155, 70), (170, 91), (150, 107), (157, 114), (124, 133), (78, 110)]

crds3 = [(298, 81), (310, 74), (319, 74), (391, 86),  (430, 135), (410, 158), (398, 158), (381, 133), (387, 108), (349, 99), (326, 114), (323, 133), (306, 135), (306, 110)]
crds4 = [(504, 165), (507, 186), (540, 189), (550, 208), (514, 226), (524, 255),(521, 258), (497, 259), (470, 266), (461, 253), (459, 243), (438, 229), (480, 216), (469, 199), (482, 180)]
crds_for_anal = [(155, 169), (205, 156), (300, 193), (281, 209), (191, 206), (152, 174)]

crds = [crds1, crds2, crds3, crds4, crds_for_anal]
print(len(crds))
for i in range(len(crds)):
    for j in range(len(crds[i])):
        crds[i][j] = list(crds[i][j])
        crds[i][j][1] = (271 - crds[i][j][1])
        crds[i][j] = tuple(crds[i][j])
crds1 = crds[0]
crds2 = crds[1]
crds3 = crds[2]
crds4 = crds[3]
crds_for_anal = crds[4]

poly_1 = Polygon(crds1)
poly_2 = Polygon(crds2)
poly_3 = Polygon(crds3)
poly_4 = Polygon(crds4)
poly_for_anal = Polygon(crds_for_anal)

ob = MultiPolygon([
        poly_1, poly_2, poly_3, poly_4, poly_for_anal
])
plot_polygon(ob, add_points=False)
# ax.get_yaxis().set_visible(False)
# ax.get_xaxis().set_visible(False)
# plt.grid(color='r', linestyle='-', linewidth=2)
plt.show()
