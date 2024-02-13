import requests
from requests.auth import HTTPBasicAuth
from FUNC.config import API_METHOD


def API_REGISTER(*args, API_METHOD=API_METHOD):
    url = 'http://127.0.0.1:7000/register'

    first_data = {
        'name': args[0],
        'username': args[1],
        'email': args[2],
        'is_chef': [3],
        'password': [4]
    }

    username = r'T%%SSssa00SDFG55GR45654564RWEEEWERWERFWEWR51G4V56R1V65R456WE4RFEW564FRT56WV56WER41V65WE4G65EW4F65WEC16E5W4GF65E4G5W14VCEW654CWEFWEKJFBSDJKHCBJKDHBVKJWVB'
    password = r'hghgfhgfhgfTfgdf%%SSssa00gsfdghfdSDFGhgfj55GR4565456sdfgjdfdsaffgjdsgf4RWEEEWERWhjRFWhgjWR51G4kghV56R1V6kkhf5R456WE4RFEW564FRT5kjh6WV56WklhjlR41V65WE4G65EW4F65WEC16E5kjkW4GF65E4G5W14VCEWhjilkilkjl;4CWEFWEj;lk;KJFBSDJKHCBJKDHBVKJWVB'

    response = requests.post(url, json=first_data, auth=HTTPBasicAuth(username, password))

    print(response.status_code)
    res = response.json()
    print(res)
    if 'Error' in res.keys():
        return 100
    elif res['user_id']:
        return res['user_id']
    else:
        return False
    

def token_verify(tkn):
    url = 'https://127.0.0.1/token_register'

    params = {
        'Token': tkn
    }

    response = requests.post(url=url, json=params)

    data = response.json()

    return True if data['result'] is True else False