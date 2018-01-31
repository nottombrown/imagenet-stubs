import glob
import os

root_dir = os.path.dirname(os.path.abspath(__file__))

images_dir = os.path.join(root_dir, 'images')

def get_image_paths():
    rel_paths = glob.glob(images_dir + "/*")
    return [os.path.join(images_dir, rel_path) for rel_path in rel_paths]
