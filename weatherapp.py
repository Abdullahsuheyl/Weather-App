from re import T
from tkinter import*
from tkinter import font
from turtle import bgcolor
from PIL import ImageTk, Image
import requests

url="http://api.openweathermap.org/data/2.5/weather" #REQUEST YAPILACAK URL
api= "YOUR API" #Api
iconurl="http://openweathermap.org/img/wn/{}@2x.png" #İCONs URL

def Havadurumu(şehir):
    parametreler={"q":şehir,"lang":"tr","appid":api}
    veri= requests.get(url,params=parametreler).json()
    print(veri)
    deneme=veri["cod"]
    if deneme==200 :
        isim=veri["name"]
        rüzgarhizi=veri["wind"]["speed"]
        ülke=veri["sys"]["country"]
        sicaklik=int(veri["main"]["temp"]-273.15)
        hissedilensıcaklık=int(veri["main"]["feels_like"]-273.15)
        basinç=int(veri["main"]["pressure"])
        havaaciklama=veri["weather"][0]["description"]            
        icon=veri["weather"][0]["icon"]
        return (isim,rüzgarhizi,ülke,sicaklik,hissedilensıcaklık,basinç,havaaciklama,icon)
    elif deneme=="404":   
         hata1=("Böyle bir şehir bulunamadı")
         return hata1        
def main():
    
    
    şehir=cityEntry.get()
    havadurumu=Havadurumu(şehir)
    print(havadurumu)
    if havadurumu=="Böyle bir şehir bulunamadı" :
        Hata["text"]=havadurumu
        
    else:
        Lokasyon["text"]=f"{havadurumu[0]},{havadurumu[2]}"
        TempLabel["text"]=f"{havadurumu[3]}°C"
        Temp_Label["text"]=f"Hissedilen sıcaklık:{havadurumu[4]} "
        PreLabel["text"]=f"Basınç:{havadurumu[5]}"
        Aciklama["text"]=f"{havadurumu[0]}'da Hava {havadurumu[6]}"
        icon=ImageTk.PhotoImage(Image.open(requests.get(iconurl.format(havadurumu[-1]),stream=True).raw))
        iconetiket.configure(image=icon)
        iconetiket.Image=icon

app= Tk()

app.title("Hava Durumu Göstergesi")
app.geometry("700x850")

#İNPUT 
cityEntry=Entry(app,justify="center") 
cityEntry.pack(fill=BOTH,ipady="15",ipadx="23",pady="10")
cityEntry.focus()


AramaButonu= Button(app,text="Arama",font= ('Roboto',13),command=main,bg="#ff9b08")
AramaButonu.pack(fill=BOTH,ipady="10",padx="30")

iconetiket=Label(app)
iconetiket.pack()

Lokasyon= Label(app,font=("Roboto",50))
Lokasyon.pack()

TempLabel=Label(app, font=("Roboto",60,"bold"))
TempLabel.pack()
Temp_Label=Label(app, font=("Roboto",45))
Temp_Label.pack()
PreLabel=Label(app, font=("Roboto",45))
PreLabel.pack()

Aciklama=Label(app,font=("Roboto",30))
Aciklama.pack()

Hata=Label(app,font=("Roboto",30))
Hata.pack()

app.mainloop()
