import os
import os.path
from selenium import webdriver
#import subprocess

"""
def isWindowsProcessRunning( exeName ):                    
    process = subprocess.Popen( 
        'tasklist.exe /FO CSV /FI "IMAGENAME eq %s"' % exeName,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True )
    out, err = process.communicate()    
    try   : return out.split("\n")[1].startswith('"%s"' % exeName)
    except: return False
"""

if os.path.exists("video.mp4.part") == True:
    print("В корневой папке утилиты найден файл части видео!")
    print("Не желаете его воспроизвести? (y/n)")
    choose = str(input("y это да, а n это нет: "))
    if choose == "y":
        os.system("ren video.mp4.part video.mp4")
        os.system("video.mp4")
        os.system("del video.mp4")

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

def WatchingVideo():
    url = driver.current_url
    if url.find("watch?v=") != -1:
        return True
    else:
        return False

while True:
    while True:
        if WatchingVideo() == True:
            #os.system(f"start youtube-dl {driver.current_url} -o video.%(ext)s")
            os.system(f"youtube-dl {driver.current_url} -o video.%(ext)s")
            #while isWindowsProcessRunning("youtube-dl.exe") == False:
            #os.system("ren video.mp4.part video.mp4")
            os.system("video.mp4")
            os.system("del video.mp4")