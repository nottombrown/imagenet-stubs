# ImageNet Stubs
A tiny set of ImageNet-like images for testing pipelines


All images are licensed with Creative Commons and were found on flickr.com

### Usage

Install the python module
```bash
pip install git+https://github.com/nottombrown/imagenet_stubs
```

The module includes all the images. You can ask it for their paths
```python
import imagenet_stubs
import PIL.Image
import matplotlib.pyplot as plt

for image_path in imagenet_stubs.get_image_paths():
    im = PIL.Image.open(image_path)
    plt.axis('off')
    plt.imshow(im, interpolation="nearest")
    plt.show()
```

### Wishlist

- [ ] Include easy accessor for labels for each image 
- [ ] Add additional images (up to 128)
