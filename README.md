#Cam_motion_field
###Description
This package provides quick and easy way to compute camera motion field given
two consecutive images.
### Install
```
pip install cam-motion-field
```
###Usage
```python
from cam_motion_field import get_cam_flow
import cv2
image1_file = "PATH/TO/THE/FIRST/IMAGE/FILE"
image2_file = "PATH/TO/THE/SECOND/IMAGE/FILE"
ncol = 10
nrow = 10
grid_size = (ncol, nrow)

img1 = cv2.imread(image1_file, 0)
img2 = cv2.imread(image2_file, 0)
# origins.shape = (10,10,2)
# displacements.shape = (10,10,2)
origins, displacements = get_cam_flow(img1, img2, grid_size[0], grid_size[1])
```
The above example defines a 10x10 grid and returns 100 origins and
displacement points. Both origins and displacements are absolute coordinates!

##Example


<img src="https://github.com/stamas02/cam_motion_field/data/image_anim.gif" width="40"/>
