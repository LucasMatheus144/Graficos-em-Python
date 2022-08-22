import matplotlib.pyplot as plt

x = [3 , 5, 2, 1, 2]
y = [2 , 3, 4, 5, 6]

titulo = "Grafico de Dispersao ou Pontos"

plt.title(titulo)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.scatter(x,y, label = "Pontos", color = "y")
plt.plot(x,y , color="g")
plt.legend()
plt.show()
