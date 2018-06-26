import vk_api
import time

vk = vk_api.VkApi(token='377b806930a53563ea391ee3227eef0fca4a9b77a5006663b0e5578b55c9e9180c91072503a88dafe364e')
vk._auth_token()
values = {'out': 0, 'count': 100, 'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})
    
def main():
    while True:
        try:
            response = vk.method('messages.get', values)
            if response['items']:
                values['last_message_id'] = response['items'][0]['id']
            for item in response['items']:
                if response['items']:
                    a = response['items'][0]["body"]
                    a = a[::-1]
                    a = a.capitalize()
                    write_msg(item['user_id'],a)
        except:
            continue
        time.sleep(3)
                    
if __name__ == '__main__':
    main()
