# Workshop 1 - ETL Process for Global Talent Recruitment Dataset

This project aims to provide a solution for Workshop 1, where an ETL (Extract, Transform, Load) process is applied to a dataset about global talent recruitment.

## Tools Used
- Python
- Poetry
- Jupyter Notebooks
- GeoJSON
- Postgres
- Power BI

---
# Project Setup

### Clone the Repository

First, you need to clone the repository:

```bash
git clone https://github.com/sebas1193/Workshop_001.git
```

---
### Poetry Setup

Before starting, make sure you have Poetry installed. Once installed, activate the Poetry environment by running the following command in the project's root directory:

```bash
poetry shell
```

Next, install all the dependencies required for the project:

```bash
poetry install
```

---
### Running Jupyter Notebooks

To execute the notebooks, you'll need to start the Jupyter server. Run the following command from the CLI:

bash

Copiar código

```bash
jupyter notebook
```

This command will open a new window in your web browser, where you can interact with and execute the project's notebooks.

---
### GeoJSON File

The GeoJSON file used in this project contains a map of the world, where each country is labeled with its name in various languages. This file is primarily used as a reference to normalize country names, facilitating the creation of visualizations in the dashboard.

---
### ETL Process Overview

The dataset was initially loaded in a raw format into a database. The data was then extracted, transformed to meet the project's requirements, and finally loaded into a clean format, ready to be consumed by the dashboard. This completes the ETL process for the dataset