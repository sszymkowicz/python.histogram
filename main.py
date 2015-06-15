__author__ = 'Slawek'
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math

file_name = "anime.jpg"
f = Image.open(file_name)


def histogram():
    pixels = list(f.getdata())
    hist = [0] * 768

    for p in pixels:
        hist[p[0]] += 1
        hist[256+p[1]] += 1
        hist[512+p[2]] += 1

    ax = plt.subplot(111)
    ax.bar(range(len(hist)), hist)
    plt.show()


def edges():
    out_img = Image.new("L", f.size, None)
    img_data = f.load()
    out_data = out_img.load()

    matrix_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    matrix_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    matrix_size = 3
    #matrix_x = [[1, 0], [0, -1]]
    #matrix_y = [[0, 1], [-1, 0]]
    #matrix_size = 2
    matrix_middle = matrix_size/2

    rows, cols = f.size

    for row in range(rows - matrix_size):
        for col in range(cols - matrix_size):
            pixel_x = 0
            pixel_y = 0
            for i in range(matrix_size):
                for j in range(matrix_size):
                    val = sum(img_data[row+i, col+j])/3
                    pixel_x += matrix_x[i][j] * val
                    pixel_y += matrix_y[i][j] * val

            new_pixel = math.sqrt(pixel_x**2 + pixel_y**2)
            new_pixel = int(new_pixel)
            out_data[row + matrix_middle, col + matrix_middle] = new_pixel
    out_img.show()


def main():
    histogram()
    edges()

if __name__ == "__main__":
    sys.exit(main())