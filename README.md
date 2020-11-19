## 1.Introduction
&nbsp;&nbsp;This code is used to enhance the image data with various labelings, and includes three elements which respectively are main.py, Visualize.py and main.py. About 30% of the code are based on albumentations, which is cited by [albumentations' website](https://github.com/albumentations-team/albumentations_examples). The albumentations is a tool which specifically use for enhancing data like text, image and etc.  
&nbsp;&nbsp;Then, there will be three parts to explain the code.
## 2. Environment configuration
* Python3.6-3.8  
* albumentations module  
* os module  
* cv2 module  
* xml module  
* matplotlib module
## 3. File Structure
```
* ├── Visualize: Perform image and bounding box visualization operations.
* ├── Getfile: Read the .xml file, creat the .txt file:
      get bounding box parameters; get the width and height of the image; get the category of the object of the image; if the image is croped, then save the image and label in .xml; write the bounding box parameters in yolo format and the category of the object of the image in the .txt file.
* ├── main: Call the Visualize and the Getfile to finish the data enhancement:
      First, visualize the original images and labels; Second, enhance the image and label we choose in ten times in random way; Third, output the enhanced images and labels and visualize them; Finally, create a new txt file to store the enhanced image names and the bounding box parameters of them.
```   
## 4. The DS we use
The DS we use is the remote sensing data of landslide, which is about 1451 for train and about 467 for test.
## 5. Related parameters
* The related parameters of the module-main

|main||
|-|-|
|in_file_dir|the path of original image file|
|image_file_dir|the path of enhanced image file|
|classes|the name of type|
|BOX_COLOR|the color of bounding box|
|TEXT_COLOR|the color of the text of class|  

* The related parameters of the module-Visualize

|Visualize||
|-|-|
|None|Noe|
There are no parameters in the module-Visualize

* The related parameters of the module-Getfile

|Getfile||
|-|-|
|size_h|the height of the original image|
|size_w|the weight of the original image|

## 6. The way to train
* First, please ensure that you have a file full of original images and labels-.xml
* Second, please ensure that you have a file which is used to store the enhanced images and labels-.txt
* Third, modify the 'in_file_dir', 'image_file_dir', 'classes' and 'category_id_to_name'.  
&nbsp;&nbsp;&nbsp;&nbsp;'in_file_dir' is the file dir full of original images and labels.  
&nbsp;&nbsp;&nbsp;&nbsp;'image_file_dir' is the file dir is the storing file dir.  
&nbsp;&nbsp;&nbsp;&nbsp;'classes' is the variety of categories.  
&nbsp;&nbsp;&nbsp;&nbsp;'category_id_to_name' is the dictionary of categories and the corresponding mark numbers.
* Forth, run the code.