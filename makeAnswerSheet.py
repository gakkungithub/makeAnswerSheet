from PIL import Image
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

image_extensions = ['.png', '.jpg', '.jpeg', '.gif', 'bmp', '.tiff']
image_folder_name = input("input your answer sheet folder: ")

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
    fixed_width = int(fixed_img.width * 150 / fixed_img.height)
    c.drawString(100, y_position+52, img.stem)
    c.drawImage(img_path, x=100, y=y_position-100, width=fixed_width, height=150)
    y_position -= 160

    # pdfの下まで行ったら次のページを作る
    if y_position < 60:
        c.showPage()
        c.setFont('GenShinGothic', font_size)
        y_position = height - 60

c.save()
# image_paths = input("input your answer sheets by separating them with comma: ").split(',')
# images = [Image.open(f'images/{image}') for image in image_paths]

