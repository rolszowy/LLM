import requests
import ollama
from bs4 import BeautifulSoup

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return {"error": "Failed to retrieve data"}

class Website:
        def __init__(self, url):
            """
            Initializes the Website class with a URL.
            """
            self.url = url
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.title = soup.title.string if soup.title else "No title found"
                self.soup = soup
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                self.text = soup.body.get_text(separator="\n", strip=True)
            else:
                self.soup = None

if __name__ == "__main__":
    # url = "http://localhost:11434/"
    # data = get_data(url)
    # print(str(data))

    headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
    ed = Website("http://edwarddonner.com")
    get_data("http://edwarddonner.com")

    system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

    def user_prompt_for(website):
        user_prompt = f"You are looking at a website titled {website.title}."
        user_prompt += f"\n\nThe main content of the page is as follows:\n{website.text}"
        user_prompt += website.text
        return user_prompt

print (user_prompt_for(ed))

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_for(ed)}
]
response = ollama.chat("llama3.2", messages=messages)
print(response['message']['content'])
