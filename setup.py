import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thebrain2dot",
    version="0.0.1",
    author="simoncos",
    author_email="l.z.simon@hotmail.com",
    description="thebrain10 json to dot / graphviz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simoncos/thebrain2dot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
