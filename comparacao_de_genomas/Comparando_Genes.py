import matplotlib.pyplot as plt

entrada = open("bacteria.fasta").readlines()
saida = open("D:\VsCode\python\Graficos em Python/bacteria.fasta","w")

cont = {}

for i in ['A','T','C','G']:
    for j in ['A','T','C','G']:
        cont[i][j] = 0

entrada = entrada.replace("\n","")

for l in range(len(entrada)):
    cont[entrada[l]+entrada[l+1]] += 1
    
print(cont)