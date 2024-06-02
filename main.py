import matplotlib.pyplot as plt
from figures import SIZE, BLUE, GRAY, RED
from shapely.geometry import LineString, Point, MultiPoint, MultiLineString
from shapely.plotting import plot_polygon, plot_line, plot_points
from shapely import Polygon, MultiPolygon, centroid, distance, area, difference, equals
import pandas as pd
import numpy as np
from prettytable import PrettyTable


# Метрика построенная на дистанции и площади
def metric_one(df):
    df_for_edit = df.copy()
    properties = {'Dif of nodes': [abs(df_for_edit.iloc[-1, 2] - df_for_edit.iloc[i, 2]) for i in range(len(df_for_edit))]}
    df_for_edit = df_for_edit.drop(['Nodes count'], axis=1)
    df_for_edit.insert(2, 'Dif of nodes',  pd.Series(properties['Dif of nodes']))
    sort_by = ['Dif of nodes', 'Distance']
    df_for_edit.drop(df.tail(1).index, inplace=True)    
    df_for_edit = df_for_edit.sort_values(by=sort_by)
    trust = len(df_for_edit)
    for i in range(len(df_for_edit)):
        df_for_edit.iloc[i, -1] = trust
        trust -= 1
    mytable = PrettyTable()
    print(df_for_edit)
    return np.mean([df_for_edit.iloc[0, -2], df_for_edit.iloc[1, -2]])

    


def metic_two(xz_frame):
    sort_by = ['Distance', 'Square']
    new_df = xz_frame.copy()
    new_df.drop(df.tail(1).index, inplace=True)
    new_df.sort_values(by=sort_by)
    trust = len(new_df)
    for i in range(len(new_df)):
        new_df.iloc[i, -1] = trust
        trust -= 1
    print(new_df)
    return np.mean([new_df.iloc[0, -2], new_df.iloc[1, -2]])


fig = plt.figure(1, figsize=SIZE, dpi=90)

ax = plt.gca()
crds1 = [(61, 33), (135, 29), (119, 25), (199, 13), (206, 20), (274, 21), (294, 27),
         (221, 33), (239, 42), (127, 45), (107, 41), (107, 38)]
crds2 = [(99, 81), (155, 70), (170, 91), (150, 107), (157, 114), (124, 133), (78, 110)]

crds3 = [(298, 81), (310, 74), (319, 74), (391, 86), (430, 135), (410, 158), (398, 158), (381, 133), (387, 108),
         (349, 99), (326, 114), (323, 133), (306, 135), (306, 110)]
crds4 = [(504, 165), (507, 186), (540, 189), (550, 208), (514, 226), (524, 255), (521, 258), (497, 259), (470, 266),
         (461, 253), (459, 243), (438, 229), (480, 216), (469, 199), (482, 180)]
crds_for_anal = [(155, 169), (205, 156), (300, 193), (281, 209), (191, 206), (152, 174)]

crds = [crds1, crds2, crds3, crds4, crds_for_anal]
# Илюха крутой!!!!!
crds_of_cntrds = list()
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
centroid(poly_1)
poly_2 = Polygon(crds2)
poly_3 = Polygon(crds3)
poly_4 = Polygon(crds4)
poly_for_anal = Polygon(crds_for_anal)
# Лёх, привет. Ты крутой.

polygons = [poly_1, poly_2, poly_3, poly_4, poly_for_anal]
centroids = [centroid(i) for i in polygons]  # Центроиды полигонов

ob = MultiPolygon(polygons)
for i in range(len(polygons)):
    print(equals(poly_for_anal, polygons[i]))

plot_polygon(ob, add_points=False)
plot_polygon(poly_for_anal, add_points=False, color=RED)
plot_points(centroids, color=RED)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
plt.grid(color='r', linestyle='-', linewidth=2)
target_dist = [distance(centroids[-1], centroids[i]) for i in range(len(centroids))]
areas = [area(i) for i in polygons]
dif_areas = [abs(areas[-1] - areas[i]) for i in range(len(areas) - 1)]
min_dist = {np.where(target_dist == np.min(target_dist))[0][0] + 1: np.min(target_dist)}
best_square = {np.where(dif_areas == np.min(dif_areas))[0][0] + 1: np.min(dif_areas)}
# for i in range(len(target_dist)):
#         print(f'Target {i + 1} - distance: {target_dist[i]}, square: {areas[i]}')
# print(f'Область анализа: площадь {area(poly_for_anal)}')        
# print(f'Ближайшая по расстоянию - {min_dist}')
# print(f'Ближайшая по площади - {best_square}')  # I'm done

# Pandas Time!!!!
# 
cool_dict = {'Figure': [i + 1 for i in range(len(polygons))],
             'Square': [i for i in areas],
             'Nodes count': [len(list(polygons[i].exterior.coords)) for i in range(len(polygons))],
             'Distance': [i for i in target_dist],
             'Population': [250, 10000, 100000, 100, None],
             'Similarities': [0 for i in range(len(polygons))]}
df = pd.DataFrame(cool_dict)

print(metric_one(df))
print(metic_two(df))
plt.title('пофтафтье максямумь, позазуста! 😭')
plt.show()