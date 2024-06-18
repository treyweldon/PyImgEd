from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './PyImgEd/edits'

for filename in os.listdir(path):
    image = Image.open(f'{path}/{filename}')

    edit = image.filter(ImageFilter.SHARPEN).convert('L')

    cFactor = 1.4
    contrast = ImageEnhance.Contrast(edit)
    contEdit = contrast.enhance(cFactor)

    bFactor = 1.2
    brightness = ImageEnhance.Brightness(edit)
    brigEdit = brightness.enhance(bFactor)

    new_name = os.path.splitext(filename)[0]

    edit.save(F'.{pathOut}/{new_name}_edited.jpg')

