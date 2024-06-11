class Article:
    # Class variable for all variables
    all = []

    def __init__(self, author, magazine, title):
        #Validate the title
        if not isinstance(title, str) and not 5 <= len(title) <= 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
            #initialize instance variables
        self._author = author
        self.magazine = magazine
        self._title = title
        self._author.add_articles(self)
        self._magazine.add_articles(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("author must be of type Author")
        else:
            self._author = new_author
            
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")
        else:
            self._magazine = new_magazine

class Author:
    
    def __init__(self, name):
        #validate the name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a string with at least 1 character")
        
        self._name = name
        self._articles = []
    
    @property  
    def name(self):
        return self._name

    def articles(self):
        return self._articles
    #create a new article
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    def magazines(self):
     set_magazines = {article.magazine for article in self._articles}
     return list(set_magazines)

    def topic_areas(self):
        if not self._articles:
            return None
        set_categories = {article.magazine.category for article in self._articles}
        return list(set_categories)

class Magazine:
    def __init__(self, name, category):
        
        self.name = name
        self.category = category
        self._articles = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <=16:
                self._name = new_name
            else: 
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                raise ValueError("Category must be more than 0 characters")
        else:
            raise TypeError("Name must be a string")
        
    def articles(self):
        #Return the list of articles published in the magazine
        return self._articles  
    

    def article_titles(self):
        #return a list of titles
        if not self._articles:
            return None
        special_categories = list()
        for article in self._articles:
            if article.magazine:
                special_categories.append(article.title)
        return list(special_categories)


    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
        else:
            raise TypeError("Must be of type Article")

    def contributors(self):
        unique_authors_set = {article.author for article in self._articles}
        return list(unique_authors_set) if unique_authors_set else None


    def contributing_authors(self):
        #return a list of authors who have written more than two articles
        author_counts = {}
        for article in self._articles:
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else: 
                author_counts[author] = 1
        many_authors = [author for author, count in author_counts.items() if count > 2]
        if many_authors:
            return many_authors
        else:
            return None