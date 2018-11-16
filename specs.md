Unofficial News App through News API for [News API](https://newsapi.org/).
The app is live here [News.io](https://news-io.herokuapp.com/).


Features
========

- Built with Python 3 (3.7+) and Flask
- Shows 'news sources', 'news articles','categories' and sorted by relevancy
- Styled using Bootstrap
- Handles external get posts and requests from API
- Get news articles from several sources (`choose from landing page`)


Installation
========

    $ git clone <repository_url>


Usage
========

**NOTE:** You need to have fully cloned it to run it locally.


    $ ./start.sh 

    # it will launch the web page from local server and fetch 
    news using api provided


API Object Reference
========

## Classes: `Sources, Articles`


**Arguments:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `category` | string | No | Returns the articles from this topic only and sorted by relevancy. | `(empty string)`  |
| `news_source` | integer | No | Returns the articles from this news source only. | `(user's choice)` |



## Class: `Sources`

Each `Sources` has the following properties

- **name** - news source name
- **id** - news source unique id
- **description** - info about the news source
- **url** - official website link to news source

## Class: `Article`

Each `Article` has the following properties

- **id** - unique id of the article
- **title** - the title of the article itself
- **description** - the article itself and what it is about
- **published time** - time when it was submitted
- **image url** - image url for image tags
- **url** - url to website for full article

Tests
========

To run the tests locally just do:

    $ cd app
    $ python3.7 classes_test.py


The tests are run on a local test server.

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!