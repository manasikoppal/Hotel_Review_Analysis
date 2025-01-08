# Hotel_Review_Analysis
- Created a tool which predicts customer review and ratings based on the services they recieve.
- Exploratory Data Analysis and pre-processing is done on the 20,000 data.
- Sentiment Analysis is done to evaluate the Sentiment of textual data.
- build different models to see which one provides the best accuracy to be deployed.

  
Business Objective:
The dataset consist of 20,000 hotel reviews and ratings which explores how travellers articulate postive and negative experiences.The goal is to pinpoint the attributes influencing the selection of hotels.This analysis enables managers to refine specific aspects, enhancing the brand's image. It focuses on identifying the factors behind positive reviews, helping hoteliers strategically improve guest satisfaction.


![rm](https://github.com/user-attachments/assets/a6a30701-332c-4e0e-836b-96f495d23b97)


Exploratory data Analysis:
It is done to understand the potential insights hidden in the data.
![rm1](https://github.com/user-attachments/assets/228e1e7f-ddc9-4cb2-a3d8-5b7182997002)


In the analysis of 20,000 hotel reviews, we explored linguistic features like stop word counts, hashtag usage, and uppercase letters to better understand the tone and sentiments in the text. During text cleaning, phrases like 'No Negative' and 'No Positive' were removed to simplify sentiment analysis. We also used part-of-speech tagging, supported by the WordNet database, to classify words like nouns and verbs, giving us deeper insights into the language structure of the reviews.


Sentiment Analysis


![rm2](https://github.com/user-attachments/assets/4ab71d2f-9938-463a-ba93-c4a8f23d903b)

Using the SentimentIntensityAnalyzer from the NLTK library, we analyzed the sentiment of text in the "Review_clean" column of the DataFrame. It generated positive, negative, neutral, and compound scores, which were added as new columns, giving detailed sentiment insights for each review.

The feature Engineering process is done to utilize data resampling techniques to ensure balanced representaion of both postive and negative reviews to promote effective model training.


![rm3](https://github.com/user-attachments/assets/35ff63f1-e592-4c03-bd29-cf52dc79c0c0)

By splitting the data into training and testing set we build the models and compare the accuracy score.

After Comparing different models it was observed that Random forest model exhibited the highest accuracy score.


The deployemnet is done using Streamlit.
The out of the project :

![rm4](https://github.com/user-attachments/assets/0067206c-08d2-4590-bb43-186632fb4308)


