## Project Title:
##### Twitter Sentiment Analysis Using Natural Language Toolkit, VADER Sentiment, Data Visualization and Analysis Libraries.

## Project Members:
##### 1. Owais Azad (CSC-20F-139).
##### 2. Syed M. Aaliyan Tarique (CSC-20F-171).
##### 3. Muhammad Shafiq Ashfaq (CSC-20F-118).

## Libraries and Model:
- NLTK
- SentimentIntensityAnalyzer
- Pandas
- NumPy
- Metplotlib
- Seaborn
- warning
- tqdm

## DATASET:
##### ImranKhanPTI.csv file contain Ex. Prime Minister Tweets Data from 2018 to 2022.

## MAIN SOURCE CODE:
##### **"sentiment-analysis-with-nltk.ipynb"** File contain main source code that take dataset and analyse it either the tweet is Positive, Neutral, or Negative.

## TWitter API:
##### **twitter_tweet.py** file contain tweet API with .env file for getting tweets data by user name.

## Steps to setup project

### 1. Clone the repo

### 2. Install Python

### 3. Create and activate virtual enviroment in project folder
~~~~
virtualenv venv
~~~~
activate venv in linux
~~~~
source venv/bin/activate
~~~~
activate venv in windows
~~~~
venv/Scripts/activate
~~~~

### 4. Install requirements.txt
~~~~
pip install -r requirements.txt
~~~~

## Steps to use project

### 1. Place your Dataset (.csv file) and sentiment-analysis-with-nltk.ipynb file in same Folder

### 3. Make sure that dataset have same column name.

### 4. Run

~~~~
python sentiment-analysis-with-nltk.ipynb
~~~~

## DATA VISUALIZATION OF IMRAN KHAN TWEETS:

![Compound Score by Imran Khan Tweets](https://drive.google.com/uc?id=1KE8OlyIzZcw8uxnXTszIczvBRAyBn2rk)