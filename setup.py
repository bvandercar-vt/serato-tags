from setuptools import setup

setup(
   name='serato_tags',
   version='1.0',
   description='Serato track metadata tags',
   author='TODO',
   author_email='TODO',
   packages=["serato_tags"],   
   package_dir={"serato_tags": "scripts"},
   install_requires=['mutagen']
)