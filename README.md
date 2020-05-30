# Big-Data
Python project to scrape RSS news feeds, derive topic maps and analye sentiment. 
Multiple visualizations are displayed in a Jupyter Notebook

## Getting Started

The easiest approach is to clone this repository (https://github.com/jb-diplom/Big-Data/edit/master/README.md) and test the Notebook [./RSSNewsIdentification.ipynb] on Jupyter.

### Prerequisites

To run all the implemented features you'll need:
* Python 3.7 or newer
* Jupyter (I have been using Version 6.03)
* Anaconda (for easy and consistent installation)
* Gensim (for Word Embedding tools and downloader, corpora, topic modelling)
* Natural Language Toolkit (NLTK) for text processing (Lemmatization)
* VaderSentiment (Sentiment analysis)
* Bokeh (Visualization widgets and coloring)
* Feedparser (Scraping RSS Feeds)
* pyLDAvis (Visualization of LDA analysis)
* ipyvolume (3d rotational scatterplots) 
* Beautiful Soup (parsing and cleaning HTML/XML)

### Installation
Several Python packages are necessary to complete analysis/computations and for an adequate visualization in Jupyter notebook
* `conda install bokeh`
* `conda install feedparser `
* `conda install genism `
* `conda install -c conda-forge pyldavis ` see also https://github.com/bmabey/pyLDAvis
* `conda install -c conda-forge ipyvolume`
* `conda install -c conda-forge nodejs`
* `conda install -c conda-forge ipydatawidgets`
* ```import nltk
nltk.download(’vader_lexicon’)```
* nltk.download()` --> choose Corpora/wordnet

## Usage

The central element to access the funtionality of the project work is by loading the RSSNewsIdentification.ipynb: Jupyter Notebook.
Virtually all of the useful configurative settings can be specified or modified in the run parameters, which are held in an editable Python dictionary near the beginning of the notebook. The parameters are documented as comments in the code (see below).

Some  

### The Run Parameters
```
runParams={'allFeeds':       getFeedDict(),   # A collection of 50 URLs for RSS Feeds, where the names can be chosen freely
                                              # example: {'Buzzfeed': 'https://www.buzzfeed.com/world.xml', 
                                              #           'Al Jazeera': 'http://www.aljazeera.com/xml/rss/all.xml'}
           'collectFeeds':   False,           # Set to True to do more data-scraping
           'inputDir':       './data',        # Directory containing pre-collected RSS-Feed data in pickle format
           'articleLimit':   10000,           # Optional specification limiting number of articles to process (for test
                                              # purposes only)
           'numAuthDispl':   30,              # specify limit of number of authors to display/plot
           'numTagsDispl':   30,              # specify limit of number of tags to display/plot
           'numTopics':      30,              # specify limit of number of topics to be found via TFIDF Vectorization
           'numLDATopics':   30,              # specify limit of number of topics to be found via Latent Dirichlet Allocation 
           'numTopicsDispl': 30,              # specify limit of number of topics to display/plot
           'removeTopics':   True,            # specify if articles now referenced by topics should be removed (saves 
                                              # computation time later)
           'ngramRange':     (3,3),           # define min and max ngrams as tuple for deriving topic maps 
           'weModel':        'glove-wiki-gigaword-50', # Word Embedding model for soft cosine similarity calculation
                                              # options are e.g. glove-wiki-gigaword-50,fasttext-wiki-news-subwords-300
                                              # CAUTION: although higher dimension models produce more nuanced results, load
                                              # times are VERY long. In particular the first time use requires a download of
                                              # massive amounts of data which can easily take as much as an hour
           'thresholdFuzzy': 60,              # define cut-off threshold for fuzzy (Levenshtein Distance comparison) in percent
           'thresholdCosine':0.60,            # define cut-off threshold for soft cosine similarity as fraction (0.0 to 1.0)
           'fuzzyDocLimit':  None,            # optional integer limit to number of articles used for fuzzy relevance of
                                              # topics (only for test purposes: default None) 
           'matrixDir':      './outdata',     # relative path for saving matrices to file
           'saveMatrix':     False}           # whether to save matrix to file or not
```
### Test Data
Two crucial sets of data are supplied to help the user get up and running very quickly.
1. A set of 50 fully tested RSS-Feed URLs, which are loaded from the function `getFeedDict()`. The user can simply specify custom values in an equivalently structured dictionary,  .e.g.
> ``` {'Buzzfeed': 'https://www.buzzfeed.com/world.xml', 'Al Jazeera': 'http://www.aljazeera.com/xml/rss/all.xml'}```
2. A corpora of over 11000 articles which have been collected between 02.05.2020 and 31.05.2020 daily from the 50 RSS-feeds mentioned in 1.  
An article limit `articleLimit` can be specified for test purposes to take a randomized sample of documents from the test corpora. It should be mentioned that with 10000 documents the runtime for the complete notebook runs into several hours.

### Features

Initially the user can load data from a pre-configured set of 50 RSS-Feeds, or specify custom feeds for scraping. This takes typically aproximately 75s. Additionally there is a large corpus of test data in the directory [./data/] which may be loaded 
Explain what these tests test and why

```
Give an example
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Janice Butle** - *Initial work* - [Big-Data Project](https://github.com/jb-diplom/Big-Data)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
