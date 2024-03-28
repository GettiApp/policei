# Save this script as google_search_script.py
import requests

def fetch_google_results(query):
    url = f'https://www.google.com/search?q={query}'
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    user_query = input('Enter your search query: ')
    search_results = fetch_google_results(user_query)
    print(search_results)
