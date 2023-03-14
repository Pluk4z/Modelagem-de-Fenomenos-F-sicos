""" 1. Um fotógrafo está posicionado em frente a uma plataforma de
lançamento de foguetes de forma que o eixo da lente da sua câmera está a
50 m de distância e perfeitamente alinhada com a base do foguete. Em que
ângulo ele deve colocar a câmera para tirar uma foto deste foguete quando
ele estiver há 200 m de altura. """

#(a)
import math

distancia_camera = 50
altura_foguete = 200

Angulo_U = math.atan(altura_foguete / distancia_camera)

print(f'A) O angulo em radianos é {Angulo_U}')

#(b)

def angulo_camera(y):
    distancia = math.atan(y / 50)
    return distancia


AltitudeQualquer = int(input('B) Coloque uma altitude qualquer em metros: '))
resposta = angulo_camera(AltitudeQualquer)
print(f'Você deve colocar a câmera em um ângulo de {resposta} rad')

#(c)

import matplotlib.pyplot as plt

x = [0, 0, 50]
y = [0, AltitudeQualquer, 0]

plt.plot(x, y)

plt.xlim(0, 100)
plt.ylim(0, AltitudeQualquer + 200)

plt.xlabel('Distância da Câmera (m)')
plt.ylabel('Altura do Foguete (m)')
plt.title('C) Triângulo resultante')

plt.show()


