import cv2
import shutil
import glob


jpg_list = list(glob.glob("./512x512/*.jpg"))
txt_list = list(glob.glob("./512x512/*.txt"))
txt_list.remove("./512x512/classes.txt") 

def gray_copy(im: str, image: str, image_gray: str):
    # By copying the data for color image text to gray image file.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # save the gray image
    cv2.imwrite(image_gray, gray)
    print(f"{im} has been copy to gray scale: {image_gray}")


def gray_file(file: str, file_gray: str):
    # Making label text file for the gray image.
    shutil.copyfile(file, file_gray)
    print(f"auto label for {file_gray[:len(file_gray)-4]}.jpg image done")



def main():
    for im, file in zip(jpg_list, txt_list):
        image = cv2.imread(im)
        image_gray = f"{im[:len(im)-4]}_gray{im[-4:]}"
        file_gray = f"{file[:len(file)-4]}_gray{file[-4:]}"
        gray_copy(im, image, image_gray)
        gray_file(file, file_gray)


if __name__ == "__main__":
    main()


# Window shown waits for any key pressing event
cv2.destroyAllWindows()
