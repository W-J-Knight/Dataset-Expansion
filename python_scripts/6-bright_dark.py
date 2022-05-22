#!venv/bin/python3


# import opencv
from PIL import Image, ImageEnhance
import shutil
import glob
import numpy
import itertools


jpg_list = list(glob.glob("./512x512/*.jpg"))
txt_list = list(glob.glob("./512x512/*.txt"))
txt_list.remove("./512x512/classes.txt") 

def dark_copy(im: str, image: str, image_dark: str):
    enhancer = ImageEnhance.Brightness(image)
    factor = 0.7 #brightens the image
    im_output = enhancer.enhance(factor)
    im_output.save(image_dark)
    print(f"Dark copy being for {image}")



def bright_copy(im: str, image: str, image_bright: str):
    enhancer = ImageEnhance.Brightness(image)
    factor = 1.5 #brightens the image
    im_output = enhancer.enhance(factor)
    im_output.save(image_bright)
    print(f"Bright copy being for {image}")

def dark_file(file: str, file_dark: str):
    shutil.copyfile(file, file_dark)
    print(f"auto label for {file_dark[:len(file_dark)-4]}.jpg image done")


def bright_file(file: str, file_bright: str):
    shutil.copyfile(file, file_bright)
    print(f"auto label for {file_bright[:len(file_bright)-4]}.jpg image done")






def main():
    for im,file in zip(jpg_list,txt_list):
        image = Image.open(im)
        # file_name, file_ext = im.split(".")
        image_bright = f"{im[:len(im)-4]}_bright{im[-4:]}"
        image_dark = f"{im[:len(im)-4]}_dark{im[-4:]}"
        file_bright = f"{file[:len(file)-4]}_bright{file[-4:]}"
        file_dark = f"{file[:len(file)-4]}_dark{file[-4:]}"
        dark_copy(im, image, image_dark)
        dark_file(file, file_dark)
        bright_copy(im, image, image_bright)
        bright_file(file, file_bright)

if __name__ == "__main__":
    main()       
    # dark(image, file_name)



