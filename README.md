

### Project Description Slides
* analyzing_presidency_similarity.pdf

### Data Acquisition

* __web_scrape_american_presidency_raw_text.ipynb__ 

  retrieves preseidential documents from [American Presidency Project](http://www.presidency.ucsb.edu/) in units of 1000 docs, then save each unit in a pickle file

### Data Processing

* __process_data_raw_text_to_DB.ipynb__ 

 extract date, title, author and text from each web page scraped by scrape_american_presidency_raw_text.ipynb and insert the record into mongoDB
 
 
* __process_data_stem_text_to_DB.ipynb__
    1. retrieve records of presidential docs from database
    2. clean and tokenize raw text
    3.  insert processed text along with date, author and title as new records into a  new collection in database
 

### Data Transformation

* __transform_data_tfidf_topic_modelers.ipynb__ 

  1. transform tokenized text to word matrix using tfidf vectorizer
  2. build 3 topic modlers: lsa, lda and nmf

### Data Analysis

* __data_analysis_presidency_similarity_and_clusters.ipynb__

  1. given author, find most similar presidents in terms of cosine similarity
  2. group presidents in clusters 
  3. visualization

### Flask directory


  * files for creating web based flask app that takes in user input and returns a list of similar presidents
  * files in flask/data/ not included in submission because size exceeds git hub limit




### Data directory

* files in this directory not included in submission because size exceeds git hub limit

  1. scraped presidential documents from data sources
  2. saved pickle files


