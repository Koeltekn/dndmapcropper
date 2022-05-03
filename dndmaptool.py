from PIL import Image
from fpdf import FPDF
import math
import os

A3=(11,16)
A3margin=(0.35,0.25)
A4=(8,11)
A4margin=(0.15,0.35)

print("Choose format (A3 / A4): ",end='')
paperformatinput=input();
if paperformatinput=="A3":
    paperformat=A3
    papermargin=A3margin
    pdf = FPDF('P', 'in', 'A3')
elif paperformatinput=="A4":
    paperformat=A4
    papermargin=A4margin
    pdf = FPDF('P', 'in', 'A4')
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
        pdf.image("cropped/cropped"+str(j)+"_"+str(i)+".jpg",papermargin[0],papermargin[1],paperformat[0],paperformat[1])

pdf.output("cropped.pdf", "F")