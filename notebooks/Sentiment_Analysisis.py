import pandas as pd
from langdetect import detect
from transformers import pipeline, MarianMTModel, MarianTokenizer

# Load modelspython
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
translation_model_name = "Helsinki-NLP/opus-mt-am-en"
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

# 1. Detect language
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        print(f"[Language Detection Error] Text: {text[:50]} | Error: {e}")
        return "unknown"

# 2. Translate Amharic to English
def translate_amharic(text):
    try:
        inputs = translation_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = translation_model.generate(**inputs)
        return translation_tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        print(f"[Translation Error] Text: {text[:50]} | Error: {e}")
        return text  # fallback to original

# 3. Perform sentiment analysis
def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(text)[0]
        return result['label'], result['score']
    except Exception as e:
        print(f"[Sentiment Error] Text: {text[:50]} | Error: {e}")
        return "UNKNOWN", 0.0

# Load your reviews dataset
df = pd.read_csv("data/cleaned_reviews_all.csv")  # replace with actual path if needed

# Apply pipeline
df['language'] = df['review'].apply(detect_language)
df['translated_review'] = df.apply(
    lambda x: translate_amharic(x['review']) if x['language'] == 'am' else x['review'], axis=1
)
df[['sentiment', 'sentiment_score']] = df['translated_review'].apply(
    lambda x: pd.Series(analyze_sentiment(x))
)

# Save final result
df.to_csv("data/reviews_with_sentiment.csv", index=False)
print("✅ Sentiment analysis complete. File saved to 'data/reviews_with_sentiment.csv'")
 