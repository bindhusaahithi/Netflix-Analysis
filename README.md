# Netflix Data Analysis

This project explores the Netflix Movies and TV Shows dataset to uncover insights about content trends, genres, countries, and directors using Python.

## Project Objectives

* Analyze the growth of Netflix content over the years
* Compare Movies vs TV Shows distribution
* Identify the most popular genres
* Discover top contributing countries
* Find directors with the most titles

## Tools & Libraries

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## Dataset

Netflix Movies & TV Shows dataset.

## Key Insights

### Content Growth on Netflix

![Content Growth](visuals/content_growth.png)

Netflix content increased significantly after 2015, indicating aggressive platform expansion.

### Movies vs TV Shows Distribution

![Movies vs TV Shows](visuals/movies_vs_tvshows.png)

Movies dominate the Netflix catalog, making up the majority of titles.

### Top Genres on Netflix

![Top Genres](visuals/top_genres.png)

International Movies and Dramas appear most frequently in the dataset.

### Top Countries Producing Netflix Content

![Top Countries](visuals/top_countries.png)

The United States leads content production, followed by India and the United Kingdom.

### Top Directors

![Top Directors](visuals/top_directors.png)

Several directors contribute multiple titles, showing strong collaborations with Netflix.



## Architecture

```mermaid
flowchart LR

A[Netflix Dataset CSV] --> B[Data Cleaning / Preprocessing<br>Python + Pandas]

B --> C[Exploratory Data Analysis<br>Python]

C --> D[Visualization Layer<br>Matplotlib / Seaborn]

D --> E[Insights & Trend Analysis]

E --> F[Business Insights<br>Content Trends]

E --> G[Genre & Country Analysis]

E --> H[Director Analysis]




## Project Structure

Netflix-Analysis
│
├── Data
│ └── netflix_titles.csv
│
├── Notebook
│ └── Netflix_Analysis.ipynb
│
├── visuals
│ ├── content_growth.png
│ ├── movies_vs_tvshows.png
│ ├── top_genres.png
│ ├── top_countries.png
│ ├── top_directors.png
│ └── top_ratings.png
│
└── README.md

