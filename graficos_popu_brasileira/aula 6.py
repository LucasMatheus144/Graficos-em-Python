import matplotlib.pyplot as plt

dados = open("D:\VsCode\python\Graficos em Python\populacao_brasileira.csv").readlines()

x = []
y = []

for j in range(len(dados)):
    if j != 0:
        linhas = dados[j].split(";")
        x.append(int(linhas[0]))
        y.append(int(linhas[1]))
    
    
plt.title("Crescimento Populacional de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("Populaçao")   
plt.plot(x,y,color="r") 
plt.bar(x,y ,color = "gray")
plt.show()

        

    