import time
import vk_api
import threading
import os


try:
    bot = vk_api.VkApi(token='')
    bot._auth_token()
    values = {'out': 0, 'count': 100, 'time_offset': 60}
except:
    time.sleep(10)
    os.system('start Bot.py')
    raise SystemExit(403)

peopleID = []

fileR = open('pepID.txt','r')
for line in fileR.readlines():
    peopleID.append(str(line))
fileR.close()



def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

#def commandLine():
#    while True:
#        command = input('\n-->CMD: ')
#        if ((command == 'help' ) or (command == 'HELP')):
#            print('-->I am - command line of bot naoborot! I can do what do u want with users. I have functions: clear , help , CMD <command> , sendMSG <msg> <enter> <id> <enter> , glSendMSG <msg> <enter> .  <--')
#        if 'clear' in command:
#            os.system('cls')
#        if 'CMD' in command:
#            try:
#                command = command.replace('CMD' , '')
#                print(os.system(command))
#
#            except:
#                print('-->WARNING:This command is not avalible!:WARNING<--')
#        if 'sendMSG' in command:
#            try:
#                textMSG = input('-->Write the text for msg: ')
#                personID = input('-->Write the personID for msg: ')
#                write_msg(int(personID) , str(textMSG))
#                print('-->Status: Suceful! :Status<--')
#            except:
#                print('-->Status: WRONG! :Status<--')
#        if 'glSendMSG' in command:
#            try:
#                textMSG = input('-->Write the text for msg: ')
#                for persID in peopleID:
#                    write_msg(int(persID) , textMSG)
#                print('-->Status: Suceful! :Status<--')
#            except:
#                print('-->WARNING: ID HAS WRONG :WARNING<--')
#        if 'peopleID' in command:
#            try:
#                print(peopleID)
#                print('-->Status: Suceful! :Status<--')
#            except:
#                print('-->Status: WRONG! :Status<--')

def MSG():
    try:
        while True:
                response = vk.method('messages.get', values)
                if response['items']:
                    values['last_message_id'] = response['items'][0]['id']
                    print('\n-->Message from user:   ' + str(response))
                for item in response['items']:
                    if response['items']:
                        a = response['items'][0]["body"]
                        a = a[::-1]
                        a = a.capitalize()
                        write_msg(item['user_id'],a)
                        if not item['user_id'] in peopleID:
                            peopleID.append(int(item['user_id']))
                            fileW = open('pepID.txt', 'a')
                            fileW.write(int(item['user_id']))
                            fileW.close()
                            print('-->peopleID: ' + str(peopleID))
    except Exception as err:
            time.sleep(10)
            os.system('start Bot.py')
            raise SystemExit(1)
#def AdditionalMSG():
#    while(True):
#        try:
#            response = vk.method('messages.get', values)
#            if response['items']:
#                values['last_message_id'] = response['items'][0]['id']
#                print('\n-->Message from user:   ' + str(response))
#            for item in response['items']:
#                if response['items']:
#                    if not item['user_id'] in peopleID:
#                        peopleID.append(int(item['user_id']))
#                        fileW = open('pepID.txt', 'a')
#                        fileW.write(int(item['user_id']))
#                        fileW.close()
#                        print('-->peopleID: ' + str(peopleID))
#        except:
#            time.sleep(5)
#            values['last_message_id'] = response['items'][0]['id']
#            response = vk.method('messages.get', values)
#            continue

def Main():
#    threadCMD = threading.Thread(target=commandLine)
    threadBOT = threading.Thread(target=MSG)
#    threadCMD.start()
    threadBOT.start()

if __name__ == '__main__':
    Main()
