# Sentiment Data Preprocessing
This script contains the data preprocessing script used to format data for Sentiment Analysis training using Vertex AI on GCP. If you are not comfortable with terminal or command prompt, you may want to skip these instructions and copy / paste the code in the `format_data.py` file in this repository into a Jupyter Notebook, but we encourage you to try running this in terminal first!

## Setup
1. Make sure you have [Python3](https://www.python.org/downloads/) installed on your machine
2. Ensure that [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) is installed on your device
3. Open a terminal (Mac/Linux OS) or command prompt (Windows) and install [Pandas](https://pandas.pydata.org/) which is a popular data analysis library in Python:
  ```
  pip3 install pandas
  ```
4. Clone this code to your local device in a desirable location (i.e. you might want to create a folder on your Desktop called `google_workshop`):
  ```
  cd ~/Desktop/google_workshop
  git clone https://github.com/callistac/SentimentDataPreprocessing.git
  ```
  Please note that the `cd` command syntax will differ if you are on a Windows computer.
  
Congratulations-- you are ready to begin formatting your new dataset!

## Reformat Data
To reformat the data, please change directories into your cloned repository:
```
cd SentimentDataPreprocessing/
```

Now we can simply reformat the data by typing:
```
python3 format_data.py -i training.1600000.processed.noemoticon.csv -n 3000
```
The new data will be saved in the same location but will now be called `sentiment_data.csv`. This is the reformatted dataset that you will upload to Vertex AI
Note: the `-i` flag is the path to where your input data is located, and `-n` selects the first 3000 rows of the dataset to use. Vertex AI will limit you to a maximum of 100,000 rows. The less data you have, the faster training will be; however, your model may not be as accurate.
