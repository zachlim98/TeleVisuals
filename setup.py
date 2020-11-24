import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TeleVisuals-pkg",
    version="0.0.2",
    author="Zachary Lim",
    author_email="contact@nosparechange.com",
    description="A package to help you visualize exports from telegram chats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zachlim98/TeleVisuals",
    packages=setuptools.find_packages(),
    install_requires=['pandas','plotly.express'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)