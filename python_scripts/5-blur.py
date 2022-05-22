#!venv/bin/python3


# import opencv
import cv2
import shutil
import glob


jpg_list = list(glob.glob("./512x512/*.jpg"))
txt_list = list(glob.glob("./512x512/*.txt"))
txt_list.remove("./512x512/classes.txt") 
 

def blur_copy(im: str, image: str, image_gray: str):
    ksize = (10, 10)
    blur_image = cv2.blur(image, ksize) 
    cv2.imwrite(image_gray, blur_image) 
    print(f"Blur copy being for {image_gray}")

def blur_file(file: str, file_blur: str):
    shutil.copyfile(file, file_blur)
    print(f"auto label for {file_blur[:len(file_blur)-4]}.jpg image done")



def main():
    for im, file in zip(jpg_list, txt_list):
        image = cv2.imread(im)
        image_blur = f"{im[:len(im)-4]}_blur{im[-4:]}"
        file_blur = f"{file[:len(file)-4]}_blur{file[-4:]}"
        blur_copy(im, image, image_blur)
        blur_file(file, file_blur)
    
if __name__ == "__main__":
    main()

# Window shown waits for any key pressing event
cv2.destroyAllWindows()