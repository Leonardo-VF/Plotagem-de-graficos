import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x, y, z = [], [], []
with (open("fortran/Projeto_2/tarefa-3-saida-6.out")) as arq:
    while True:
        try:
            line = arq.readline().split()
            print(line)
            x.append(float(line[1]))
            y.append(float(line[2]))
        except:
            break

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

hist, xedges, yedges = np.histogram2d(x, y, bins = 70)
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")

xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

dx = dy = 30
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

colors = dz / dz.max()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True, color=plt.cm.viridis(colors))


# Configurar rótulos do eixo
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Frequência')

# Mostrar o gráfico
plt.show()