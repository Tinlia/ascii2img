from PIL import Image, ImageDraw
import time
import math

from dictionaries import colorMatrices
from dictionaries import colours

# Invert the image rgb
inverted = False

# Remove spacing character (⠄, . , ⢀)
removeSpacing = True

# Improve Shading (Not recommended for below 50x50)
shadingEnabled = True

# Advanced Shading (Not recommended for below 250x250)
advancedShadingEnabled = True

# Name of the ASCII file
filename = 'ascii2.txt'

# Name of the output img
output = "pixel_art2.png"

timeStart = time.time()

def create_pixel_art():
    # Set the width and height of each cell
    cell_width = 2
    cell_height = 4

    # Calculate the total width and height of the image
    image_width = cell_width * len(lines[0])
    image_height = cell_height * len(lines)

    # Create a new image with a black background
    image = Image.new("RGB", (image_width, image_height), "black")
    draw = ImageDraw.Draw(image)

    canvasLines = {}
    lineNo = 0

    # Loop through data and format a dictionary for black/white pixels
    for line in lines:
        # Set the lines as empty lists
        for x in range(0,4):
            canvasLines[lineNo + x] = []

        # Fill in the lines numbers four at a time
        for ascii in line:
            for x in range(0,4):
                # If an ascii character
                canvasLines[lineNo + x].extend(colorMatrices[ascii][x])
        lineNo += 4

    # Print the image from the canvasLines dict
    for y in range(1, len(canvasLines)-1):
        for x in range(1, len(canvasLines[y])-1):
            if advancedShadingEnabled:
                s = 0
                # Check surrounding 8 pixels
                for r in range(-1,2):
                    for c in range(-1,2):
                        # If not the center pixel
                        if r != 0 or c != 0:
                            if inverted:
                                s += 1 if canvasLines[y+r][x+c] == 0 else 0
                            else:
                                s += canvasLines[y+r][x+c]
                                
                # Adjust rgb based on surrounding pixels
                rgb = math.floor(((-255/8)*s)+255) if inverted else math.floor((255/8)*s)
                draw.point((x,y), (rgb, rgb, rgb))
                
            # If shaded and not a border pixel
            elif shadingEnabled and len(canvasLines) > y > 0 and len(canvasLines[y]) > x > 0:
                s = 0
                # Check adjacent pixels 
                if canvasLines[y+1][x] == 1: s += 1
                if canvasLines[y][x+1] == 1: s += 1
                if canvasLines[y-1][x] == 1: s += 1
                if canvasLines[y][x-1] == 1: s += 1

                draw.point((x,y), colours[s] if inverted else colours[4-s])
            elif shadingEnabled or advancedShadingEnabled:
                # If an edge
                draw.point((x,y), (255, 255, 255) if inverted else (0, 0, 0))
            else:
                if inverted:
                    draw.point((x,y), (255, 255, 255) if canvasLines[y][x]==0 else (0, 0, 0))
                else:
                    draw.point((x,y), (255, 255, 255) if canvasLines[y][x]==1 else (0, 0, 0))


    image.save(f'./images/{output}') # Save the image as a PNG file

lines = []  # Initialize an empty array to store lines

# Find the length of the longest line
with open(f'./inputs/{filename}', 'r', encoding='utf-8') as file:
    lines = [line.replace('\n', '') for line in file.readlines()]
    max_len = len(max(lines, key=len)) 
    lines = []
    file.close()

# Open the file in read mode to collect data
with open(f'./inputs/{filename}', 'r', encoding='utf-8') as file:
    # Read each line and add it to the 'lines' array
    for line in file:
        paddedLine = line.rstrip().ljust(max_len, ' ')
        lines.append(paddedLine.replace('\n',''))  # Remove leading and trailing whitespaces


if removeSpacing:
    colorMatrices['⠄']= [ [0, 0], [0, 0], [0, 0], [0, 0]]
    colorMatrices['⢀']= [ [0, 0], [0, 0], [0, 0], [0, 0]]
    colorMatrices['.']= [ [0, 0], [0, 0], [0, 0], [0, 0]]
    
create_pixel_art()
timeEnd = time.time()

elapsedTime = timeEnd - timeStart
print("\nTime elapsed: " + str(elapsedTime) + " s\n")
