from PIL import Image
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

HEIGHT = 250

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
    if ISTEXT == 'y':
        c.drawString(100, y_position+52, img.stem)
    c.drawImage(img_path, x=100, y=y_position-HEIGHT+50, width=fixed_width, height=HEIGHT)
    y_position -= (HEIGHT+10)

    # pdfの下まで行ったら次のページを作る
    if y_position < 60:
        c.showPage()
        c.setFont('GenShinGothic', font_size)
        y_position = height - 60

c.save()
