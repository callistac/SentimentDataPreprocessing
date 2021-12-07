import pandas as pd
import argparse

def format_data(args):
    '''
    This function reformats the Kaggle dataset such that it can be
    used as input into Vertex AI in GCP
    '''
    # reads in Kaggle dataset and stores result in a Pandas DataFrame
    df = pd.read_csv(args.input, names=["sentiment", "id", "date", "query", "user", "text"], encoding='latin1')

    # discards middle 3 columns and shuffles dataset
    df = df.drop(df.columns[1:5], axis=1)
    df = df.sample(frac=1)

    # changing all instances where sentiment = 4 to 1
    df.loc[df['sentiment'] == 4, 'sentiment'] = 1

    # ensures that the sentiment values are integers, not strings
    df.sentiment = df.sentiment.astype(int)

    # creating a new column "max_sentiment" that Vertex AI expects
    df['max_sentiment'] = 1

    # reorders columns to be in the order Vertex AI expects
    df = df[['text', 'sentiment', 'max_sentiment']]

    # selects the first n rows of the dataset (n must be less than 100k)
    df = df[:int(args.n_rows)]

    # saves new CSV file that will be uploaded to Vertex AI
    df.to_csv(args.output, index=False)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help="Local path to Kaggle dataset")
    ap.add_argument('-o', '--output', required=False, help="Output filename for reformatted dataset", default="sentiment_data.csv")
    ap.add_argument('-n', '--n_rows', required=False, help="How many rows of the data you will include in your train, test, and validation", default=4000)
    
    args = ap.parse_args()
    format_data(args)
