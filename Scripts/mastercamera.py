import picamera
import time
from subprocess import call
import os
from azure.storage.blob import ContainerClient
import sys

def capture_video():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 15
    
    #adjusts preview window so that it doesn't take up the whole screen
    camera.start_preview(fullscreen=False, window=(100,200,300,400))
    
    #input("Press enter to begin recording...")
    print("Recording...")
    camera.start_recording('/home/inviol/inviol_videos/tmp.h264', intra_period=15)
    camera.wait_recording(30)             
    camera.stop_recording()
    camera.stop_preview()
    print("Recording Complete!")

def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")

def upload_database():
    filename = time.strftime("%d-%m-%y %H:%M:%S.mp4")
    os.rename("/home/inviol/inviol_videos/tmp.mp4", '/home/inviol/inviol_videos/' + filename)
    conn_str = "DefaultEndpointsProtocol=https;AccountName=julia;AccountKey=LFMmYTi4PyWTDMTubQ8lT1DXJJTciM6kJCMzx99ly1Q1XValj8tk47+u5K55FZFbeB9jrp+h5Q/3+ASt1fvR5w==;EndpointSuffix=core.windows.net"
    container_name = "testvideos"

    #blob_client should be set to the name of the video
    container_client = ContainerClient.from_connection_string(conn_str, container_name)
    blob_client = container_client.get_blob_client(filename)
    
    #Path file here
    with open('/home/inviol/inviol_videos/' + filename, 'rb') as data:
        blob_client.upload_blob(data)
    print("Video has been uploaded!")

capture_video()
convert('/home/inviol/inviol_videos/tmp.h264', '/home/inviol/inviol_videos/tmp.mp4')
upload_database()