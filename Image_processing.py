import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def abrir_arquivo():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

try:
    #abre arquivo e retorna seu endereço
    file_path = abrir_arquivo()

    #busca a imagem do endereço e armazena como matriz
    a_imagem_original = cv2.imread(file_path)

    #corta a imagem para 360x360:
    a_imagem_cortada = a_imagem_original[160:520,400:760]

    #converte a matriz multidimensional de volta para imagem e exibe
    cv2.imshow('Imagem cortada', a_imagem_cortada)
    
    #a imagem é uma matriz de 3 dimensoes, aqui pegamos a cor de cada pixel e colocamos numa lista
    cores_dos_pixels = list()
    for linha in a_imagem_cortada:
        for pixel in linha:
            cor = pixel[0] #cada pixel tem 3 ints (rgb), aqui só queremos 1
            cores_dos_pixels.append(cor)

    print('\nEssa imagem tem:',len(cores_dos_pixels),'pixels')

    espectro_de_cores = 255
    plt.hist(cores_dos_pixels, bins=espectro_de_cores)
    plt.show()

except:
    print('Nao foi possivel encontrar a imagem')