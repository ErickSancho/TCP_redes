import socket
import pickle
import signal
import sys

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 5000
hanler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (SERVER_ADDRESS, SERVER_PORT)

print "server " + str(SERVER_ADDRESS) + " at port " + str(SERVER_PORT)
hanler.bind(address)
hanler.listen(3)


def terminate_handler(obj, obj2):
  print("Finalizacion servidor")
  hanler.close()
  sys.exit()

signal.signal(signal.SIGTERM, terminate_handler)
signal.signal(signal.SIGINT, terminate_handler)



def connect_server():
    con_status = False
    while True:
        print("waiting for connection")
        connection, client_address = hanler.accept()
        try:
            print('connection from', client_address)
            while con_status != True:
                data = connection.recv(4096)
                obj = pickle.loads(data)
                del data
                print("recieved.")
                obj.Connection()
                print("server side:")
                obj.print_status()
                connection.sendall(pickle.dumps(obj))
                con_status = obj.IsConnected()
            print("3-way done!!!")   
        except:
            pass
        server_message(connection)
        break
              

def disconnect_server(connection):
    con_status = True
    print("Ending Connection")
    try:
        while con_status != False:
            data = connection.recv(4096)
            obj = pickle.loads(data)
            del data
            obj.Connection()
            print("server side:", obj)
            connection.sendall(pickle.dumps(obj))
            con_status = obj.IsConnected()
        print("3-way disconnection done!!!")
        connection.close()
        
    except:
        pass



def server_message(connection):
    
    while True:
        data = connection.recv(4096)
        if data:
            data_string = data.decode('ascii')

            if (data_string=='0'):
              disconnect_server(connection)
              break
            else:
              print('received {!r}'.format(data.decode('ascii')))
              print('sending data back to the client')
              data_mayus = data_string.upper()
              connection.sendall(data_mayus.encode('ascii'))
              continue
                      

if __name__ == '__main__':
  while(True):
    connect_server()