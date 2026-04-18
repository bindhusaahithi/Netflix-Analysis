# Netflix Content Analytics Platform

Explore content trends, genre dominance, and global production insights using data analytics on the Netflix Movies and TV Shows dataset.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# Project Overview

This project analyzes the **Netflix Movies and TV Shows dataset** to uncover insights about streaming content trends.

The analysis focuses on understanding:

- How Netflix expanded its content library over time  
- The distribution of Movies vs TV Shows  
- The most popular genres on Netflix  
- Countries producing the most Netflix content  
- Directors contributing the most titles  

Using **Python, Pandas, Matplotlib, and Seaborn**, this project demonstrates how exploratory data analysis can transform raw datasets into meaningful insights.

---

# Why This Analysis Matters

Streaming platforms generate massive volumes of content data.

Analyzing these datasets helps:

- Media analysts understand content growth strategies  
- Studios identify dominant genres  
- Investors analyze global production trends  
- Creators understand market demand  

This project demonstrates how **data analytics can reveal valuable patterns in entertainment datasets**.

---

# Project Objectives

- Analyze the growth of Netflix content over the years  
- Compare Movies vs TV Shows distribution  
- Identify the most popular genres  
- Discover top contributing countries  
- Find directors with the most titles on Netflix  

---

# Tools & Libraries

- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

# Dataset

Netflix Movies & TV Shows dataset.

Source:  
https://www.kaggle.com/datasets/shivamb/netflix-shows

---

# Key Insights

## Content Growth on Netflix

![Content Growth](visuals/content_growth.png)

Netflix content increased significantly after 2015, indicating aggressive platform expansion.

---

## Movies vs TV Shows Distribution

![Movies vs TV Shows](visuals/movies_vs_tvshows.png)

Movies dominate the Netflix catalog, making up the majority of titles.

---

## Top Genres on Netflix

![Top Genres](visuals/top_genres.png)

International Movies and Dramas appear most frequently in the dataset.

---

## Top Countries Producing Netflix Content

![Top Countries](visuals/top_countries.png)

The United States leads content production, followed by India and the United Kingdom.

---

## Top Directors on Netflix

![Top Directors](visuals/top_directors.png)

Several directors contribute multiple titles, showing strong collaborations with Netflix.

---

# Data Analytics Pipeline

The project follows a simple data analytics workflow.

Dataset → Data Cleaning → Exploratory Analysis → Visualization → Insights

---

# Architecture

```mermaid
flowchart LR

A["Netflix Dataset CSV"] --> B["Data Cleaning / Preprocessing (Pandas)"]
B --> C["Exploratory Data Analysis (Python)"]
C --> D["Visualization Layer (Matplotlib / Seaborn)"]
D --> E["Insights & Trend Analysis"]

E --> F["Content Growth Insights"]
E --> G["Genre Distribution"]
E --> H["Country Production Trends"]
E --> I["Top Directors Analysis"]
```

---

# What You Can Do With This Project

### Content Trend Analysis

- Analyze Netflix content growth across years  
- Identify expansion patterns in the streaming platform

### Genre Analysis

- Discover dominant genres on Netflix  
- Explore content category distributions

### Geographic Analysis

- Identify which countries contribute the most titles  
- Analyze global production patterns

### Creator Analysis

- Identify directors producing the most Netflix content

---

# Quick Start

## Prerequisites

Python 3.8+

Install required libraries:

pip install pandas matplotlib seaborn

---

## Clone Repository

git clone https://github.com/bindhusaahithi/Netflix-Analysis.git

cd Netflix-Analysis

---

## Run the Analysis

Open the notebook:

jupyter notebook Netflix_Analysis.ipynb

Run all cells to reproduce the analysis and visualizations.

---

# Project Structure

Netflix-Analysis

├── data  
│   └── netflix_titles.csv  

├── notebooks  
│   └── Netflix_Analysis.ipynb  

├── visuals  
│   ├── content_growth.png  
│   ├── movies_vs_tvshows.png  
│   ├── top_genres.png  
│   ├── top_countries.png  
│   └── top_directors.png  

└── README.md

---

# Future Improvements

Possible extensions of this project:

- Build an **interactive dashboard using Streamlit**  
- Implement a **Netflix recommendation system using machine learning**  
- Perform **sentiment analysis on Netflix reviews**  
- Train a **model to predict popular content categories**

---

# Author

Bindhu Saahithi  

Master's in Data Science  

GitHub: https://github.com/bindhusaahithi

---

# License

MIT License
