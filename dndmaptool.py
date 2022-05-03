from PIL import Image
from fpdf import FPDF
import math
import os
print("Rows: ",end='')
rows = int(input())
print("Columns: ",end='')
columns = int(input())
mydata_path = os.path.join(os.path.dirname(__file__), "map.jpg")
img = Image.open(mydata_path)
dpi=img.info["dpi"][0]
width, height=img.size
scalata=img.resize((dpi*columns,dpi*rows))
os.mkdir("cropped")
pdf = FPDF('P', 'mm', 'A3')
for i in range(0,math.ceil(rows/16)):
    for j in range(0,math.ceil(columns/11)):
        img_cropped=scalata.crop((j*dpi*11,i*dpi*16,(j+1)*dpi*11,(i+1)*dpi*16))
        img_cropped.save("cropped/cropped"+str(j)+"_"+str(i)+".jpg")
        pdf.add_page()
        pdf.image("cropped/cropped"+str(j)+"_"+str(i)+".jpg",0,0,297,420)

pdf.output("cropped.pdf", "F")