from PIL import Image
from fpdf import FPDF
import math
import os

A3=(11,16)
A3mm=(297,420)
A4=(5,8)
A4mm=(210,297)

print("Choose format (A3 / A4): ",end='')
paperformatinput=input();
if paperformatinput=="A3":
    paperformat=A3
    papermm=A3mm
    pdf = FPDF('P', 'mm', 'A3')
elif paperformatinput=="A4":
    paperformat=A4
    papermm=A4mm
    pdf = FPDF('P', 'mm', 'A4')
else:
    print("Wrong paper format")
    exit()

print("Rows: ",end='')
rows = int(input())
print("Columns: ",end='')
columns = int(input())
mydata_path = os.path.join(os.path.dirname(__file__), "map.jpg")
img = Image.open(mydata_path)
dpi=int(img.info["dpi"][0])
width, height=img.size
scalata=img.resize((dpi*columns,dpi*rows))
os.mkdir("cropped")

for i in range(0,math.ceil(rows/paperformat[1])):
    for j in range(0,math.ceil(columns/paperformat[0])):
        img_cropped=scalata.crop((j*dpi*paperformat[0],i*dpi*paperformat[1],(j+1)*dpi*paperformat[0],(i+1)*dpi*paperformat[1]))
        img_cropped.save("cropped/cropped"+str(j)+"_"+str(i)+".jpg")
        pdf.add_page()
        pdf.image("cropped/cropped"+str(j)+"_"+str(i)+".jpg",0,0,papermm[0],papermm[1])

pdf.output("cropped.pdf", "F")