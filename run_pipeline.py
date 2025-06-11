# run_pipeline.py

import pandas as pd
from scripts.pipeline_utils import clean_text, lemmatize
from scripts.sentiment_analysis import get_sentiment
from scripts.thematic_analysis import extract_keywords, map_keywords_to_themes

# Load your review dataset
df = pd.read_csv("data/cleaned_reviews_all.csv")

# Step 1: Preprocessing
print("Cleaning and lemmatizing text...")
df['clean_text'] = df['review_text'].apply(clean_text).apply(lemmatize)

# Step 2: Sentiment Analysis
print("Running sentiment analysis...")
df = get_sentiment(df, text_col='clean_text')

# Step 3: Keyword Extraction
print("Extracting keywords...")
df = extract_keywords(df, text_col='clean_text')

# Step 4: Map Keywords to Themes
print("Mapping keywords to themes...")
df = map_keywords_to_themes(df)

# Save output
print("Saving results...")
df.to_csv("outputs/full_output.csv", index=False)

print("✅ Pipeline complete. Output saved to outputs/full_output.csv")
