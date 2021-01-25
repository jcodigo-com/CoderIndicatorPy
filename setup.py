import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Coder Indicator py",
    version="1.0.0",
    author="Pedro Jesús Guzman Ramos",
    author_email="pedrojesusguzmanramos@gmail.com",
    description="A library write in Python to send notificator and push register to Android device this proyect is in construction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jcodigo.com",
    packages=['coderindicatorpy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)