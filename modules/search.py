from googlesearch import search as gsearch


class Search:
    def __init__(self, query):
        self.query = query

    def urls(self):
        return gsearch(f'"{self.query}"')