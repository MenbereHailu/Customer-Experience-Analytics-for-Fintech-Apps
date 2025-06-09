from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime
def scrape_reviews(app_id, bank_name, lang='en', country='us', num_reviews=5000):
    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=num_reviews,
        filter_score_with=None
    )
    df = pd.DataFrame(result)
    df = df[['content', 'score', 'at']]  # Review text, rating, date
    df.rename(columns={'content': 'review', 'score': 'rating', 'at': 'date'}, inplace=True)
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

if __name__ == '__main__':
    apps = {
        'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
        'Bank of Abyssinia': 'com.boa.boaMobileBanking',
        'Dashen Bank': 'com.dashen.dashensuperapp'
    }

    all_reviews = []
    for bank, app_id in apps.items():
        df = scrape_reviews(app_id, bank, num_reviews=5000)
        all_reviews.append(df)

    combined_df = pd.concat(all_reviews, ignore_index=True)
    combined_df.drop_duplicates(subset=['review', 'date', 'bank'], inplace=True)
    combined_df.to_csv('data/cleaned_reviews_all.csv', index=False)
    print(f"✅ Saved {combined_df.shape[0]} cleaned reviews.")