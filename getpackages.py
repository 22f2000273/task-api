import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/simple/"

def get_packages(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        packages = [a.text.strip() for a in soup.find_all('a')]  # Extract package names

        # Save only package names (not entire HTML)
        with open("packages.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(packages))  

        print("Packages list saved to 'packages.txt'")

get_packages(url)
