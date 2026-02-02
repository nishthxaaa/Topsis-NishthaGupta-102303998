[![PyPI version][pypi-shield]][pypi-url]
[![License: MIT][license-shield]][license-url]
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

<br />
<p align="center">
  <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998">
    <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TOPSIS-NishthaGupta-102303998</h3>

  <p align="center">
    A comprehensive Python package and Web Service for Multiple Criteria Decision Making (MCDM) using the TOPSIS technique.
    <br />
    <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://pypi.org/project/Topsis-NishthaGupta-102303998/">View PyPI Package</a>
    ·
    <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998/issues">Report Bug</a>
    ·
    <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method. It compares a set of alternatives based on a set of criteria, identifying the alternative that is closest to the ideal solution and farthest from the negative ideal solution.

This project offers a unified solution with three modes of operation:
1.  **CLI Tool**: Run calculations directly from your command line interface.
2.  **Python Library**: A plug-and-play package for your Python scripts.
3.  **Web Service**: A user-friendly Streamlit interface to upload data and get results via email (simulation).

### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Streamlit](https://streamlit.io/)
* [NumPy](https://numpy.org/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.6 or higher
* pip

### Installation

1. **Install via pip (Recommended)**
   The easiest way to use the library is to install it directly from PyPI:
   ```bash
   pip install Topsis-NishthaGupta-102303998
   ```

2. **Clone the Repo (For Web App Usage)**
   If you want to run the Streamlit Web App locally:
   ```bash
   git clone [https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998.git](https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998.git)
   cd Topsis-NishthaGupta-102303998
   pip install -r requirements.txt
   ```

## Usage

### 1. Command Line Interface (CLI)
You can use the package directly from your terminal.

**Syntax:**
```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

**Example:**
```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv
```
*Note: The input file must contain 3 or more columns. The first column is treated as the object/fund name.*

### 2. Python Library
Import the package in your own Python script to perform calculations programmatically.

```python
from Topsis_NishthaGupta_102303998.topsis import topsis

# Define your parameters
input_file = "data.csv"
weights = "1,1,1,1,1"
impacts = "+,+,-,+,+"
output_file = "result.csv"

# Call the function
topsis(input_file, weights, impacts, output_file)
```

### 3. Web Service
Launch the graphical interface to upload files and download results.

```bash
streamlit run app.py
```
* **Step 1:** Upload your `.csv` or `.xlsx` file.
* **Step 2:** Enter weights (comma-separated).
* **Step 3:** Enter impacts (+ or -).
* **Step 4:** View results and download the ranking file.

## Roadmap

- [x] Core TOPSIS Algorithm Implementation
- [x] Command Line Interface (CLI)
- [x] Published to PyPI
- [x] Streamlit Web Application
- [ ] Add visualization (Bar charts for rankings)
- [ ] Live email integration

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Nishtha Gupta - [YourEmail@example.com](mailto:YourEmail@example.com)

Project Link: [https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998](https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998)

[pypi-shield]: https://img.shields.io/pypi/v/Topsis-NishthaGupta-102303998.svg?style=flat-square
[pypi-url]: https://pypi.org/project/Topsis-NishthaGupta-102303998/
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
