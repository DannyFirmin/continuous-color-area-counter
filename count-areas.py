import cv2 as im
import argparse
import sys
from collections.abc import Iterable
sys.setrecursionlimit(2000000000)

'''Algorithm Summary:
Using recursion to search all the pixel with same color to count continuous area.
Find the neighbor pixels and keep searching if any neighbor is in a different color. 
If it is different don’t do a recursive from that and store it as unchecked.
Then it finishes searching for one area and count adds 1. 
Finally, pick a different unchecked color and do the same thing again

To reduce complexity, search each pixel only once. This can be done by using a mask array with T/F
or I just simply change the searched pixel to 150 (which is not very good but just a quick way)

To improve:
- Recursion is not good for large image, it's a tree structure and grow exponentially
- Find a graphic traversal algorithm or iterative way (stack) instead of recursion
- Use argparse lib to let user run from command line with args'''
output = [0] * 256


def load_img(path):
    '''Loads the image into a nd-array.Given that the image is in
        the same root folder as the sourcecode. 
        @param:path - File name
        @return:imageArr - Image nd-array '''
    img_arr = im.imread(path, im.IMREAD_GRAYSCALE)
    return img_arr


def is_last_pixel_in_area(current_colour, row, col):
    positions_to_check = find_neighbor((row, col))
    for (x, y) in positions_to_check:
        try:
            if imgArr[x][y] != current_colour:  # means the neighbouring  cell is different
                continue
            else:
                return False
        except IndexError:
            continue
    return True


def check_completion():
    for r in range(len(imgArr)):
        for c in range(len(imgArr[0])):
            if imgArr[r][c] != 150:
                return False
    return True


def area_counter(unchecked_pixels, row, col):
    '''Counts the number of coloured areas in the image and updates the area counts 
       @param:imageArr - ndArray of the image
       If currentColour value of a cell  is 150, it means that it has been searched '''
    print("This is the Image array \n \n ", imgArr, "\n")
    current_colour = imgArr[row][col]
    while not check_completion():
        unchecked = filler(current_colour, 0, 0, [])
        global output
        output[current_colour] += 1
        if not isinstance(unchecked, Iterable):
            continue
        for uncheckObject in unchecked:
            if type(uncheckObject) == tuple:
                try:
                    row = uncheckObject[0]
                    col = uncheckObject[1]
                    if imgArr[row][col] == 150:
                        continue
                    current_colour = imgArr[row][col]
                    filler(current_colour, row, col, unchecked)
                    output[current_colour] += 1
                except ValueError:
                    continue




def filler(current_colour, row, col, unchecked):
    global imgArr
    if is_last_pixel_in_area(current_colour, row, col) and imgArr[row][col] == current_colour:
        imgArr[row][col] = 150
        return unchecked
    elif imgArr[row][col] != current_colour:
        if (row, col) not in unchecked and (row, col) is not None:
            unchecked.append((row, col))
    elif imgArr[row][col] == current_colour:
        imgArr[row][col] = 150
        for (x, y) in find_neighbor((row, col)):
            if x >= len(imgArr) or y >= len(imgArr[0]):
                continue
            unchecked.append(filler(current_colour, x, y, unchecked))
        return unchecked


def find_neighbor(current_position):
    neighbour_pixels = []
    x = current_position[0]
    y = current_position[1]
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0:
                continue
            position = (i, j)
            neighbour_pixels.append(position)
    neighbour_pixels.remove(current_position)
    return neighbour_pixels


def output_display():
    global output
    print("Number of White: ", output[255])
    print("Number of Black: ", output[0])
    print("Number of Grey: ", output[250])


parser = argparse.ArgumentParser(description='Count Continuous Color Area.')
parser.add_argument('filename', type=str, nargs='?', default='example.png',
                    help='File should be in the same folder')

args = parser.parse_args()
imgArr = load_img(args.filename)
area_counter([], 0, 0)
output_display()
