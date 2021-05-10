class Sort:
    """
    Sort Class
    """
    def __init__(self, urls=None, socials_file="./socials.txt", ratings_file="ratings.txt") -> None:
        """Constructor

        Args:
            urls (list, optional): List of URLs. Defaults to None.
            socials_file (str, optional): Path to socials.txt. Defaults to "./socials.txt".
            ratings_file (str, optional): Path to ratings.txt. Defaults to "ratings.txt".
        """
        if urls is None:
            urls = []
        self.urls: list = urls
        self.socials_file: str = socials_file
        self.ratings_file: str = ratings_file
        self.output: dict = {
            "socials": [],
            "pastes": [],
            "ratings": [],
            "blogs": [],
            "hacking": [],
            "programming": [],
            "images": [],
            "other": []
        }

    def sort(self) -> dict:
        hacking_keywords: list = ["hacking", "ctf", "hacker", "hack"]
        programming_keywords: list = ["code", "coding", "programmer", "developer", "programming", "coder"]
        image_keywords: list = ["image", "photo", "picture"]
        for url in self.urls:
            added: bool = False
            if "paste" in url:
                self.output["pastes"].append(url)
                continue
            if "blog" in url:
                self.output["blogs"].append(url)
            for hk in hacking_keywords:
                if hk in url:
                    self.output["hacking"].append(url)
                    added = True
            for pk in programming_keywords:
                if pk in url:
                    self.output["programming"].append(url)
                    added = True
            for ik in image_keywords:
                if ik in url:
                    self.output["images"].append(url)
                    added = True
            for social in open(self.socials_file, "r+").readlines():
                if social.replace("\n", "") in url:
                    self.output["socials"].append(url)
                    added = True
            for rating in open(self.ratings_file, "r+").readlines():
                if rating.replace("\n", "") in url:
                    self.output["ratings"].append(url)
                    added = True
            if added is False:
                self.output["other"].append(url)
        return self.output
