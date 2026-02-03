[![PyPI version][pypi-shield]][pypi-url]
[![License: MIT][license-shield]][license-url]
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

<br />
<p align="center">
  <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998">
    <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TOPSIS-NishthaGupta-102303998</h3>

  <p align="center">
    A comprehensive Python package and Web Service for Multiple Criteria Decision Making (MCDM) using the TOPSIS technique.
    <br />
    <a href="https://pypi.org/project/Topsis-NishthaGupta-102303998/"><strong>View PyPI Package »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998/issues">Report Bug</a>
    ·
    <a href="https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998/issues">Request Feature</a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#input--output">Input / Output</a></li>
    <li><a href="#live-link">Live Link</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Description

**TOPSIS-NishthaGupta-102303998** is a Python library and web application designed to solve Multiple Criteria Decision Making (MCDM) problems. It implements the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) algorithm, which ranks alternatives based on their distance from an ideal best solution and an ideal worst solution.

This project offers a unified solution with three modes:
1.  **CLI Tool**: For quick terminal-based calculations.
2.  **Python Library**: For integration into data science scripts.
3.  **Web Service**: A deployed Streamlit app for easy user access.

## Methodology

The algorithm generally follows these steps:
1.  **Normalization**: Convert the decision matrix to a normalized scale.
2.  **Weighting**: Apply user-defined weights to the criteria.
3.  **Ideal Solutions**: Determine the Ideal Best ($V^+$) and Ideal Worst ($V^-$) values.
4.  **Separation Measures**: Calculate the Euclidean distance of each alternative from $V^+$ and $V^-$.
5.  **Performance Score**: Compute the relative closeness to the ideal solution.
6.  **Ranking**: Rank alternatives based on the performance score (descending).

## Input / Output

### Input
The program requires a CSV or Excel file with the following constraints:
* **Column 1**: Object Name (e.g., Fund Name, Model Name).
* **Columns 2 to N**: Numeric values for criteria.
* **Weights**: Comma-separated integers (e.g., `1,1,1,2`).
* **Impacts**: Comma-separated signs `+` (beneficial) or `-` (non-beneficial).

### Output
The output is a CSV file containing:
* All original columns.
* **Topsis Score**: The calculated score.
* **Rank**: The final rank of the alternative.

## Live Link

Access the live application here:
[**Launch Web App**](https://topsis-nishthagupta-102303998.streamlit.app/)

*Note: The application is hosted on Streamlit Cloud.*

## Screenshots

### Interface View 1
![App Screenshot 1](Screenshot(1).png)

### Interface View 2
![App Screenshot 2](Screenshot(2).png)

## Installation

To install the library, run the following command:

```bash
pip install Topsis-NishthaGupta-102303998
```
## Run the Web App Locally

```bash
git clone https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998.git
cd Topsis-NishthaGupta-102303998
pip install -r requirements.txt
streamlit run app.py
```

---

## Usage

### 1. Command Line Interface (CLI)

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

**Example:**

```bash
topsis data.csv "1,1,1,1" "+,-,+,+" result.csv
```

---

### 2. Python Library

```python
from Topsis_NishthaGupta_102303998.topsis import topsis

# topsis(input_filename, weights, impacts, output_filename)
topsis("data.csv", "1,1,1,1", "+,-,+,+", "result.csv")
```

---

## License

Distributed under the **MIT License**.  
See the `LICENSE` file for more information.

---

## Contact

**Nishtha Gupta**  
📧 nishtha19gupta@gmail.com  

🔗 Project Link:  
https://github.com/nishthxaaa/Topsis-NishthaGupta-102303998


[pypi-shield]: https://img.shields.io/pypi/v/Topsis-NishthaGupta-102303998.svg?style=flat-square
[pypi-url]: https://pypi.org/project/Topsis-NishthaGupta-102303998/
[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
