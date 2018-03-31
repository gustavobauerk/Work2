
import cv2
import time
import numpy as np


def mean_filter_ing(img, tam_janela):
    img_mean_ing = img.copy()
    w = int(tam_janela/2)
    rows, cols, channels = img.shape
    for c in range(channels):
        for y in range(w, rows-w):
            for x in range(w, cols-w):
                soma = 0
                for y2 in range(y-w, y+w+1):
                    for x2 in range(x-w, x+w+1):
                        soma += img[y2][x2][c]
                img_mean_ing[y, x, c] = soma / (tam_janela * tam_janela)

    return img_mean_ing


def mean_filter_sep(img, tam_janela):
    img_linha = img.copy()
    img_mean_sep = img.copy()
    w = int(tam_janela/2)
    rows, cols, channels = img.shape
    for c in range(channels):
        for y in range(w, rows-w):
            for x in range(w, cols-w):
                soma = 0
                for x2 in range(x-w, x+w+1):
                    soma += img[y][x2][c]
                img_linha[y][x][c] = soma/tam_janela

    for c in range(channels):
        for y in range(w, rows-w):
            for x in range(w, cols-w):
                soma = 0
                for y2 in range(y-w, y+w+1):
                    soma += img_linha[y2][x][c]
                img_mean_sep[y][x][c] = soma/tam_janela

    return img_mean_sep


def mean_filter_int(img, tam_janela):
    img_aux = img.copy()
    img_mean_int = img.copy()
    w = int(tam_janela / 2)
    rows, cols, channels = img.shape
    for c in range(channels):
        for y in range(0, rows):
            for x in range(0, cols):
                img_aux[y][x][c] = img[y][x][c]
                if y != 0:
                    img_aux[y][x][c] += img_aux[y-1][x][c]

    for c in range(channels):
        for y in range(0, rows):
            for x in range(0, cols):
                if x != 0:
                    img_aux[y][x][c] += img_aux[y][x-1][c]

    for c in range(channels):
        for y in range(w, rows-w):
            for x in range(w, cols-w):
                img_mean_int[y][x][c] = img_aux[y+w][x + w][c]
                if y != w:
                    img_mean_int[y][x][c] -= img_aux[y-w-1][x+w][c]
                if x != w:
                    img_mean_int[y][x][c] -= img_aux[y+w][x-w-1][c]
                if y != w and x != w:
                    img_mean_int[y][x][c] += img_aux[y-w-1][x-w-1][c]
                img_mean_int[y][x][c] /= tam_janela*tam_janela

    return img_mean_int


def main():
    tam_janela = 15
    imagem = cv2.imread('b01 - Original.bmp')
    imagem = imagem.astype(np.float)/255

    # start_time = time.time()
    # imagem_media_ing = mean_filter_ing(imagem, tam_janela)
    # imagem_media_ing = (imagem_media_ing * 255).astype(np.uint8)
    #
    # elapsed_time = time.time() - start_time
    # print("Alg ingenuo ( janela", tam_janela, ")=", elapsed_time)

    start_time = time.time()
    imagem_media_sep = mean_filter_sep(imagem, tam_janela)
    imagem_media_sep = (imagem_media_sep * 255).astype(np.uint8)

    elapsed_time = time.time() - start_time

    print("Alg separavel ( janela", tam_janela, ")=", elapsed_time)

    start_time = time.time()
    imagem_media_int = mean_filter_int(imagem, tam_janela)
    imagem_media_int = (imagem_media_int * 255).astype(np.uint8)
    elapsed_time = time.time() - start_time

    print("Alg integral ( janela", tam_janela, ")=", elapsed_time)

    # cv2.imshow('algoritimo ingenuo', imagem_media_ing)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    cv2.imshow('algoritimo separavel', imagem_media_sep)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('algoritimo integral', imagem_media_int)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # cv2.imwrite('ingenuo.bmp', imagem_media_ing)
    cv2.imwrite('separavel.bmp', imagem_media_sep)
    cv2.imwrite('integral.bmp', imagem_media_int)

if __name__ == "__main__":
    main()
