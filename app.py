import pickle
import streamlit as st
import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the Random Forest model
with open('rf_model_final.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

st.title('Hotel Review Sentiment Analysis')

def predict_sentiment(review):
    # Clean the review
    stop_words = set(stopwords.words('english'))
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = word_tokenize(review)
    review = [word for word in review if not word in stop_words]

    # TF-IDF Vectorize the review
    review = tfidf_vectorizer.transform([' '.join(review)])

    # Predict the sentiment
    prediction = model.predict(review)[0]
    return prediction

def main():

  review_text = st.text_area('Enter your review', '')

  if st.button('Predict'):
    sentiment = predict_sentiment(review_text)
    if sentiment==2:
      st.write("Positive Review")
    elif sentiment==1:
      st.write("Neutral Review")
    else:
      st.write("Negative Review")

if __name__=="__main__":
    main()
    