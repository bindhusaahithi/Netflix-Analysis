import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Netflix EDA Dashboard",
    page_icon="🎬",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .hero-banner {
        background: linear-gradient(135deg, #E50914 0%, #B20710 50%, #221F1F 100%);
        padding: 40px 30px;
        border-radius: 16px;
        margin-bottom: 24px;
        text-align: center;
    }
    .hero-title {
        color: white;
        font-size: 2.6em;
        font-weight: 900;
        margin: 0;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        color: rgba(255,255,255,0.8);
        font-size: 1.1em;
        margin-top: 8px;
    }
    .hero-links a {
        color: rgba(255,255,255,0.9);
        text-decoration: none;
        margin: 0 12px;
        font-size: 0.95em;
        border-bottom: 1px solid rgba(255,255,255,0.4);
    }

    .stats-bar {
        display: flex;
        justify-content: space-around;
        background: #1a1a1a;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 24px;
        border: 1px solid #333;
    }
    .stat-item { text-align: center; }
    .stat-number {
        font-size: 1.9em;
        font-weight: 800;
        color: #E50914;
        display: block;
    }
    .stat-label {
        font-size: 0.75em;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .section-header {
        font-size: 1.3em;
        font-weight: 700;
        color: #eee;
        margin: 28px 0 12px 0;
        padding-bottom: 8px;
        border-bottom: 2px solid #E50914;
    }

    .filter-box {
        background: #1a1a1a;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #333;
        margin-bottom: 20px;
    }

    .insight-card {
        background: #1a1a1a;
        border-left: 4px solid #E50914;
        border-radius: 8px;
        padding: 14px 18px;
        margin: 8px 0;
        color: #ccc;
        font-size: 0.95em;
    }

    .footer {
        text-align: center;
        color: #666;
        font-size: 0.85em;
        padding: 20px 0 10px 0;
    }
    .footer a { color: #E50914; text-decoration: none; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("Data/netflix_titles.csv")
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month_name()
    return df

df = load_data()

# ── Hero Banner ───────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <p class="hero-title">🎬 Netflix Content Analysis Dashboard</p>
    <p class="hero-subtitle">Exploratory Data Analysis · 8,800+ Titles · Movies & TV Shows</p>
    <div class="hero-links" style="margin-top:14px;">
        <a href="https://github.com/bindhusaahithi" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/bindhu-saahithi-naralashetty-yogendranath/" target="_blank">LinkedIn</a>
        <a href="https://www.kaggle.com/bindhusaahithi" target="_blank">Kaggle</a>
        <a href="https://github.com/bindhusaahithi/Netflix-Analysis" target="_blank">View Code</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Stats Bar ─────────────────────────────────────────────────
total    = len(df)
movies   = len(df[df["type"] == "Movie"])
shows    = len(df[df["type"] == "TV Show"])
countries = df["country"].dropna().str.split(", ").explode().nunique()

st.markdown(f"""
<div class="stats-bar">
    <div class="stat-item">
        <span class="stat-number">{total:,}</span>
        <span class="stat-label">Total Titles</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">{movies:,}</span>
        <span class="stat-label">Movies</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">{shows:,}</span>
        <span class="stat-label">TV Shows</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">{countries}</span>
        <span class="stat-label">Countries</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Filters ───────────────────────────────────────────────────
st.markdown('<p class="section-header">🎛️ Filter Content</p>', unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    content_type = st.selectbox(
        "Content Type",
        ["All", "Movie", "TV Show"]
    )

with col_f2:
    all_ratings  = ["All"] + sorted(df["rating"].dropna().unique().tolist())
    rating_filter = st.selectbox("Rating", all_ratings)

with col_f3:
    year_min = int(df["year_added"].dropna().min())
    year_max = int(df["year_added"].dropna().max())
    year_range = st.slider("Year Added", year_min, year_max, (2015, year_max))

# Apply filters
filtered = df.copy()
if content_type != "All":
    filtered = filtered[filtered["type"] == content_type]
if rating_filter != "All":
    filtered = filtered[filtered["rating"] == rating_filter]
filtered = filtered[
    (filtered["year_added"] >= year_range[0]) &
    (filtered["year_added"] <= year_range[1])
]

st.markdown(f"**Showing {len(filtered):,} titles** matching your filters")

st.markdown("---")

# ── Charts ────────────────────────────────────────────────────
sns.set_theme(style="darkgrid")
NETFLIX_RED = "#E50914"

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.markdown('<p class="section-header">🎭 Movies vs TV Shows</p>', unsafe_allow_html=True)
    type_counts = filtered["type"].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    colors = ["#E50914", "#B20710"]
    wedges, texts, autotexts = ax.pie(
        type_counts.values,
        labels=type_counts.index,
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
        textprops={"color": "white", "fontsize": 12}
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontsize(11)
    ax.set_title("Content Type Distribution", color="white", fontsize=13, pad=15)
    st.pyplot(fig)
    plt.close()

with col2:
    st.markdown('<p class="section-header">🌍 Top 10 Countries</p>', unsafe_allow_html=True)
    country_data = filtered.dropna(subset=["country"]).copy()
    country_data["country"] = country_data["country"].str.split(", ")
    country_exploded = country_data.explode("country")
    top_countries = country_exploded["country"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    bars = ax.barh(top_countries.index[::-1], top_countries.values[::-1], color=NETFLIX_RED)
    ax.set_xlabel("Number of Titles", color="white")
    ax.set_title("Top Countries Producing Content", color="white", fontsize=13)
    ax.tick_params(colors="white")
    ax.spines["bottom"].set_color("#444")
    ax.spines["left"].set_color("#444")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for bar, val in zip(bars, top_countries.values[::-1]):
        ax.text(val + 10, bar.get_y() + bar.get_height()/2,
                str(val), va="center", color="white", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Row 2
col3, col4 = st.columns(2)

with col3:
    st.markdown('<p class="section-header">📅 Content Added Over Time</p>', unsafe_allow_html=True)
    year_counts = filtered["year_added"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    ax.fill_between(year_counts.index, year_counts.values, alpha=0.3, color=NETFLIX_RED)
    ax.plot(year_counts.index, year_counts.values, color=NETFLIX_RED, linewidth=2.5, marker="o", markersize=5)
    ax.set_xlabel("Year", color="white")
    ax.set_ylabel("Titles Added", color="white")
    ax.set_title("Netflix Content Growth", color="white", fontsize=13)
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col4:
    st.markdown('<p class="section-header">⭐ Top Ratings</p>', unsafe_allow_html=True)
    rating_counts = filtered["rating"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    palette = sns.color_palette("Reds_r", len(rating_counts))
    bars = ax.barh(rating_counts.index[::-1], rating_counts.values[::-1], color=palette)
    ax.set_xlabel("Number of Titles", color="white")
    ax.set_title("Content Ratings Distribution", color="white", fontsize=13)
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444")
    for bar, val in zip(bars, rating_counts.values[::-1]):
        ax.text(val + 5, bar.get_y() + bar.get_height()/2,
                str(val), va="center", color="white", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Row 3
col5, col6 = st.columns(2)

with col5:
    st.markdown('<p class="section-header">🎭 Top Genres</p>', unsafe_allow_html=True)
    genre_data = filtered.dropna(subset=["listed_in"]).copy()
    genre_data["listed_in"] = genre_data["listed_in"].str.split(", ")
    genre_exploded = genre_data.explode("listed_in")
    top_genres = genre_exploded["listed_in"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    bars = ax.barh(top_genres.index[::-1], top_genres.values[::-1],
                   color=sns.color_palette("magma", len(top_genres)))
    ax.set_xlabel("Number of Titles", color="white")
    ax.set_title("Top 10 Genres on Netflix", color="white", fontsize=13)
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444")
    for bar, val in zip(bars, top_genres.values[::-1]):
        ax.text(val + 5, bar.get_y() + bar.get_height()/2,
                str(val), va="center", color="white", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col6:
    st.markdown('<p class="section-header">🎬 Top Directors</p>', unsafe_allow_html=True)
    dir_data = filtered.dropna(subset=["director"]).copy()
    dir_data["director"] = dir_data["director"].str.split(", ")
    dir_exploded = dir_data.explode("director")
    top_dirs = dir_exploded["director"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor("#111")
    ax.set_facecolor("#111")
    bars = ax.barh(top_dirs.index[::-1], top_dirs.values[::-1],
                   color=sns.color_palette("viridis", len(top_dirs)))
    ax.set_xlabel("Number of Titles", color="white")
    ax.set_title("Most Prolific Directors", color="white", fontsize=13)
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444")
    for bar, val in zip(bars, top_dirs.values[::-1]):
        ax.text(val + 0.1, bar.get_y() + bar.get_height()/2,
                str(val), va="center", color="white", fontsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# ── Key Insights ──────────────────────────────────────────────
st.markdown('<p class="section-header">💡 Key Insights</p>', unsafe_allow_html=True)

movies_pct = round(movies / total * 100, 1)
top_country = df["country"].dropna().str.split(", ").explode().value_counts().index[0]
peak_year   = int(df["year_added"].value_counts().idxmax())
top_rating  = df["rating"].value_counts().index[0]

insights = [
    f"🎬 <b>{movies_pct}%</b> of Netflix content is Movies, with the rest being TV Shows",
    f"🌍 <b>{top_country}</b> produces the most Netflix content globally",
    f"📅 Netflix content additions peaked in <b>{peak_year}</b>",
    f"⭐ <b>{top_rating}</b> is the most common content rating on Netflix",
    f"🎭 <b>International Movies</b> is the most popular genre category",
]

for insight in insights:
    st.markdown(f'<div class="insight-card">{insight}</div>', unsafe_allow_html=True)

# ── Search ────────────────────────────────────────────────────
st.markdown('<p class="section-header">🔍 Search Titles</p>', unsafe_allow_html=True)
search = st.text_input("Search by title, director, or cast", placeholder="e.g. Rajiv Chilaka")

if search:
    mask = (
        df["title"].str.contains(search, case=False, na=False) |
        df["director"].str.contains(search, case=False, na=False) |
        df["cast"].str.contains(search, case=False, na=False)
    )
    results = df[mask][["title", "type", "country", "release_year", "rating", "listed_in"]].head(20)
    st.dataframe(results, use_container_width=True)
    st.caption(f"Found {mask.sum()} results")

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built by <a href="https://github.com/bindhusaahithi">Bindhu Saahithi</a> ·
    <a href="https://www.linkedin.com/in/bindhu-saahithi-naralashetty-yogendranath/">LinkedIn</a> ·
    <a href="https://www.kaggle.com/bindhusaahithi">Kaggle</a> ·
    <a href="https://github.com/bindhusaahithi/Netflix-Analysis">View on GitHub</a>
    <br>Netflix EDA Dashboard · 8,800+ titles analyzed
</div>
""", unsafe_allow_html=True)
