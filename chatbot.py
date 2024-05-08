from googlesearch import search
from bs4 import BeautifulSoup
import requests

def search_google(query):
    try:
        return search(query, num=5, stop=5, pause=2)
    except Exception as e:
        print("An error occurred while searching:", str(e))
        return []

def extract_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return ' '.join([p.get_text() for p in soup.find_all('p')])[:200] + "..."
    except Exception as e:
        print("An error occurred while extracting content:", str(e))
        return ""

def chatbot():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        results = search_google(user_input)
        if results:
            print("Chatbot: Here is the information I found:")
            for i, result in enumerate(results, start=1):
                content = extract_content(result)
                print(f"{i}. {content}\n" if content else f"{i}. No information available for this result.\n")
        else:
            print("Chatbot: I couldn't find any relevant information. Can you please rephrase your query?")

chatbot()
