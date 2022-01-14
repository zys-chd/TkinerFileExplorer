# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import setuptools
import os
import requests
import io


with open("README.md", "r") as fh:
    long_description = fh.read()

if os.path.exists("requirements.txt"):
    install_requires = io.open("requirements.txt").read().split("\n")
else:
    install_requires = []

setuptools.setup(
    name="TkinkerFileExplorer",
    version="0.0.3",
    author="zys-chd",
    author_email="yusong_zhang@outlook.com",
    description="A simple and efficient file explorer written in python tkinker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zys-chd/TkinerFileExplorer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=install_requires,
        package_data = {
            # If any package contains *.txt or *.rst files, include them:
            # 'TkinkerFileExplorer': ['source/*.txt', "source/*.json"],
    },
    entry_points={
        'console_scripts': [
            # 'TkinkerFileExplorer = TkinkerFileExplorer.run:main'
        ]
    }
)
