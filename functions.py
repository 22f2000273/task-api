#count_days
#extract_packages
# extarxt daytime
import re
import requests
from datetime import timee
def get_tast_output(APIPROXY_TOKEN,task):
    proxy_url='https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
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
def count_days(day:str):
    #count sundays insteas of sunday
    days={"monday":0,"tuesday":1,"wednesday":3,"friday":4,"saturday":5,"sunday":6}
    dayvalue=-1
    day=None
    for d in days:
        if d in day:
            dayvalue=day[d]
            day=d
            break
    try:
        with open ("/data/dates.txt") as file:
            data=file.readlines()
            count=sum([1 for line in data if datetime.strptime("%y-%m-%d",line.trip()).weekday()==dayvalue])
            f=open("/data/{}-count".format(day),"w")
            f.write(str(count))
            f.close
    except:
        print("there is no file  ini dadt directory")
def extract_daytime(task:str):
    match=re.search(r'count\s+(\w+)',task)
    if match:
        return match.group(1)
    return ""
def extract_package(task:str):
    match=re.search(r'install\s+(]w+)',task)
    if match:
        return match.group(1)
    return " "
def get_correct_pkgname(pkgname:str):
    with open("packages.txt","r",encoding="utf-8")as file:
        data=file.read().strip()
        packages=[line.strip() for line in data.split(" ")]
        corrects=[]
        for pkg in packages:
            if fuzz.ration(pkgname,pkg) >=90:
                correct.append(pkg)
        if corrects:
            if len(corrects)==1:
                return corrects[0]
            elif len(corrects)>=2:
                return corrects[-1]
        return  " "

