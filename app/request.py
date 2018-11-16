import urllib.request,json
from .models import Articles,Sources

#fetching API key
api_key= None

#getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCE_URL']
    


def get_sources():


    '''
    function that returns the json response from url
    :return:
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results=process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    sources_results=[]
    for source_item in sources_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        language=source_item.get('language')

        if id:
            source_object = Sources(id,name,description,language)
            sources_results.append(source_object)

    return sources_results

def get_articles(id):
    get_articles_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(get_articles_details_url)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response["articles"]:
            articles_list=articles_details_response['articles']
            articles_object= process_source_results(articles_list)

    return articles_object

def process_source_results(news_list):
    articles_object=[]
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        urlToImage=news_item.get('urlToImage')

        if urlToImage:
            source_news_object = Articles(author,title,description,url,publishedAt,urlToImage)
            articles_object.append(source_news_object)

    return articles_object

def get_category(category):
    get_category_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'.format(category, api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_category_results = None

        if get_cartegory_response['articles']:
            get_category_list = get_cartegory_response['articles']
            get_category_results = process_source_results(get_category_list)

    return get_category_results
