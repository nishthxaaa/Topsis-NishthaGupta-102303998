from setuptools import setup, find_packages
import os

# Read the User Manual from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis-NishthaGupta-102303998",            # <--- CHANGE THIS
    version="1.0.0",
    author="Nishtha Gupta",                        # <--- CHANGE THIS
    author_email="ngupta2_be23@thapar.edu",     # <--- CHANGE THIS
    description="A Python package for implementing TOPSIS technique.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nishthxaaa/topsis",   # <--- OPTIONAL (Can be empty)
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'topsis=Topsis_NishthaGupta_102303998.topsis:main',      # <--- CHANGE '1020033' to your folder name
        ],
    },
)