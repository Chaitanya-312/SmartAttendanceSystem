from MyQR import myqr
import os

#create and read
f=open('students.txt','r')

lines=f.read().split("\n")
print(lines)

#for generating multiple qr codes
for i in range(0,len(lines)):
    data=lines[i]
    name=data        
    #defining & creating qr code     
    version, level, qr_name=myqr.run(
        str(lines[i]),
        level='H',
        version=1,
        #background
        picture='bg.jpg',
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=str(lines[i]+'.bmp'),
        save_dir=os.getcwd()
    )

    


