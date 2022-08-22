import matplotlib.pyplot as plt

x = [3 , 5, 2, 1, 2]
y = [2 , 3, 4, 5, 6]

titulo = "Grafico de Dispersao ou Pontos"

plt.title(titulo)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.scatter(x,y, label = "Pontos", color = "y", marker="^", s=200)
plt.plot(x,y , color="g", linestyle = "--")
plt.legend()
plt.show()

#plt.savefig("Nome da Figura salva em png")Salvando grafico


"""color: cor (ver exemplos abaixo)

label: rótulo

linestyle: estilo de linha (ver exemplos abaixo)

linewidth: largura da linha

marker: marcador (ver exemplos abaixo)



CORES (color)
'b' blue

'g' green

'r' red

'c' cyan

'm' magenta

'y' yellow

'k' black

'w' white



Marcadores (marker)
'.' point marker

',' pixel marker

'o' circle marker

'v' triangle_down marker

'^' triangle_up marker

'<' triangle_left marker

'>' triangle_right marker

'1' tri_down marker

'2' tri_up marker

'3' tri_left marker

'4' tri_right marker

's' square marker

'p' pentagon marker

'*' star marker

'h' hexagon1 marker

'H' hexagon2 marker

'+' plus marker

'x' x marker

'D' diamond marker

'd' thin_diamond marker

'|' vline marker

'_' hline marker





Tipos de linha (linestyle)
'-' solid line style

'--' dashed line style

'-.' dash-dot line style

':' dotted line style"""




