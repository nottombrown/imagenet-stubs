import glob
import os

images_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))

def get_image_paths():
    rel_paths = glob.glob(images_dir + "/*")
    return [os.path.join(images_dir, rel_path) for rel_path in rel_paths]
