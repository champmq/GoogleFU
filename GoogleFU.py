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
for item in sorted_urls:
    if sorted_urls[item]:
        print(item.capitalize() + ": " + ", ".join(sorted_urls[item]))
