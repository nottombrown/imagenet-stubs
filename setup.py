from setuptools import setup

setup(name='imagenet-stubs',
      version='0.0.7',
      author='Tom Brown',
      author_email='nottombrown@gmail.com',
      packages=['imagenet_stubs'],
      package_data={'imagenet_stubs': ['images/*.jpg']},
      include_package_data=True,
     )
