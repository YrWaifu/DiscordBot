from PIL import Image, ImageDraw, ImageFont

image = Image.open("../misc/Banana.jpeg")

draw = ImageDraw.Draw(image)
text = input()

width, height = image.size

font = ImageFont.truetype("../misc/7fonts.ru_Berta_Drug_01.ttf", 50)

textBbox = draw.textbbox((0, 0), text, font=font)

textX = (width - textBbox[2] - textBbox[0]) / 2
textY = height - height / 10

draw.text((textX, textY), text, font=font, fill=(0, 0, 0))

image.save("../misc/Cucumber.jpeg")