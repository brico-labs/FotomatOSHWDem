import time
from gpiozero import Button
from picamera import PiCamera
from time import gmtime, strftime
from overlay_functions import *
from guizero import App,PushButton, Text, Picture
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret, 
    access_token,
    access_token_secret
)
status = 1 
# le dice a next_overlay button que hacer
def next_overlay():
    global overlay
    remove_overlays(camera)
    overlay = next(all_overlays)
    # Remove all overlays
    
    preview_overlay(camera, overlay)
    
#dice al  boton take_pic que hacer
def take_picture():
    global output
    output = strftime("/home/pi/fotomaton/Pictures/image.png")
    camera.capture(output)
    remove_overlays(camera)
    output_overlay(output, overlay)

#funcion toma una nueva foto 
def new_picture():
    camera.start_preview()
    preview_overlay(camera, overlay)

def send_tweet():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    # Send the tweet
    message = "Pillado en #OSHWDem17 @OSHWDem @Brico_Labs"
    with open(output, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)


def orange_beha():
    global status
    if status == 1:
        remove_overlays(camera)
        next_overlay()
    elif status == 2:
        pass
    else:
        quit()
def green_beha():
    global status
    if status == 1:
        status = 2
        preview_overlay_o(camera, "Pre")
        time.sleep(1)
        remove_overlays(camera)
        remove_overlays(camera)
        preview_overlay(camera, overlay)
        preview_overlay_o(camera, "3")
        time.sleep(1)
        remove_overlays(camera)
        remove_overlays(camera)
        preview_overlay(camera, overlay)
        preview_overlay_o(camera, "2")
        time.sleep(1)
        remove_overlays(camera)
        remove_overlays(camera)
        preview_overlay(camera, overlay)
        preview_overlay_o(camera, "1")
        time.sleep(1)
        remove_overlays(camera)
        remove_overlays(camera)
        preview_overlay(camera,overlay)
        take_picture()
        send_tweet()
        preview_overlay(camera, overlay)
        preview_overlay_o(camera, "fin")
        time.sleep(2)
        remove_overlays(camera)
        remove_overlays(camera)
        preview_overlay(camera,overlay)
        status = 1
    elif status == 2:
        pass
    else:
        quit()

#Def Satus
# - Status = 1 -> Usual Status
# - Status = 0 -> Asking for seding tweet

   
#declaracion de botones
#Button(23) -> orange button
#Button(25) -> green button

orange_button = Button(25)
green_button= Button(23)

orange_button.when_pressed = orange_beha
green_button.when_pressed = green_beha


#declaracion camara
camera = PiCamera()
camera.resolution=(800,480)
camera.hflip = True

#vista previa camara
camera.start_preview()
preview_overlay(camera,overlay)

#establece nombre foto
output = " "

#Funcion App pantalla de inicio, fin y enlace sigueinte foto
app = App("FotomatOSHWDem", 800, 480)
app.display()



 
