
from PIL import Image, ImageDraw, ImageFont

while True:
        while True:
                sen1=150
                sen2=120
                sen3=70
                sen4=80
                sen5=100
                image = Image.open("foot.jpeg")
                draw = ImageDraw.Draw(image)
                if(sen1>0):
                    x=420
                    y=340
                    r=10+sen1/10
                    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,255))
                if(sen2>0):
                    x=325
                    y=585
                    r=10+sen2/10
                    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,255))
                if(sen3>0):
                    x=350
                    y=515
                    r=10+sen3/10
                    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,255))
                if(sen4>0):
                    x=280
                    y=245
                    r=10+sen4/10
                    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,255))
                if(sen5>0):
                    x=248
                    y=105
                    r=10+sen5/10
                    draw.ellipse((x-r,y-r,x+r,y+r),fill=(255,0,0,255))
                break
        break
image.show()
