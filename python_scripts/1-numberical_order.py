"""rename pictures
as a number list
1.jpg, 2.jpg, 3.jpg, 4.jpg and etc...
"""
import glob
import os
from pathlib import Path
import cv2


#make a list of the pictures in the directory
picture_list = list(glob.glob("./images/*.jpg"))

def make_directory(name_of_directory):
    """check to see if the directory exists
    if not creates the directory

    Arg:
        name_of_directory(str): the name of the directory in question

    """
    # get current working directory
    current_path = Path.cwd()
    #create variable for the directory
    child_directory  = current_path / name_of_directory
    #check a directory exists
    if child_directory.is_dir() == False:
        #print('FALSE')
        #create the directory
        child_directory.mkdir()

def copy_to_directory(directory: str, list_images: list):
    """copying images to new directory
    Args:
        directory(str): the directory to copy
        list_images(list): list of images to be copy
    """
    #loop through the list of the pictures  i as count starting at one, and c as current picture in the list
    for i, c in enumerate(list_images, 1):
        #read the current image
        im = cv2.imread(c)
        #create variable the directory to copy inside current count with .jpg extension 
        x = f"{directory}/{i}.jpg"
        #rprint  the current image copy as new variable x
        print(f"renaming: {c} ---> {x}")
        #creating the copy
        cv2.imwrite(x , im)

def main():
    make_directory("numberical_order")
    copy_to_directory("./numberical_order", picture_list)
    print("All copy")


if __name__ == "__main__":
    main()