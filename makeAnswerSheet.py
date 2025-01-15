from PIL import Image
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import subprocess

image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
image_folder_name = input("input your answer sheet folder: ")
while True:
    ISTEXT = input("add titles of your answer sheets? (y or n): ")
    if ISTEXT in ('y', 'n'):
        break
    print("input 'y' or 'n'")

# select files of image format
folder = Path(f'images/{image_folder_name}')
image_files = [f for f in folder.rglob('*') if f.suffix.lower() in image_extensions]

# create the best pdf
while True:
    # set height in integer (100 or higher)
    while True:
        try:
            HEIGHT = int(input("input height of all answer sheet in integer: "))
            if HEIGHT > 100:
                break
            else:
                print("this height is too small !!")
        except ValueError:
            print("input one integer")

    # initial settings of pdf
    c = canvas.Canvas(f"as_pdf/{image_folder_name}.pdf", pagesize=A4)

    # add Japanese font
    pdfmetrics.registerFont(TTFont('GenShinGothic', "./fonts/GenshinGothic/GenShinGothic-Monospace-Medium.ttf"))
    font_size = 5
    c.setFont('GenShinGothic', font_size)

    width, height = A4
    y_position = height - 60

    for img in image_files:
        img_path = f'images/{image_folder_name}/{img.name}'
        fixed_img = Image.open(img_path)
        fixed_width = int(fixed_img.width * HEIGHT / fixed_img.height)
        # at bottom of the current page, new page will be added
        if y_position < HEIGHT:
            c.showPage()
            c.setFont('GenShinGothic', font_size)
            y_position = height - 60
        if ISTEXT == 'y':
            c.drawString(100, y_position+52, img.stem)
        c.drawImage(img_path, x=100, y=y_position-HEIGHT+50, width=fixed_width, height=HEIGHT)
        y_position -= (HEIGHT+10)

    c.save()

    try:
        subprocess.run(['open', f"as_pdf/{image_folder_name}.pdf"])
        while True:
            ISOK = input("save this pdf or create a new pdf? (save or new): ")
            if ISOK in ('save', 'new'):
                break
            print("input 'save' or 'new'")
        if ISOK == 'save':
            break
    except Exception as e:
        print(f"ERROR: {e}")
        break

print(f"check '{image_folder_name}.pdf' in the 'as_pdf' folder !!")

