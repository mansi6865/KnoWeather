import json
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root= Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city= textfield.get()
    geolocator= Nominatim(user_agent= "geoapiExercises")
    location= geolocator.geocode(city)
    obj= TimezoneFinder()
    result= obj.timezone_at(lng= location.longitude, lat= location.latitude)
    timezone.config(text= result)
    long_lat.config(text= f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    home= pytz.timezone(result)
    local_time= datetime.now(home)
    current_time= local_time.strftime("%I: %M %p")
    clock.config(text= current_time)
    # name.config(text= "CURRENT WEATHER")

    #weather

    api_key= 'a5efb16ea59d8dc596c4ee992d2fab5d'
    base_url= "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city
    json_data= requests.get(base_url).json()
    
    condition= json_data['weather'][0]['main']
    description= json_data['weather'][0]['description']
    temp= int(json_data['main']['temp']-273.15)
    pressure= json_data['main']['pressure']
    humidity= json_data['main']['humidity']
    wind= json_data['wind']['speed']
    
    t.config(text= (temp, "°"))
    c.config(text=(condition,"|", "FEELS", "LIKE", temp,"°"))
    w.config(text= wind)
    h.config(text= humidity)
    d.config(text= description)
    p.config(text= pressure)
    
#search
search_img= PhotoImage(file= "search.png")
myimg= Label(image= search_img)
myimg.place(x=20, y=20)
textfield= tk.Entry(root, justify= "center", width= 17, font= ("poppins",20,"bold"), bg= "#404040", border= 0, fg= "white")
textfield.place(x=50,y=40)
textfield.focus()
search_icon= PhotoImage(file= "search_icon.png")
myimg_icon= Button(image= search_icon, borderwidth=0,cursor="hand2", bg="#404040", command= getWeather)
myimg_icon.place(x=400, y=34)

#logo
img_logo= PhotoImage(file="logo.png")
logo= Label(image= img_logo)
logo.place(x=150, y=100)

#bottom box
img_frame= PhotoImage(file= "box.png")
frame_img= Label(image= img_frame)
frame_img.pack(padx= 5, pady= 5, side= BOTTOM)

#clock
clock= Label(root, font=("Helvetica",15,"bold"), fg="black")
clock.place(x=750, y=100)

#time
timezone= Label(root, font=("Helvetica", 25, "bold"))
timezone.place(x= 600, y=50)
long_lat= Label(root, font= ("Helvetica", 10))
long_lat.place(x=600, y=90)

#label
label1= Label(root, text= "WIND", font= ("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2= Label(root, text= "HUMIDITY", font= ("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3= Label(root, text= "DESCRIPTION", font= ("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4= Label(root, text= "PRESSURE", font= ("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t= Label(font=("arial", 70, "bold"), fg= "#ee666d")
t.place(x=400, y=150)
c= Label(font=("arial", 15, 'bold'))
c.place(x= 400, y=250)

w= Label(text="...", font= ("arial", 20, "bold"), bg= "#1ab5ef")
w.place(x=120, y=430)
h= Label(text="...", font= ("arial", 20, "bold"), bg= "#1ab5ef")
h.place(x=280, y=430)
d= Label(text="...", font= ("arial", 20, "bold"), bg= "#1ab5ef")
d.place(x=450, y=430)
p= Label(text="...", font= ("arial", 20, "bold"), bg= "#1ab5ef")
p.place(x=670, y=430)




root.mainloop()
