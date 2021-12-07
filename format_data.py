import pandas as pd

# reads in our sentiment data and explicitly defines column names
df = pd.read_csv('training.1600000.processed.noemoticon.csv', names=["sentiment", "id", "date", "user", "text"])
df = df.drop(df.columns[1:4], axis=1)
df = df.sample(frac=1)
# ensures that the sentiment values are integers, not strings
df.sentiment = df.sentiment.astype(int)
# creating a new column "max_sentiment" that Vertex AI expects
df['max_sentiment'] = 4
# reordering columns to be in the order Vertex AI expects
df = df[['text', 'sentiment', 'max_sentiment']]
df = df[:99999]
print(df.head())
# saves new CSV file that we will upload to Vertex AI
df.to_csv('sentiment_data.csv', index=False)