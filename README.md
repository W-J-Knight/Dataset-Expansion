# Dataset  Expansion by Augmentation  With Lables to Match for YOLO5

1. install vertual python enveriment
     ```bash
    python3 -m venv venv
    ```
1.  active pytyon enveriment
    ```bash
    source venv/bin/activate
    ```
1. install python modules
    ```bash
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    ```
    
1.  get images
    * for the web
    * take pictures
1. preparing the dataset
    * renaming the dataset with numbers
    ```bash
    python3 ./python_scripts/1-numberical_order.py
    ```
    * square up the images
    ```bash
    python3 ./python_scripts/2-square_up.py
    ```
    * resizing the images
    ```bash
    python3 ./python_scripts/3-resize.py
    ```
1. clean up
    *  compress the orginals to save space 
    * delete directories numberical_order and square_up
    * move images.tar.gz to Pictures dicetory
    *  delete images
    ```bash
    tar -czvf images.tar.gz ./images
    rm -r numberical_order square_up
    mv images.tar.gz ~/Pictures
    rm -r images 
    ```
1. lable images
    * labelIMG
        * installing labelIMG
            * https://pypi.org/project/labelImg/
        * open labelImg 

            ``` bash
            pip3 install labelImg 
            labelImg
            ```
<!-- make screenshot labvelIMG open -->
1. lable images
    * make for yolo5 
        * text file
        
2.  expand dataset with new lables
    * Make gray images
    ```bash
    python3 ./python_scripts/4-gray.py
    ```
    * Make Images blur
    ```bash
    python3 ./python_scripts/5-blur.py
    ```

    * Make brighter and darker images
    ```bash
    python3 ./python_scripts/6-bright_dark.py 
    ```
    


