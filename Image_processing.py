import cv2
import numpy as np
import matplotlib.pyplot as plt

try:
    #busca a imagem do endereço e armazena como matriz
    a_imagem_grande = cv2.imread('C:/Users/psillosx/OneDrive - Intel Corporation/Desktop/ImageWorks/a_imagem.jpg')
    
    #corta a imagem para 360x360:
    a_imagem_ideal = a_imagem_grande[160:520,400:760]

    #conta as ocorrencias das cores da imagem e ordena por cor, de 0 a 255
    #numero de ocorrencias de uma cor: (ex. 123)
    #n = 194
    #print('Valor da cor',n,':',contagem_de_cores[n][1])
    
    x = list()
    for linha in a_imagem_ideal:
        for pixel in linha:
            x.append(pixel[0])
    plt.hist(x, bins=255)
    plt.show()

except:
    print('Nao foi possivel encontrar a imagem')