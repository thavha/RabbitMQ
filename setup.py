from setuptools import find_packages, setup
setup(
    packages=find_packages(),
    name="one",
    version="1.0.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)