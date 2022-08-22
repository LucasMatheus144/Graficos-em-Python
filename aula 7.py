import matplotlib.pyplot as plt
import random 

vetor = []

for i in range(1000):
    randomm = random.randint(0,100)
    vetor.append(randomm)
    
plt.boxplot(vetor)
plt.title("BoxPlot")
plt.show()