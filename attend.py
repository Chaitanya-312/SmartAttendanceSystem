#Scanning QR code 
import cv2
import pyzbar.pyzbar as pyzbar
import time

#start web cam 
cap=cv2.VideoCapture(0)
names=[]

#function for attendence file
fob=open('attendence.txt','a+')

def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)        
        # z=''.join(str(z))        
        fob.write(z+'\n')
    return names
    
print("Reading code...........")

#function to check data present or not
def checkData(data):
    data=str(data)
    if data in names:
        print("Already present")
    else:
        print("\n"+ str(len(names)+1)+"\n"+ "Present done")        
        enterData(data)
        
while True:
    _,frame=cap.read()
    decodedObject=pyzbar.decode(frame)  
        
    for obj in decodedObject:
        checkData(obj.data)        
        time.sleep(1)
        
    cv2.imshow('Frames',frame)
    
    #closing the program when s is pressed
    if cv2.waitKey(1) & 0xFF==ord('s'):
            cv2.destroyAllWindows()
            break
fob.close()


    
        

    

