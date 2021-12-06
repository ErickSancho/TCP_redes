import socket
import pickle
from twh import ThreeWayHandshake
from time import sleep
# SERVER_ADDRES = "127.0.0.1"
# SERVER_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_client(SERVER_ADDRES, SERVER_PORT):
    address = (SERVER_ADDRES, SERVER_PORT)
    conn1 = ThreeWayHandshake()
    sock.connect(address)
    conn1.Connection()
    while conn1.connected != True:
        sleep(1)
        print("client side:")
        conn1.print_status()
        sock.sendall(pickle.dumps(conn1))
        if conn1.connected == True:
            break
        del conn1
        sleep(1)
        data = sock.recv(4096)
        conn1 = pickle.loads(data)
        del data
        print("client side after response:")
        conn1.print_status()
        conn1.Connection()

    if conn1.connected == True:
      print("Connection established!") 
      return True
    else:
      print("Connection not established!")
      return False

def disconnect_client():
    conn1 = ThreeWayHandshake()
    conn1.Disconnection()
    while conn1.connected != False:
      print("client side:", conn1)
      sock.sendall(pickle.dumps(conn1))
      if conn1.connected == True:
          break
      del conn1
      data = sock.recv(4096)
      conn1 = pickle.loads(data)
      del data
      print("client side after response:", conn1)
      conn1.Disconnect()

    return True    


def client_message(msg):
  try:
    # Send data    
    msg = msg.encode('ascii')
    sock.sendall(msg)

    # Look for the response
    amount_received = 0
    amount_expected = len(msg)

    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        print('data received: \''+str(data.decode('ascii')) + '\'')
  except:
    print('Something went wrong')





def main():
  print("Welcome!\n")  
  IP_server = str(raw_input("IP Address:"))
  server_port = str(raw_input("Server's Port:"))

  conexion= connect_client(IP_server, int(server_port))

  while(conexion):
    print("\n\n*******************\n")
    accion = raw_input("Connection menu:\n1: Send Message\n2: Desconnect\nInput: ")
    print("\n")

    if(accion=='1'):
      msg = raw_input("Enter the message:")
      client_message(msg)
      sock.sendall('1'.encode('ascii'))


    elif (accion=='2'):
      sock.sendall('0'.encode('ascii'))
      disconnect_client()
      sock.close()
      return True

    else:
      print("Enter a valid option")
      continue

    


if __name__ == '__main__':
    main()