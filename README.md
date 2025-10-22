# DATA PRE-PROCESSING in Python

This repo is part of me learning the basics of data preprocessing in Python.
It has three simple scripts to practice **Ordinal Encoding**, **One-Hot Encoding**, and **Imputation** - all done manually using **Python, Pandas, and NumPy**.

The idea was to understand *how these things actually work* instead of just calling built-in functions like `get_dummies()` or `scikit-learn encoders`.

Basically, I wanted to get a hands-on feel for preprocessing before diving into real ML models.

## Files

| File               | What it does                                                                                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------------------|
| `DATA`             | A small house pricing dataset                                                                                       |
| `ENCODIND`         | Ordinal_ENCODING.py : Turns ordered categories (like Small, Medium, Large) into numbers using a manual mapping.     |
|                    | OneHot_ENCODING.py  : Makes binary columns for each category using loops and simple NumPy logic.                    |
| `IMPUTATION`       | Fills missing values using mea for mode, all done manually without high-level functions.                            |



## What I Learned

* The difference between **ordinal** and **one-hot encoding**.
* How to handle missing data manually.
* Importance of PRE-PROCESSING the data in ML models.
* Improved comfort with Pandas and NumPy.


This repo is just a simple record of what I tried and learned - nothing fancy.
