# 📁 Task 1: Setup, GitHub Integration & Exploratory Data Analysis (EDA)

## 🎯 Objective

This task focuses on:
- Setting up a reproducible Python data science environment
- Initializing Git and GitHub for version control
- Implementing CI with GitHub Actions
- Performing Exploratory Data Analysis (EDA) on financial news headlines

---

## ✅ Task Checklist

### 1. Setup & Version Control
- [x] Create GitHub repository
- [x] Create and switch to a new branch: `task-1`
- [x] Setup Python virtual environment
- [x] Add `requirements.txt` with required libraries (e.g., `pandas`, `seaborn`, `nltk`, etc.)
- [x] Add `.gitignore` to exclude unnecessary files
- [x] Create folder structure (see below)
- [x] Add initial `README.md` file
- [x] Setup GitHub Actions for Continuous Integration (CI)

### 2. Exploratory Data Analysis (EDA)
- [x] Load and inspect news dataset
- [x] Analyze:
  - Headline lengths
  - Article counts by publisher
  - Article counts by date
  - Publishing frequency over time
  - Hour-of-day publishing trends
  - Publisher domain distribution
- [x] Visualize results using bar charts, histograms, and line plots

---

## 📁 Folder Structure

<pre> ``` ├── .github/ │ └── workflows/ │ └── unittests.yml # GitHub Action for CI (unit test runner) ├── data/ │ └── news_data.csv # Raw news dataset ├── notebooks/ │ └── 01_eda_news.ipynb # Jupyter Notebook for EDA ├── scripts/ │ └── data_loader.py # Helper script to load/clean data ├── tests/ │ └── test_loader.py # Unit tests for data loading ├── requirements.txt # Python dependencies ├── .gitignore # Files/folders to ignore in Git ├── README.md # Project overview (this file) ``` </pre>


---

## 📦 Required Libraries

Install all dependencies with:

```bash
pip install -r requirements.txt
```
Example packages:

- pandas
- numpy
- matplotlib
- seaborn
- nltk
- pytest
- jupyter

📊 Outputs
Key plots and summaries will be stored in outputs/ (optional).


# 📊 Task-2 : Stock Price Analysis and Technical Indicator Dashboard

## 🧾 Project Overview
This project involves loading and analyzing stock price data using Python, TA-Lib, and PyNance to calculate key financial indicators and visualize insights. The goal is to prepare clean data, apply technical analysis, and create an interactive dashboard-ready dataset for stock market insights.

---

## ✅ Features
- Load and clean historical stock price data (Open, High, Low, Close, Volume)
- Compute technical indicators using **TA-Lib**:
  - Moving Averages (SMA, EMA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
- Extract financial metrics using **PyNance**
- Generate visualizations for trend analysis and signal interpretation
- Follow best practices in version control using Git and GitHub



---

## 🔧 Tools & Libraries
- Python (Pandas, Matplotlib, Seaborn)
- TA-Lib (Technical Analysis Library)
- PyNance (Financial metrics)
- Git & GitHub

---

## 📌 Workflow Summary
- Merged essential changes from `task-1` into `main` using a **Pull Request**
- Created a new development branch `task-2` for ongoing dashboard development
- Committed all progress with descriptive messages for clear version tracking

---

## 📈 Key KPIs
- **Proactivity**: Used external resources and documentation to implement tools
- **Accuracy**: Verified indicators against expected trends
- **Completeness**: Full pipeline from data prep to indicator calculation and visualization

---

## 📊 Sample Output
Visualizations include:
- Price with SMA/EMA overlays
- RSI and MACD signal plots
- Volume distribution and trendlines

---

#  📰📈 Task 3: News Sentiment vs Stock Price Movement Analysis

## 🧾 Project Overview
This project explores the relationship between news sentiment and stock price movements. By aligning financial market data with sentiment analysis of news headlines, we aim to identify potential correlations and assess the predictive value of media tone on stock performance.

---

## ✅ Features

- **Date Alignment**: Normalized and aligned news and stock datasets by trading dates to ensure analytical consistency.
- **Sentiment Analysis**: Used NLP tools (TextBlob, NLTK) to assign sentiment scores (positive, neutral, negative) to news headlines.
- **Stock Return Calculation**: Computed daily stock return percentages based on closing prices.
- **Correlation Analysis**: Performed statistical correlation analysis between daily average sentiment scores and daily stock returns using Pearson's correlation coefficient.

---

## 🔧 Tools & Libraries

- Python (Pandas, NumPy)
- NLP: NLTK, TextBlob
- Matplotlib/Seaborn for visualization
- Git & GitHub for version control

---

---

## 🔄 Workflow Summary

- Merged updates from `task-2` into `main` via a **Pull Request**
- Created new development branch `task-3` for ongoing sentiment-stock analysis
- All commits use descriptive messages documenting tasks completed

---

## 📊 KPIs

- **Proactivity**: Leveraged and shared references to implement sentiment scoring and correlation methods
- **Sentiment Analysis**: Headlines successfully scored using basic NLP sentiment tools
- **Correlation Strength**: Pearson correlation coefficient calculated to assess strength and direction of sentiment-price relationship

---

## 🔬 Methodology

1. **Normalize Dates**
   - Converted timestamps and ensured news and stock data aligned by trading days.

2. **Sentiment Scoring**
   - Applied TextBlob polarity scores to quantify the tone of each headline.
   - Aggregated sentiment scores to daily averages.

3. **Calculate Daily Returns**
   - Used percent change in closing stock prices to represent daily movements.

4. **Correlation**
   - Performed Pearson correlation between aggregated sentiment and returns to analyze relationships.



## 🖊️ Author
- Maintained by Menbere Hailu
- 📧 menberehailu.w@gmail.com
- 🌐 GitHub: MenbereHailu