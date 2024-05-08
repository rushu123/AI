# pip install google beautifulsoup4 requests

import re
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def is_math_expression(input_str):
    return bool(re.search(r'[\d+\-*/]', input_str))

def evaluate_math_expression(input_str):
    try:
        return eval(input_str)
    except:
        return None

def search_google(query):
    try:
        return search(query, num=5, stop=5, pause=2)
    except:
        return []

def extract_content(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        return ' '.join([p.get_text() for p in soup.find_all('p')])[:200] + "..."
    except:
        return ""

def chatbot():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        result = evaluate_math_expression(user_input)
        if result is not None:
            print(f"Chatbot: The result is {result}")
        else:
            results = search_google(user_input)
            if results:
                print("Chatbot: Here is the information I found:")
                for i, result in enumerate(results, start=1):
                    content = extract_content(result)
                    print(f"{i}. {content}\n" if content else f"{i}. No information available for this result.\n")
            else:
                print("Chatbot: I couldn't find any relevant information. Can you please rephrase your query?")

if __name__ == "__main__":
    chatbot()
