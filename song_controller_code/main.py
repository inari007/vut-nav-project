import serial
import youtube_player
import file_parser
import user_interface

import threading

# parse txt files
fileParser = file_parser.FileParser()
port, firefox_path, geckodriver_path = fileParser.ParseAndGetConfig()
songs = fileParser.ParseAndGetSongs()

# listen on serial port
try:
    ser = serial.Serial(port, 115200)
except:
    print("Could not open port ", port)
    exit(1)

# open YouTube Bot
currentVideo = youtube_player.YoutubePlayer(firefox_path, geckodriver_path)

# open user interface
thread = threading.Thread(target=user_interface.UserInterface, args=(songs, currentVideo))
thread.start()

i = 0
while True:
    # Read data from the serial port
    data = ser.readline().decode('utf-8').strip()

    if data == 'palm':
        currentVideo.PauseVideo()

    elif data == 'thumb':
        currentVideo.PlayVideo()

    elif data == 'left':
        currentVideo.RewindVideo()

    else:
        currentVideo.ResetCounters()

    # debugging
    print(i, " : ", data)
    i = i + 1

ser.close()
