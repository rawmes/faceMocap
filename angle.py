import math
import maya.cmds as rd

def getAngle(x,y):
	radians = math.atan2(y,x)
	degree = math.degrees(radians)
	degree = round(degree,3)
	return degree
def getRotArray(x,y,z):
	a=getAngle(y,z)
	b=getAngle(z,x)
	c=getAngle(x,y)
	return a,b,c
mainRotation = getRotArray(0,0,-4.669);
selection = rd.ls(sl=1)
for item in selection:
	co_x = rd.getAttr("%s.translateX"%item)
	co_y = rd.getAttr("%s.translateY"%item)
	co_z = rd.getAttr("%s.translateZ"%item)
	print co_x,co_y,co_z
	rotation= getRotArray(co_x,co_y,co_z)
	netRotation = rotation - mainRotation

	print netRotation;
	

#getRotArray();