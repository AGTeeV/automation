import cv2
import dropbox
import time
import random

startTime=time.time()

def takePicture():
    number=random.randint(0,100)
    camera=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=camera.read()
        imageName="newPicture"+str(number)+".jpg"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    camera.release()
    cv2.destroyAllWindows()


def uploadFile(imageName):
    accesToken="sl.BITmUFJx1mgrDwIa6wFxDVQD6cV-W7J5pKGCfgo7xC4ivZW0bGgocx7mYc3airdNIqi35p5yf857yWi8F_ERvAbkyuCen1BRenaTmGOf-syzkbnk9U8snB0AkMfunZipYfpLLekdAOo"
    source=imageName
    destination="/images/"+imageName
    dbx=dropbox.Dropbox(accesToken)
    with open(source,"rb") as img:
        dbx.files_upload(img.read(),destination,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")


def main():
    while True:
        if((time.time()-startTime)>=5):
            image=takePicture()
            uploadFile(image)
main()
