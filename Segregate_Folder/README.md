Python script to segregate a input_folder having images, and text files
Into the two folder having images, and texts files in sepration.


input_folder:
  -image1.png
  -text1.txt
  -image2.tiff

Input: complete path to input_folder

Output: Two Folders are created in following manner:
input_folder:
  image_folder:
    -image1.png
    -image2.tiff
  text_folder:
    -text1.txt
  

Run The script as:
python segregate.py --src "/C:/path/input_folder"
