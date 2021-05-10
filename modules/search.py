from googlesearch import search as gsearch


class Search:
    """
    Search class
    """
    def __init__(self, query="") -> None:
        """Constructor

        Args:
            query (str, optional): Query to look up. Defaults to.
        """
        self.query: str = query

    def urls(self) -> list:
        return gsearch(f'"{self.query}"')