from asyncio import wait_for
from PIL import Image
from fpdf import FPDF
import math
import os
import shutil

folder_name = "tiles/"
pdf_name = "tiles"
A0 = (32, 46)
A0margin = (0.55, 0.4)
A1 = (22, 32)
A1margin = (0.7, 0.55)
A2 = (15, 22)
A2margin = (0.75, 0.7)
A3 = (11, 16)
A3margin = (0.35, 0.25)
A4 = (7, 10)
A4margin = (0.65, 0.85)


def wait_for_key():
    print("Press enter to exit")
    input()
    exit()


def get_map():
    map_path = os.path.join(os.path.dirname(__file__), "map.jpg")
    try:
        img = Image.open(map_path)
    except:
        map_path = os.path.join(os.path.dirname(__file__), "map.jpeg")
        try:
            img = Image.open(map_path)
        except:
            map_path = os.path.join(os.path.dirname(__file__), "map.png")
            try:
                img = Image.open(map_path)
            except:
                map_path = os.path.join(os.path.dirname(__file__), "map.webp")
                try:
                    img = Image.open(map_path)
                except:
                    print('Map file could not be found, rename the file as "map" (supported file types png, jpg, jpeg, webp)')
                    wait_for_key()

    return img


def create_folder():
    try:
        os.mkdir(folder_name)
    except FileExistsError as error:
        shutil.rmtree(folder_name)
        os.mkdir(folder_name)


def get_image_dpi(image):
    try:
        dpi = int(image.info["dpi"][0])
    except:
        print("Image dpi could not be obtained, type the image DPI: ", end="")
        dpi = int(input())

    return dpi


def get_paper_format():
    paperformatinput = input()
    if paperformatinput == "A0":
        paperformat = A0
        papermargin = A0margin
        pdf = FPDF("P", "in", "A0")
    elif paperformatinput == "A1":
        paperformat = A1
        papermargin = A1margin
        pdf = FPDF("P", "in", "A1")
    elif paperformatinput == "A2":
        paperformat = A2
        papermargin = A2margin
        pdf = FPDF("P", "in", "A2")
    elif paperformatinput == "A3":
        paperformat = A3
        papermargin = A3margin
        pdf = FPDF("P", "in", "A3")
    elif paperformatinput == "A4":
        paperformat = A4
        papermargin = A4margin
        pdf = FPDF("P", "in", "A4")
    else:
        paperformat = ""
        papermargin = ""
        pdf = ""

    return (paperformat, papermargin, pdf)


map_img = get_map()
dpi = get_image_dpi(map_img)
create_folder()

print("Number of rows: ", end="")
rows = int(input())
print("Number of columns: ", end="")
columns = int(input())

print("Choose output format (A0 / A1 / A2 / A3 / A4): ", end="")
paperformat, papermargin, pdf = get_paper_format()
while(paperformat==""):
    print("Invalid paper format, choose either A4 or A3")
    paperformat, papermargin, pdf = get_paper_format()


# Resize image
scaled_img = map_img.resize((dpi * columns, dpi * rows))
width, height = scaled_img.size

row_subdivision_count=math.ceil(rows / paperformat[1])*math.ceil(columns / paperformat[0])
column_subdivision_count=math.ceil(rows / paperformat[0])*math.ceil(columns / paperformat[1])

if row_subdivision_count>column_subdivision_count:
    scaled_img=scaled_img.rotate(90,expand=1)
    width,height=height,width
    rows,columns=columns,rows

# Add white padding
fullwidth = (math.ceil(width/(paperformat[0]*dpi)))*(columns*dpi)
fullheight = (math.ceil(height/(paperformat[1]*dpi)))*(rows*dpi)
scaled_padded_img = Image.new("RGB", (fullwidth, fullheight), (255, 255, 255))
scaled_padded_img.paste(scaled_img, (0, 0))

for i in range(0, math.ceil(rows / paperformat[1])):
    for j in range(0, math.ceil(columns / paperformat[0])):
        img_cropped = scaled_padded_img.crop(
            (
                j * dpi * paperformat[0],
                i * dpi * paperformat[1],
                (j + 1) * dpi * paperformat[0],
                (i + 1) * dpi * paperformat[1],
            )
        )

        img_cropped.save(folder_name + str(j) + "_" + str(i) + ".jpg")
        pdf.add_page()
        pdf.image(
            folder_name + str(j) + "_" + str(i) + ".jpg",
            papermargin[0],
            papermargin[1],
            paperformat[0],
            paperformat[1],
        )
            
pdf.output(pdf_name + ".pdf", "F")
