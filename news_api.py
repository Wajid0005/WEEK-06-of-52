import requests
from config import API_KEY, BASE_URL


def get_news(country = "in"):

    params = {
    "apiKey": API_KEY,
    "q": "india",
    "pageSize": 20,
    "sortBy": "publishedAt",
    "language": "en"
    }

    
    response = requests.get(BASE_URL, params = params)
    print("Status Code:", response.status_code)
    
    if response.status_code != 200:
        print("Error:", response.text)
        return []

    data = response.json()

    if data.get("status") != "ok":
        print("API Error:", data)
        return []

    articles = data.get("articles", [])
    return articles

if __name__ == "__main__":
    news = get_news("in")
    print("Total articles:", len(news))

    if news:
        print(news[0]["title"])

