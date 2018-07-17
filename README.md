# Detection of Image Tampering using CNN 

## This is an implemntation of the CNN model which is based on the VGG16 pretrained model and Fine tunned on our Datset which is The CASIA.v2 and the Columbia Image Splicing Detection Dataset 
<br />
### Note:<br />
This Model was trained on the Google Colab python notebook in order to be able to run it on the google colab notebook you must edit the path for the dataset and the pretrained model and running the First inside the VGG16_based_model.ipynb to authenticate with the google drive API to load/write files from/to it. <br />

Files structure : <br />

--VGG16_based_model.ipynb  <br />
-- model: <br />
------CNNImageSplicingDetectorModel.json <br />
------CNNImageSplicingDetectorModelWeights.h5 <br />
-- dataset: <br />
------test: <br />
---------img1.jpg <br />
---------img2.jpg <br />
---------img3.jpg <br />
------train: <br />
---------img1.jpg <br />
---------img2.jpg <br />
---------img3.jpg <br />
------valid: <br />
---------img1.jpg <br />
---------img2.jpg <br />
---------img3.jpg <br />

