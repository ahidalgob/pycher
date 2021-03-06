import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pycher",
    version="0.0.6",
    description="Quick desktop python launcher",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ahidalgob/pycher",
    author="Augusto Hidalgo",
    author_email="ahidalgo94@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['pycher'],

    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": [
        "pycher=pycher.__main__:main",
    ]},
)
