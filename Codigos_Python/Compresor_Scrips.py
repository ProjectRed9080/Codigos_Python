from PIL import Image  # python3 -m pip install Pillow

import os

downloadsFolder = "/Users/elias/Downloads/"
picturesFolder = "/Users/elias/Downloads/Photos/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "compressed_" +
                         filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".exe"]:
            aplicationFolder = "/Users/elias/Downloads/Aplicación/"
            os.rename(downloadsFolder + filename, aplicationFolder + filename)

        if extension in [".pdf"]:
            DocumentFolder = "/Users/elias/Downloads/Documentos PDFS/"
            os.rename(downloadsFolder + filename, DocumentFolder + filename)

        if extension in [".docx"]:
            DocumentFolder = "/Users/elias/Downloads/Documentos Words/"
            os.rename(downloadsFolder + filename, DocumentFolder + filename)

        if extension in [".mp4"]:
            VideoFolder = "/Users/elias/Downloads/documentos_mp4/"
            os.rename(downloadsFolder + filename, VideoFolder + filename)

        if extension in [".txt"]:
            txtFolder = "/Users/elias/Downloads/Documentos_txt/"
            os.rename(downloadsFolder + filename, txtFolder + filename)
