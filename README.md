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

4. Toggle removeSpacing to `True` to get rid of spacing in images
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/766387914136485948/1180631571666059344/spaceTrue.jpg?ex=657e1fd5&is=656baad5&hm=460c59181f56e3bd88a2842d5bd0f905a7ab9ce10a20b95ed0c8d9eaa4f1341a&"  width=100px/> <img src="https://cdn.discordapp.com/attachments/766387914136485948/1180631571905126470/spaceFalse.jpg?ex=657e1fd5&is=656baad5&hm=7c6f833f3e5b48c90403bf1886989e23152a7b4843e34fadf89315f391689db9&" width=100px/>
</p>

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
