# OOP_LAB_3

## Lab Overview

This project is an Object-Oriented Programming (OOP) exercise demonstrating how to handle and process structured data using Python classes.

---

## Project Structure

The required file structure for this project is minimal:

OOP_LAB_3/ ├── data_processor.py #main program
           └── Cities.csv 
           └── Countries.csv


## Design Overview

### 1. `DataLoader` Class
* **Responsibility:** Handles file I/O operations. It takes a file name and uses `csv.DictReader` to load data into a list of dictionaries, where column headers become dictionary keys.
* **Robustness:** Uses `pathlib.Path` for reliable file path resolution across different operating systems.

### 2. `DB` Class
* **Responsibility:** Stores the dictionary of tables object used in the project.

| Method | Purpose | Key Feature |
| :--- | :--- | :--- |
| `insert(table)` | Adds a table loaded from `load_csv` to DB dictionary.  | Returns an updated version of DB dictionary. |
| `search(key)` | Create new table with only data with that key. | Returns new table object. |

### 3. `Table` Class
* **Responsibility:** Stores the list of dictionaries (the data) and provides methods for data manipulation.

| Method | Purpose | Key Feature |
| :--- | :--- | :--- |
| `filter(condition)` | Selects a subset of rows based on a provided `lambda` function. | Returns a **new** `Table` object. |
| `aggregate(function, key)` | Calculates a summary value (e.g., average, count, max) on a specific column (`key`). | Attempts automatic type conversion to `float` for numerical analysis. |
| `join(table, key)` | Combines two tables with the same key together. | Returns new table object. |


---

## How to Use

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are required beyond the standard library modules (`csv` and `pathlib`).

### 1. Setup

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ratamon2606-create/cities-repo.git