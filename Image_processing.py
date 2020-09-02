import cv2
import matplotlib

try:
    #busca a imagem do endereço e armazena como matriz
    a_imagem_grande = cv2.imread('C:/Users/psillosx/OneDrive - Intel Corporation/Desktop/a_imagem.jpg')
    
    #corta a imagem para 360x360:
    a_imagem_ideal = a_imagem_grande[160:520,400:760]

    #dimensoes da imagem
    print('Numero de linhas da imagem: '+str(a_imagem_ideal.shape[0]))
    print('Numero de colunas da imagem: '+str(a_imagem_ideal.shape[1]))
    print('Espectros de cores por pixel: '+str(a_imagem_ideal.shape[2]))
    
except:
    print('Nao foi possivel encontrar a imagem')