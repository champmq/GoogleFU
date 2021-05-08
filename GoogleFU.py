from modules.sort import Sort
from modules.search import Search


banner = """
  ▄████  ▒█████   ▒█████    ▄████  ██▓    ▓█████   █████▒█    ██ 
 ██▒ ▀█▒▒██▒  ██▒▒██▒  ██▒ ██▒ ▀█▒▓██▒    ▓█   ▀ ▓██   ▒ ██  ▓██▒
▒██░▄▄▄░▒██░  ██▒▒██░  ██▒▒██░▄▄▄░▒██░    ▒███   ▒████ ░▓██  ▒██░
░▓█  ██▓▒██   ██░▒██   ██░░▓█  ██▓▒██░    ▒▓█  ▄ ░▓█▒  ░▓▓█  ░██░
░▒▓███▀▒░ ████▓▒░░ ████▓▒░░▒▓███▀▒░██████▒░▒████▒░▒█░   ▒▒█████▓ 
 ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▒░▒░  ░▒   ▒ ░ ▒░▓  ░░░ ▒░ ░ ▒ ░   ░▒▓▒ ▒ ▒ 
  ░   ░   ░ ▒ ▒░   ░ ▒ ▒░   ░   ░ ░ ░ ▒  ░ ░ ░  ░ ░     ░░▒░ ░ ░ 
░ ░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░   ░   ░ ░      ░    ░ ░    ░░░ ░ ░ 
      ░     ░ ░      ░ ░        ░     ░  ░   ░  ░          ░     
                                                                 
"""
print(banner +
      "*" * 40 + "\n" + "This tool will find information that\nare on Google about someone."
                        "\nIt works good with invented online names." + "\n" + "*" * 40 + "\n")

query = input("Query: ")
urls = Search(query).urls()
sorted_urls = Sort(urls).sort()
if sorted_urls["socials"]:
    print("Socials: " + ", ".join(sorted_urls["socials"]))
if sorted_urls["pastes"]:
    print("Pastes: " + ", ".join(sorted_urls["pastes"]))
if sorted_urls["ratings"]:
    print("Ratings: " + ", ".join(sorted_urls["ratings"]))
if sorted_urls["blogs"]:
    print("Blogs: " + ", ".join(sorted_urls["blogs"]))
if sorted_urls["hacking"]:
    print("Hacking: " + ", ".join((sorted_urls["hacking"])))
if sorted_urls["other"]:
    print("Other: " + ", ".join(sorted_urls["other"]))
