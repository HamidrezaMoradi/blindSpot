<h1 style="text-align: center">Blind Spot</h1> 

### ***About***
A simple script for construction of mosaic images in python.

### ***FAQ***
> **What is the mosaic image?**
>> [From Wikipedia](https://en.wikipedia.org/wiki/Photographic_mosaic): In the field of photographic imaging, a photographic mosaic, also known under the term Photomosaic, a portmanteau of photo and mosaic, is a picture (usually a photograph) that has been divided into (usually equal sized) tiled sections, each of which is replaced with another photograph that matches the target photo. When viewed at low magnifications, the individual pixels appear as the primary image, while close examination reveals that the image is in fact made up of many hundreds or thousands of smaller images. Most of the time they are a computer-created type of montage...

### ***Installation:***
Manual install via git :

```shell
$ git clone https://github.com/hamdirezamoradi/blindSpot.git
$ cd blindSpot
$ python setup.py install
```

### ***Usage:***
Try your first blindSpot program

```python
from blindSpot import BlindSpot

mainImage = 'original.jpeg'
tilesPath = 'tilesPath/'

mosaic = BlindSpot(mainImage, tilesPath)
mosaic.mosaicByNumTiles(numberOfVerticalTiles = 80, numberOfHorizontalTiles = 120, enlargement = 10).save("mosaic.jpg")
# "numberOfVerticalTiles" Number of vertical tile
# "numberOfHorizontalTiles" Number of horizontal tile
# "enlargement" it sets the size of the final image compared to the original image.
```

And shell

```shell
$ BlindSpot -m original.jpeg -t img/
```

### ***Performance:***
|Original Image|Tiles Images|Final Resualt|
|:---:|:---:|:---:|
|![original image](https://user-images.githubusercontent.com/31303957/65553601-13809c80-df34-11e9-8647-aa9bbba87cc0.jpg)|![tiles images](https://user-images.githubusercontent.com/31303957/65553771-76723380-df34-11e9-98a4-459ea301aef3.JPG)|![final resualt](https://user-images.githubusercontent.com/31303957/65553661-3a3ed300-df34-11e9-9674-324a7b25775f.jpg)(click through for [full mosaic](http://uupload.ir/files/z8tw_mosaic.jpg) ~40MB)|
