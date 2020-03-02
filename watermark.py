import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 设置所使用的字体和字体大小
font1 = ImageFont.truetype("c:\\windows\\fonts\\micross.ttf", 100)

# 打开图片
imageFile = "C:\\ProgramData\\Anaconda3\\envs\\weixin\pic\\200226-122147.png"
im1 = Image.open(imageFile)

# 绘图实例化
draw1 = ImageDraw.Draw(im1)

# 设置水印的位置,内容,颜色,字体
draw1.text((10, 10), "www.zhaokaifeng.com", (255, 0, 0), font=font1)

# 将生成的图片另存
im1.save("200226-122147.png")