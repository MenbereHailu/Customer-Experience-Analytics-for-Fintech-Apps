# Mobile Banking App Review Analysis – Task 1

## 🧾 Overview

This repository is part of a consulting simulation challenge by Omega Consultancy. The goal is to analyze customer satisfaction with mobile banking apps from three major Ethiopian banks by scraping Google Play Store reviews.

This section (Task 1) focuses on:

- Scraping 400+ reviews per bank.
- Cleaning and preprocessing the data.
- Saving the data for further sentiment and thematic analysis.

---

## 🏦 Targeted Bank Apps

| Bank                        | Google Play App ID                     |
|----------------------------|----------------------------------------|
| Commercial Bank of Ethiopia | `com.combanketh.mobilebanking`         |
| Bank of Abyssinia           | `com.boa.boaMobileBanking`             |
| Dashen Bank                 | `com.dashen.dashensuperapp`            |

---

## 🧪 Scraping Methodology

- **Tool used**: [`google-play-scraper`](https://pypi.org/project/google-play-scraper/)
- **Language**: Python 3
- **Data Collected**:
  - Review text
  - Rating (1–5 stars)
  - Review date
  - Bank name
  - Source (`Google Play`)

---

## 🧹 Preprocessing Steps

1. Removed duplicate reviews.
2. Normalized the review date to `YYYY-MM-DD` format.
3. Appended metadata columns for `bank` and `source`.
4. Ensured all reviews have valid content and ratings.
5. Combined all reviews into a single CSV.

---

## 📂 Output

- ✅ `data/cleaned_reviews_all.csv` — contains cleaned reviews from all 3 banks.
- Structure:

| review | rating | date | bank | source |
|--------|--------|------|------|--------|

---

## 💡 How to Run Locally

```bash
pip install -r requirements.txt
python scripts/scrape_reviews.py
