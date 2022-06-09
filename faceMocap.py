#currnet issue
import socket
import maya.cmds as rd
import math
counter = 1
listPoints = [196,126,355]
leftV = [-87.967,-4.694,-358.423]
rightV = [70.188,-6.437,-372.613]
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
    def get_angle(x1,y1,x2,y2):
        myradians1 = math.atan2(y1, x1)
        myradians2 = math.atan2(y2,x2)
        myradians = myradians2-myradians1
        mydegrees = math.degrees(myradians)
        mydegrees = round(mydegrees,3)
        return mydegrees
    #############################################################   
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
        
    #######################################################
    def getTranslation(a,b,c,angle):
        angle = math.radians(angle) 
        x = a
        y = b*math.cos(angle)-c*math.sin(angle)
        z = b*math.sin(angle)+c*math.cos(angle)
        return x,y,z;   
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

    def angleSubtract(a,b):
        x = a[0]-b[0]
        y = a[1]-b[1]
        z = a[2]-b[2]
        return x,y,z
    ###########################################################
    def animateLoc(self,*arg):
        frame = 0
        endFrame = 100
        step = 5
        while frame < endFrame:
            self.readlines()
            erenYeager = self.splitData
            pos1 = str(erenYeager[listPoints[0]]).split("_")
            pos2 = str(erenYeager[listPoints[1]]).split("_")
            pos3 = str(erenYeager[listPoints[2]]).split("_")
            


            #print(erenYeager)
            length = len(erenYeager)
            print(frame)
            for i in range (length):
                axisStr = str(erenYeager[i]).split("_")
                if(len(axisStr)>2):
                    x1 = pos[0]
                    y1 = pos[1]
                    z1 = pos[2] 

                    namer = "mocapLocator_"+str(i)
                    xValue = float(axisStr[0])-pos1[0]
                    yValue = float(axisStr[1])-pos1[1]
                    zValue = float(axisStr[2])-pos1[2]
                    
                    rd.setKeyframe( namer, t=frame, at='tx', v=xValue )
                    rd.setKeyframe( namer, t=frame, at='ty', v=yValue  )
                    rd.setKeyframe( namer, t=frame, at='tz', v=zValue  )

            frame = frame +step
            for i in range(4):
                self.readlines()
                
    def getPosition(a):
        x=rd.getAttr('%s.translateX'%a)
        y=rd.getAttr('%s.translateY'%a)
        z=rd.getAttr('%s.translateZ'%a)
        return x,y,z;

    def getAngle(x,y):
        radians = math.atan2(y,x)
        degree = math.degrees(radians)
        degree = round(degree,3)
        return degree
    #############################################
    def stabalizeLoc(self,*args):
        pos1=getPosition('mocapLocator_60')
        post2=getPosition('stabilizer')
        rot1=(pos1)
        rot2=(pos2)
        
        

        
            
            
        
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
        self.inputButton4 = rd.button(label = 'animateLoc',command = listen.animateLoc)
        self.inputButton5 = rd.button(label = 'stabalizeLoc')
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