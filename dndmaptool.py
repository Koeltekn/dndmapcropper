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
try:
    dpi=int(img.info["dpi"][0])
except:
    print("DPI: ",end='')
    dpi=int(input())

scaled=img.resize((dpi*columns,dpi*rows))
width, height=scaled.size
os.mkdir("cropped")

fullwidth=math.floor(width/(paperformat[0]))*columns
fullheight=math.floor(height/(paperformat[1]))*rows
scaled_bg=Image.new('RGB',(fullwidth,fullheight),(255,255,255))
scaled_bg.paste(scaled,(0,0))

for i in range(0,math.ceil(rows/paperformat[1])):
    for j in range(0,math.ceil(columns/paperformat[0])):
        img_cropped=scaled_bg.crop((j*dpi*paperformat[0],i*dpi*paperformat[1],(j+1)*dpi*paperformat[0],(i+1)*dpi*paperformat[1]))
        img_cropped.save("cropped/cropped"+str(j)+"_"+str(i)+".jpg")
        pdf.add_page()
        pdf.image("cropped/cropped"+str(j)+"_"+str(i)+".jpg",papermargin[0],papermargin[1],paperformat[0],paperformat[1])

pdf.output("cropped.pdf", "F")