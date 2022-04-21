#currnet issue
import socket
import maya.cmds as rd
import traceback
import maya.mel as mel
counter = 1
class TCPConnection:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    ##########################################################         
    def connect(self, host, port):
        host = str(host)
        port = int(port)
        try:
            self.sock.connect((host, port))
            print('Successful Connection')
        except:
            print('Connection Failed')
    #########################################################
    def readlines(self):
        x=0
        data = ''
        flush = self.sock.recv(1)
        while(x != 1):
            char = self.sock.recv(1)
            if(str(char) == '?' ):
                x=1
            else:
                data = data+str(char)
        dataArray = data.split("|")
        
        del dataArray[0]
        self.splitData = dataArray
        
        
    ########################################################
    def makeLoc(self,*arg):
        self.deleteLoc()
        for i in range(469):
            thisLocatorName= 'mocapLocator_'+str(i)
            rd.spaceLocator(n=thisLocatorName)
    #######################################################        
    def deleteLoc(self,*arg):
        try:
            rd.delete('*mocapLocator_*')
        except:
            print('nothing was deleted')
    ####################################################
    def initConnection(self,*arg):
        host = uiMake.getHost()
        port = uiMake.getPort()
        self.connect(host,port)
        
    def closeConnection(self,*arg):
        self.sock.close()
    ##########################################################
    
    def animateLoc(self,*arg):
        frame = 0
        endFrame = 500
        step = 1
        while frame < endFrame:
            self.readlines()
            erenYeager = self.splitData
            #print(erenYeager)
            length = len(erenYeager)
            print(frame)
            for i in range (length):
                axisStr = str(erenYeager[i]).split("_")
                if(len(axisStr)>2):
                    namer = "mocapLocator_"+str(i)
                    xValue = float(axisStr[0])
                    yValue = float(axisStr[1])
                    zValue = float(axisStr[2])
                    rd.setKeyframe( namer, t=frame, at='tx', v=xValue )
                    rd.setKeyframe( namer, t=frame, at='ty', v=yValue  )
                    rd.setKeyframe( namer, t=frame, at='tz', v=zValue  )

            frame = frame +step
            for i in range(4):
                self.readlines()
    '''
    def moveLoc(self,*arg):
        self.readlines()
        erenYeager = self.splitData
        #print(erenYeager)
        length = len(erenYeager)
        print(length)
        for i in range (length):
            axisStr = str(erenYeager[i]).split("_")
            print(len(axisStr))
            if(len(axisStr)>2):
                namer = "mocapLocator_"+i
                xvalue = float(axisStr[0])
                yValue = float(axisStr[1])
                zValue = float(axisStr[2])
                rd.setKeyframe( namer, t=frame, at='tx', v=xValue )
                rd.setKeyframe( namer, t=frame, at='ty', v=yValue  )
                rd.setKeyframe( namer, t=frame, at='tz', v=zValue  )
       '''
        
            
            
        
    ########################################################
 
        
        
        

class showUI():
    def __init__(self,*arg):
        self.dispWindow = 'mocap by Rawmes'
        try:
            rd.deleteUI(self.windowx,window=True)
            rd.windowPref(self.windowx,remove = True)
            print('deleted')
        except:
            print('does not exist')
            pass
        self.windowx = rd.window(self.dispWindow)
        rd.columnLayout(adjustableColumn=True)
        rd.text('rawmes was here... Maybe.. maybenot?')
        rd.separator(w=30)
        self.inputStringHost = rd.textFieldGrp(label = 'Enter the host ip:',editable = True,text='192.168.1.67')
        self.inputStringPort = rd.textFieldGrp(label = 'Enter the port:',editable = True,text='9996')
        self.inputButton1 = rd.button(label = 'createLoc', command = listen.makeLoc)
        self.inputButton2 = rd.button(label = 'deleteLoc', command = listen.deleteLoc)
        self.inputButton3 = rd.button(label = 'connect Socket',command = listen.initConnection)
        self.inputButton4 = rd.button(label = 'moveLoc',command = listen.animateLoc)
        self.inputButton5 = rd.button(label = 'close Socket',command = listen.closeConnection)

        rd.showWindow()
        
    def getHost(self):
        host = rd.textFieldGrp(self.inputStringHost,query=True,text=True)
        return host
        
    def getPort(self):
        port = rd.textFieldGrp(self.inputStringPort,query=True,text=True)
        return port
        
listen = TCPConnection()
uiMake = showUI()

uiMake