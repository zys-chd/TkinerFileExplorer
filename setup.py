import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TkinkerFileExplorer",
    version="0.0.1",
    author="zys-chd",
    author_email="yusong_zhang@outlook.com",
    description="A simple and efficient file explorer written in python tkinker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zys-chd/TkinerFileExplorer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)