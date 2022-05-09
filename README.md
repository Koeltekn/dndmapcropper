# DnD Map cropper
Tool to crop DnD tiled maps to fit them in A4 and A3 papers, while maintaining the tile dimension to 1inch

## Supported file types
- ✅ Png
- ✅ Jpg
- ✅ Webp

# Requirements
Python 3 along with the following libraries are required:
### FPDF (https://pypi.org/project/fpdf/)
- Install with:
```sh
pip install fpdf
```
### Pillow (https://pillow.readthedocs.io/en/stable/index.html)
- Install with: 
```sh
pip install Pillow
```
  
# Instructions
- Download the python script
- Place the map file (renamed as "map") in the same folder as the script
- Run the script
- Type the DPI of the image if requested (view DPI paragraph)
- Type the number of rows and columns the map has
- Type the paper format

## DPI
The software automatically detects DPI from 'dpi' field in the map file, however not all files includes this field, in this case the program will prompt you to insert it manually.
### Find DPI of a picure on Windows:
- Right click on the image
- Properties
- Switch to Details tab
- Horizontal resolution and Vertical resolution in the Image section shows the dpi
### Find DPI of a picture on MacOS:
- Open the image with "Preview"
- Click "Tools" > "Show inspector" (or ⌘I)
- DPI is shown in the popup
