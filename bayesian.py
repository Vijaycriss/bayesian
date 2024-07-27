import argparse
import os
import requests

ollama_API_URL = "https://api.ollama.com/summarize"
API_KEY = os.getenv("OLLAMA_API_KEY") 


def summary_text(text):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'qwen2-0.5b',
        'text': text
    }
    
    response = requests.post(ollama_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get('summary', 'No summary found.')
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():

    parser = argparse.ArgumentParser(description="This is new Command-line Tool for summrizing text")

    parser_group = parser.add_argument_group('input_options', 'Enter one of the input options')
    parser_group.add_argument('--file', type=str, help='path to the text file')
    parser_group.add_argument('--text', type=str, help='text')
    
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        parser.error("Provide valid input")
    
    summary = summary_text(text)
    print(summary)
    
if __name__ == '__main__':
    main()
    
