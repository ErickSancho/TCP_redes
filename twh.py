class ThreeWayHandshake:

    def __init__(self, twh=None):

        self.status = None
        self.connected = False

    def Connection(self):
        if self.status == None:
            print("starting 3-way handshake\nstatus: sync")
            self.status = "sync"

        elif self.status == "sync":
            print("sync received\nstatus: ack-sync")
            self.status = "ack-sync"

        elif self.status == "ack-sync":
            print("ack-sync received\nstatus: ack")
            self.status = "ack"
            
        elif self.status == "ack":
            self.connected = True
            self.status = "connected"
            print("connected.\nready to received data.")
    def Disconnection(self):
        if self.status == "connected":
            print("starting 3-way handshake\nstatus: connected")
            self.status = "send_end"

        elif self.status == "send_end":
            print("End recived\nstatus: ack")
            self.status = "ack"

        elif self.status == "ack":
            print("Disconnect ack sended\nstatus: disconnect")
            self.status = "disconnect_ack"

        elif self.status == "disconnect_ack":
            print("Disconnecting")
            self.status = "Final_ack"

        elif self.status == "Final_ack":
            print("Disconnected")
            self.status = "disconnected"
            self.connected = False
    


    def IsConnected(self):
        return self.connected

    def Reset(self):
        self.status = None
        self.connected = False

    def print_status(self):
        print "\tstatus: "+ str(self.status) +", connection established: " + str(self.connected)