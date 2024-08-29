# Workshop 1 - ETL Process for Global Talent Recruitment Dataset

This project aims to provide a solution for Workshop 1, where an ETL (Extract, Transform, Load) process is applied to a dataset about global talent recruitment.

## Tools Used
- Python <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px">
- Poetry <img src="https://python-poetry.org/images/logo-origami.svg" alt="Poetry" width="21px" height="21px">
- Jupyter Notebooks <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- GeoJSON <img src="https://cdn-icons-png.flaticon.com/512/11570/11570271.png" alt="Json" width="21px" height="21px">
- Postgres <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">
- Power BI <img src="https://1000logos.net/wp-content/uploads/2022/08/Microsoft-Power-BI-Logo.png" alt="PowerBI" width="30px" height="21px">
- SQLAlchemy <img src="https://quintagroup.com/cms/python/images/sqlalchemy-logo.png/@@images/eca35254-a2db-47a8-850b-2678f7f8bc09.png" alt="SQLalchemy" width="50px" height="21px">

---
# Requirements

 - Install Python: [Python Downloads](https://www.python.org/downloads/)
 - Install Poetry: [Poetry Downloads](https://python-poetry.org/docs/#installing-with-the-official-installer)
 - Install PostgreSQL: [PostgreSQL Downloads](https://www.postgresql.org/download/)
 - Install Power BI: [Install Power BI Desktop](https://www.microsoft.com/en-us/download/details.aspx?id=58494)

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