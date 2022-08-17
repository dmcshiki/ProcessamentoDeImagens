from pickletools import optimize
from PIL import Image

def image_converter(input_file, output_file, formatType, thumbnailName):
    image = Image.open(input_file)
    image.save(output_file,
     format=formatType,
     optimize = True, 
     quality = 75
     )
    image.thumbnail((75,75))
    image.save(thumbnailName)

def image_format(file):
    image = Image.open(file)
    print(f"Image format: {image.format_description}")

if __name__ == "__main__":
    image_converter("cool.jpg", "cool2.png", "PNG", "thumbnail.jpeg")
    image_format("cool.jpg")
    image_format("cool2.png")
    image_format("image.jpeg")
    # image_format("coolPNGJPEG.jpg")
    # image_converter("castle.png", "castle2.jpg", "JPEG")
    # image_format("castle2.jpg")