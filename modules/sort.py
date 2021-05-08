class Sort:
    def __init__(self, urls=None, socials_file="./socials.txt", ratings_file="ratings.txt"):
        if urls is None:
            urls = []
        self.urls = urls
        self.socials_file = socials_file
        self.ratings_file = ratings_file
        self.output = {
            "socials": [],
            "pastes": [],
            "ratings": [],
            "blogs": [],
            "hacking": [],
            "other": []
        }

    def sort(self):
        hacking_keywords = ["hacking", "ctf", "hacker", "hack"]
        for url in self.urls:
            added = False
            if "paste" in url:
                self.output["pastes"].append(url)
                continue
            if "blog" in url:
                self.output["blogs"].append(url)
            for hk in hacking_keywords:
                if hk in url:
                    self.output["hacking"].append(url)
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
