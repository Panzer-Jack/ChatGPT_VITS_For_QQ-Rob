import json
import os.path
import random
import requests
import socket
import time

import config
from chatGPT import chatGPT_ask

par_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(par_dir)

null = None
true = True

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ListenSocket.bind(('localhost', 5701))
ListenSocket.listen(100)

HttpResponseHeader_OK = '''HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n\r\n
'''

HttpResponseHeader_Continue = '''HTTP/1.1 100 Continue\r\n
Content-Type: text/html\r\n\r\n
'''


class Rep_Funtion:
    def __init__(self):
        self.msg_type = None
        self.language = 0
        pass

    def talk(self, recv):
        num = self.permission(recv)
        print(num)
        print(recv)

        if num:
            # 默认为日语
            if config.language == 1:
                recv["raw_message"] += ", 请你用中文回答"
            elif config.language == 2:
                recv["raw_message"] += ", 请你用英语回答"
            else:
                recv["raw_message"] += ", 请你用日语回答"

            chatGPT_ask(recv["raw_message"])
            msg = '[CQ:record,file=out.wav]'
            self.send_msg(msg, num)

    def permission(self, recv):
        if recv["post_type"] == "message":
            if recv["message_type"] == "group":
                if "CQ:at,qq=2506205190" in recv["raw_message"]:
                    return recv["group_id"]
            elif recv["message_type"] == "private":
                return recv['user_id']
            else:
                return 0

    def find_command(self):
        try:
            req = self.recv_msg()
            recv = req[req.find('"post_type') - 1:]
            recv = json.loads(recv)
            # else:
            print('-----------------------------------------')
            print(recv["raw_message"])
            print('-----------------------------------------')
            self.talk(recv)
        except:
            pass

    def recv_msg(self):
        self.Client, self.Address = ListenSocket.accept()
        Request = self.Client.recv(1024).decode(encoding='utf-8')
        self.Client.sendall((HttpResponseHeader_OK).encode(encoding='utf-8'))
        self.Client.close()
        return Request

    def send_msg(self, msg, number):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payload = None

        ip = '127.0.0.1'
        client.connect((ip, 5700))
        msg_type = 'group'

        # 将字符中的特殊字符进行url编码
        msg = msg.replace(" ", "%20")
        msg = msg.replace("\n", "%0a")

        if msg_type == 'group':
            payload = "GET /send_group_msg?group_id=" + str(
                number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"
        elif msg_type == 'private':
            payload = "GET /send_private_msg?user_id=" + str(
                number) + "&message=" + msg + " HTTP/1.1\r\nHost:" + ip + ":5700\r\nConnection: close\r\n\r\n"

        print("发送" + payload)
        client.send(payload.encode("utf-8"))
        client.close()


if __name__ == '__main__':
    Rep_Server = Rep_Funtion()
    while 1:
        Rep_Server.find_command()
