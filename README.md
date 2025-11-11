# OOP_LAB_2

## Lab Overview

This project is an Object-Oriented Programming (OOP) exercise demonstrating how to handle and process structured data using Python classes. The goal is to encapsulate data manipulation logic—loading, filtering, and aggregation—within dedicated classes, simulating the functionality of database queries or data frames (like Pandas).

Key OOP principles demonstrated:
* **Encapsulation:** Data and methods are bundled together within the `DataLoader` and `Table` classes.
* **Method Chaining:** The `.filter()` method returns a new `Table` instance, allowing operations to be chained (e.g., `table.filter(...).aggregate(...)`).

---

## Project Structure

The required file structure for this project is minimal:

OOP_LAB_2/ ├── data_processor.py # Contains DataLoader and Table classes, and example usage script └── Cities.csv # The required dataset for the examples


### Data Schema (`Cities.csv`)

The script requires a CSV file with at least the following headers:

| Header | Type | Description |
| :--- | :--- | :--- |
| `city` | String | Name of the city |
| `country` | String | Country name |
| `temperature` | Numeric | Average annual temperature (°C) |
| `population` | Numeric | Population (optional) |

---

## Design Overview

### 1. `DataLoader` Class
* **Responsibility:** Handles file I/O operations. It takes a file name and uses `csv.DictReader` to load data into a list of dictionaries, where column headers become dictionary keys.
* **Robustness:** Uses `pathlib.Path` for reliable file path resolution across different operating systems.

### 2. `Table` Class
* **Responsibility:** Stores the list of dictionaries (the data) and provides methods for data manipulation.

| Method | Purpose | Key Feature |
| :--- | :--- | :--- |
| `filter(condition)` | Selects a subset of rows based on a provided `lambda` function. | Returns a **new** `Table` object. |
| `aggregate(function, key)` | Calculates a summary value (e.g., average, count, max) on a specific column (`key`). | Attempts automatic type conversion to `float` for numerical analysis. |

---

## How to Use

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are required beyond the standard library modules (`csv` and `pathlib`).

### 1. Setup

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ratamon2606-create/cities-repo.git
cd OOP_LAB_2