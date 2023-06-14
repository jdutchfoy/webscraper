import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    passages = soup.find_all(string=lambda text: text and "[citation needed]" in text)
    return len(passages)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    passages = soup.find_all(string=lambda text: text and "[citation needed]" in text)
    report = "\n".join(passages)
    return report

def get_citations_needed_by_section(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    sections = soup.find_all('section')  # Modify this to match your desired section element
    citations_by_section = {}
    for section in sections:
        section_passages = section.find_all_next(string=lambda text: text and "[citation needed]" in text)
        citations_by_section[section.get('id')] = section_passages
    return citations_by_section

# Example usage:
url = "https://en.wikipedia.org/wiki/Your_Wikipedia_Page"
count = get_citations_needed_count(url)
print(f"Number of citations needed: {count}")

report = get_citations_needed_report(url)
print("Citations needed report:")
print(report)

citations_by_section = get_citations_needed_by_section(url)
print("Citations needed by section:")
print(citations_by_section)
