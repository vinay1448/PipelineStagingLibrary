import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="custom-pipeline-stages-manager",
    version="0.1.0",
    author="Vinay Sriram Iyer",
    author_email="x23203595@student.ncirl.ie",
    description="A package for managing custom pipeline stages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x23203595/PipelineStagingLibrary.git",
    packages=setuptools.find_packages(),
    install_requires=['boto3'],
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)