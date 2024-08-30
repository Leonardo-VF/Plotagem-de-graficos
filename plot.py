import matplotlib.pyplot as plt

x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []

with (open("fortran/Projeto_4/tarefa-4-saida-1.out")) as arq:
    while True:
        try:
            line = arq.readline().split()
            print(line)
            x.append(float(line[0]))
            y.append(float(line[1]))
        except:
            break


with (open("fortran/Projeto_4/tarefa-4-saida-1.out")) as arq:
    while True:
        try:
            line = arq.readline().split()
            print(line)
            v1.append(float(line[0]))
            d1.append(float(line[1]))
        except:
            break

with (open("fortran/Projeto_4/tarefa-4-saida-1.out")) as arq:
    while True:
        try:
            line = arq.readline().split()
            print(line)
            v2.append(float(line[0]))
            d2.append(float(line[1]))
        except:
            break



#plt.hist(x, 150)
plt.plot(x, y, '-', label = "Teta")
plt.plot(x1, y1, '-', label = "Omega")
plt.plot(x2, y2, '-', label = "Energia")
plt.xlabel('')
plt.ylabel('')
plt.legend(["Teta","Omega", "Energia"], 
           bbox_to_anchor = (1.05, 0.6))
plt.grid(True)
plt.show()
