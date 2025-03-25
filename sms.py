import requests
import json
import requests
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
def banner():


    print(f"""{green}
                ╔═╗╔╦╗╔═╗  
                ╚═╗║║║╚═╗  
                ╚═╝╩ ╩╚═╝  
          
          {white}Created By : {red}Jovan
""")
def refresh_jwt_token():
    url = "https://34.160.218.33.nip.io/lbconline/RefreshJWTToken"

    # Headers
    headers = {
        'Host': '34.160.218.33.nip.io',
        'Content-Length': '0',
        'Sec-CH-UA-Platform': '"Windows"',
        'LBCOakey': 'd1ca28c5933f41638f57cc81c0c24bca',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Sec-CH-UA': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'Content-Type': 'application/json',
        'Token': 'O8VpRnC2bIwe74mKssl11c0a1kz27aDCvIci4HIA+GOZKffDQBDkj0Y4kPodJhyQaXBGCbFJcU1CQZFDSyXPIBni',
        'Sec-CH-UA-Mobile': '?0',
        'Accept': '*/*',
        'Origin': 'https://lbconline.lbcexpress.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Storage-Access': 'active',
        'Referer': 'https://lbconline.lbcexpress.com/',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'lexaRefreshTokenProd=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJGdm9pNlF5TWpBZ1M2QkhmRGs0eDRabmM2a0EzIiwianRpIjoiNDNmMzI1OTItYzc5Zi00NjNmLWE5MjQtODhiNGVlMzM5OWY1IiwiaWF0IjoiMy8yNS8yMDI1IDEwOjUwOjE0IEFNIiwibmFtZSI6IkZ2b2k2UXlNakFnUzZCSGZEazR4NFpuYzZrQTMiLCJpcCI6IjM0LjEyOC43MS4xOTMiLCJleHAiOjE3NDI5NTc0MTQsImlzcyI6Imh0dHBzOi8vbGJjb25saW5lLmxiY2V4cHJlc3MuY29tIiwiYXVkIjoiaHR0cHM6Ly9sZXhhYXBpLmF6dXJld2Vic2l0ZXMubmV0In0.0uC6DRix3uALdC0rfNUxsW8OHtGtSNkTQykymQUxmlA',
    }

    # Sending the POST request
    response = requests.post(url, headers=headers)

    # Checking the response
    if response.status_code == 200:
        return response.json()  # This will print the JSON response if successful
    else:
        print(response.text)



def send_request(token,number,text):
    # Get inputs from the user
    

    # API URL
    url = "https://34.160.218.33.nip.io/lbconline/AddDefaultDisbursement"

    # Headers
    headers = {
        'Host': '34.160.218.33.nip.io',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Length': '318',
        'Ptxtoken': f'{token}',
    }

    # Data payload
    data = {
        "Recipient": number,
        "Message": text,
        "ShipperUuid": "LBCEXPRESS",
        "DefaultDisbursement": 3,
        "ApiSecret": "03da764a333680d6ebd2f6f4ef1e2928",
        "apikey": "7777be96b2d1c6d0dee73d566a820c5f"
    }

    # Sending the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Checking if the request was successful
    if response.status_code == 200:
        print(f"{green} Message Succesfully Sent to : {red}{Number}")
    else:
        print(f"Failed to send request. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    banner()
    refresh_jwt_token()
    print(f"{blue}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    Number = input(f" Enter Number : ")
    print(f"{blue}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    Text = input(f"   Enter Text : ")
    print(f"{blue}⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    token = refresh_jwt_token()
    send_request(token,Number,Text)

