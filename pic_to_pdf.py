import os

def CompressImage(image_name):
  os.system("convert -resize\"600x800>\" %s %s" % (image_name,image_name))

def CompressAll():
  ext_names = ['.JPG','.jpg','.jepg','*.png']
  for each_image in os.listdir('./'):
    for ext_name in ext_names:
      if each_image.endswith(ext_name):
        CompressImage(each_image)
        break

CompressAll()
os.system("magick *.png +adjoin book.pdf")