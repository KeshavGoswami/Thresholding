<h1>Image Thresholding</h1>
<p>
<h3>Goal</h3>

<ul><li>	Simple thresholding, Adaptive thresholding, Otsu's thresholding.</li></ul>
Simple Thresholding
Here, the matter is straight forward. If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). The function used is cv2.threshold. First argument is the source image, which should be a grayscale image. Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value. OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function. Different types are:
<ul>	
<li>cv2.THRESH_BINARY</li>
<li>cv2.THRESH_BINARY_INV</li>
<li>cv2.THRESH_TRUNC</li>
<li>cv2.THRESH_TOZERO</li>
<li>cv2.THRESH_TOZERO_INV</li>
</ul>
</p>
<h3>Gaus</h3>
<p align="center">
  <img src="https://github.com/KeshavGoswami/Thresholding/blob/master/gaus.PNG" width="350"/>
</p>
<h3>Outsu</h3>
<p align="center">
  <img src="https://github.com/KeshavGoswami/Thresholding/blob/master/outsu.PNG" width="350"/>
</p>

<h3>Threshold</h3>
<p align="center">
  <img src="https://github.com/KeshavGoswami/Thresholding/blob/master/threshold.PNG" width="350"/>
</p>

<h3>Threshold 1</h3>
<p align="center">
  <img src="https://github.com/KeshavGoswami/Thresholding/blob/master/threshold1.PNG" width="350"/>
</p>


