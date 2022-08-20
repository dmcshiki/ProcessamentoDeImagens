import io
import os
import PySimpleGUI as sg
from PIL import Image
import urllib.request

def saveImage(input_file, output_file, formatType, qualityPercentage): 
    image = Image.open(input_file)
    image.save(output_file,
     format=formatType,
     optimize = True, 
     quality = qualityPercentage
     )

def saveThumbnail(input_file, output_thumbnail): 
    image = Image.open(input_file)
    image.thumbnail((75,75))
    image.save(output_thumbnail)

def main():
    layout = [
        [
            sg.Image(
                key = "imageKey",
                size = (500, 500)
            )
        ],
        [
            sg.Text("Image file"),
            sg.Input(size = (25,1), key = "fileKey"),
            sg.FileBrowse(file_types = [("JPEG (*.jpg)", "*.jpg"), ("PNG (*.png)", "*.png"), ("All", "*.*")]),
            sg.Button("Load image"),
        ],
        [
            sg.Text("Show image from internet instead"),
            sg.Input(size = (25,1), key = "urlKey"),
            sg.Button("Load image from web"),
        ],
        [
            sg.Text("Choose the format to save the image"),
            sg.Combo(['PNG', 'JPEG'], default_value='PNG', key='formatKey')
        ],
        [
            sg.Text("Image name"),
            sg.Input(size = (25,1), key = "imageName"),
            sg.Button("Save Image"),
            sg.Button("Save low quality Image"),
            sg.Button("Save image as thumbnail")
        ],

    ]

    window = sg.Window("Image viewer", layout = layout)


    isScreenOpen = True

    while isScreenOpen: 
        event, value = window.read()

        if event == "Exit" or event == sg.WINDOW_CLOSED:
            isScreenOpen = False
        if event == "Load image":
            fileName = value["fileKey"]
            if os.path.exists(fileName):
                image = Image.open(fileName)
                image.thumbnail((500, 500))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["imageKey"].update(data = bio.getvalue(), size = (500,500))

        if event == "Load image from web":
            if value["urlKey"] != '':
                urlResponse = value["urlKey"]
                urllib.request.urlretrieve(
                urlResponse,
                'image.png')
                image = Image.open('image.png')
                image.thumbnail((500, 500))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["imageKey"].update(data = bio.getvalue(), size = (500,500))

        if event == "Save Image": 
            fileName = value["fileKey"]
            if os.path.exists(fileName):
                if value['imageName'] != '':
                    imageName = value['imageName'] + '.' + value["formatKey"].lower()
                    saveImage(fileName, imageName, value["formatKey"], 100)

        if event == "Save low quality Image": 
            fileName = value["fileKey"]
            if os.path.exists(fileName):
                if value['imageName'] != '':
                    lowQualityImageName = value['imageName'] + 'lowQuality.' + value["formatKey"].lower()
                    saveImage(fileName, lowQualityImageName, value["formatKey"], 75)

        if event == "Save image as thumbnail": 
            fileName = value["fileKey"]
            if os.path.exists(fileName):
                if value['imageName'] != '':
                    thumbnailName = value['imageName'] + 'thumbnail.' + value["formatKey"].lower()
                    saveThumbnail(fileName, thumbnailName)
    
    window.close()


if __name__ == "__main__":
    main()