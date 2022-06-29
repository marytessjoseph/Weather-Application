# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:33:00 2022

@author: maryt
"""

#import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Read the config.ini file and load the key and URL in the program
#extract key from the configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


#create a getweather() to get the weather of particular location
#explicit function to get weather details
def getweather(city):
    result = requests.get(url.format(city,api_key))
    
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country,temp_kelvin,temp_celsius,weather1]
        return final
    else:
        print("NO results found")
        
#create a search function to get output weather details
#explicit function to search city
def search():
    city = city_text.get()
    weather = getweather(city)
    
    if weather:
        location_lbl['text'] = '{},{}'.format(weather[0],weather[1])
        temperature_label['text'] = str(weather[3])+"° Celsius"
        weather_l['text'] = weather[4]
        
    else:
        messagebox.showerror('Error',"Cannot find {}".format(city))
  
#Driver code
#create the body of the GUI with the help of tkiinter
#create object
app = Tk()

#add title
app.title ("Weather Application")

#adjust window size
app.geometry("1080x200")

#add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable = city_text)
city_entry.pack()

Search_btn = Button(app,text ="Search",width =14,command =search)
Search_btn.pack()

location_lbl = Label(app,text = "Location", font = {'bold',18})
location_lbl.pack()

temperature_label = Label(app, text ="")
temperature_label.pack()

weather_l = Label(app,text="")
weather_l.pack()

app.mainloop()
