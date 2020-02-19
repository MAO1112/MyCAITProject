#from MyFunc import *
from socket import *
from json import *

#####其他文件的函数
def recongnize_face():
    res = {}
    res["name"] = "Michael"
    res["coordinates"] = [23, 55, 56, 175]
    return res
#####

Host = '127.0.0.1'
Port = 6695
Server = socket(AF_INET, SOCK_STREAM)
Server.bind((Host , Port))
Server.listen(5)
print('Servering port %d' % Port)

Cont = '''
HTTP/1.x 200 ok
Access-Control-Allow-Origin: *

'''
Erro = '''
HTTP/1.x 500 Internal Server Error
Access-Control-Allow-Origin: *

Python Error: '''
Res = ""

while 1:
    Conn, Addr = Server.accept()
    try:
        Sent = Conn.recv(1024).decode("UTF-8")
        Sent = Sent.split('\n')
        Sent = Sent[-1]
        if Sent:
            print(Sent)
            exec("Res = " + Sent)
            Res = dumps(Res)
            print("Res = " + Res)
            Conn.sendall(bytes(Cont + str(Res), 'UTF-8'))
            print("============\n\n")

    except Exception as Res:
        print(Res)
        Conn.sendall(bytes(Erro + str(Res), 'UTF-8'))
    finally:
        Conn.close()