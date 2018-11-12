class Sources:
    def __init__(self,id,name,description,language):
        self.id = id
        self.name = name
        self.description = description
        self.language = language

class Articles:
    def __init__(self,author,title,description,url,publishedAt,urlToImage):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.urlToImage = urlToImage