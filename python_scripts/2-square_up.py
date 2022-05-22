# importing cv2
import cv2
import glob
import os
from pathlib import Path


# Reading an image in default mode
#im = cv2.imread("1.jpg")


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
        

def square_up_image(name: str, im: str,top: int=0, bottom: int=0,left: int=0 ,right: int=0): 
    """Square up the image by add border the right or the bottom
        Args: 
            name(str): The name of the square image
            im(str): the current image anme
            top(int): should stay at defualt 0
            bootom(int): should stay at defualt 0 unless adding border square up the image size 
            left(int): should stay at defualt 0
            right(int):  should stay at defualt 0 unless adding border square up the image size
    """
    #light purple color
    RED = [255,0,255]
    #create a border for the image
    im = cv2.copyMakeBorder(im, top,bottom,left,right, cv2.BORDER_CONSTANT, value=RED)
    #save the new square up image
    status = cv2.imwrite(name, im)
    print("Image written to file-system in square_up : ",status)


def main():
    #make a list of the pictures in the directory
    picture_list = list(glob.glob("./numberical_order/*.jpg"))
    #loop through the list of the pictures  i as count starting at one, and c as current picture in the list
    make_directory("square_up")
    for i, c in enumerate(picture_list, 1):
        im_c = cv2.imread(c)
        height, width  = im_c.shape[0:2]
        #create variable as current count with .jpg extension
        name = f"square_up/{i}.jpg"
        #rename the current picture as new variable x
        # print(f"renaming: {c} ---> {x}")
        # os.rename(c, x)
        if height > width:
            x = height - width
            #add border on the right
            square_up_image(name, im_c, right=x)
        elif width > height:
            x = width - height  
            #add border on the bottom 
            square_up_image(name, im_c, bottom=x)
        else:                                                                                           
            print("Width and height are equal")   



if __name__ == "__main__":
    main()
