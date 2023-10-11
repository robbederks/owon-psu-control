import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="owon_psu",
    version="0.0.2",
    author="Robbe Derks",
    author_email="robbe.derks@gmail.com",
    description="Simple Python library for controlling Owon SPE6103 and SPE3103 power supplies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[ 'scpi', 'owon', 'SPE6103', 'SPE3103', 'simple' ],
    url="https://github.com/robbederks/owon-psu-control",
    project_urls = {
      'Source Code': 'https://github.com/robbederks/owon-psu-control',
      'Bug Tracker': 'https://github.com/robbederks/owon-psu-control/issues'
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    install_requires=[
      'pyserial'
    ]
)
