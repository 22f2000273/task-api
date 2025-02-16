import requests

AIPROXY_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjIwMDAyNzNAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.ODIcsNPnLHL-TmTL0jpuMF8DogUUKRvnWOnZhS2pIxw'

def add_two_number_with_ai(num1, num2):
    proxy_url = 'https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer {}'.format(AIPROXY_TOKEN)
    }
    payload = {
        'model': 'gpt-4o-mini',  # Update to available model

        "messages": [  # Changed from "message" to "messages"
            {'role': 'system', 'content': 'you are a python calculator. add two numbers'},
            {'role': 'user', 'content': f'add {num1} and {num2}'}
        ],
        'temperature': 0,
        'max_tokens': 50
    }
    
    # Sending the request
    response = requests.post(url=proxy_url, headers=headers, json=payload)
    
    # Debugging: Print the response for errors
    if response.ok:
        ai_response = response.json()
        #print("AI Response:", ai_response)  # Debugging line
        result = ai_response["choices"][0]["message"]["content"].strip()
        return result
    else:
        print(f"Error: {response.text}")  # Added to print the error message from the server
        return f'Error fetching the sum, status code: {response.status_code}'

num1 = 8744
num2 = 9054
result = add_two_number_with_ai(num1, num2)
print(f"Addition of {num1} and {num2} is: {result}")
