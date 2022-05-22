# let's start with the Imports
import cv2
import glob	 
from pathlib import Path

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
        

def image_resize(name: str, width:int, height: int, save_as: str):
    """Resize a image to a new size 
    Args:
        name(str):
            the current name of the image
        width(int):
            the new width of image
        height(int):
            the new height of image
        save_as(str):
            where to save on path and new name
    """    
    dimension = (width, height)
    re_image = cv2.resize(name, dimension)
    cv2.imwrite(save_as ,re_image)
	 
def main():
    #make a list of images in the directory
    picture_list = list(glob.glob("./square_up/*.jpg"))
    
    make_directory("512x512")
    
    # loop the list images	
    for i, c in enumerate(picture_list, 1):
        #read te current image to memory
        im_c = cv2.imread(c)
        #where to save and new name
        new_name = f"512x512/{i}.jpg"
        #saving the resize image
        image_resize(im_c, 512, 512, new_name)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
