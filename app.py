import requests


def random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        print(f"{joke['setup']}\n{joke['punchline']}")
    else:
        print(f"Échec de l'import de blague. Code erreur: {response.status_code}")


if __name__ == "__main__":
    random_joke()