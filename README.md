# ascii2img v0.2
A small Python program to convert 6- and 8-bit braille ASCII Art to Black/White Pixel art


![Pixel Art](/images/pixel_art.jpg) 

## Overview

`ascii2img` is a simple Python program that converts ASCII art into pixel art images. The program takes input from a text file (`ascii.txt`) containing ASCII art and generates an output image (`pixel_art.jpg`). The conversion is done by mapping ASCII characters to pixel matrices. 

This program currently supports 6-8 Bit Braille characters, shades, spaces, periods, and commas.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tinlia/ascii2img.git
   cd ascii2img
   ```
2. Install `pillow`
   ```bash
   pip install pillow
   ```

## Usage

1. Edit the ascii.txt file to include your braille ASCII art.

2. Run the conversion script:

```bash
python convert.py
```

3. Check the output image in pixel_art.jpg.

## ASCII Mapping
The program maps ASCII characters to pixel matrices in the `colorMatrices` dictionary. You can customize this dictionary to add more characters or modify existing mappings.

This program currently ignores any whitespace in the `ascii.txt` file, so it is suggested that every whitespace be replaced by the character `⠈`. This will be patched next

## Examples
Three examples are provided:  
 1. [ascii.txt](/inputs/ascii.txt) --> [output](/images/pixel_art.jpg) (13,500 characters)
 2. [ascii2.txt](/inputs/ascii2.txt) --> [output](/images/pixel_art2.jpg) (37,500 characters)
 3. [ascii3.txt](/inputs/ascii3.txt) --> [output](/images/pixel_art3.jpg) (150,000 characters)

## Credits
Braille ASCII art generated using [Lachlan's Braille ASCII Generator](https://lachlanarthur.github.io/Braille-ASCII-Art/)
