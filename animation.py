from tkinter import *
import random
import time

WIDTH = 500
HEIGHT = 500
pelotaNo = 0
textoX=60
textoY=0

pelota_width = 30
pelota_height = 30

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg = "light yellow")
canvas.pack()


def lanzarPelota():
    global pelotaNo
    global textoY

    xVelocity = 5
    yVelocity = 5

    color = "#"+("%06x"%random.randint(0,16777215))
    pelotaNo +=1
    numero = pelotaNo
    textoY += 20
    pelota = canvas.create_oval(0,0,30,30, width=0, fill=color )
    canvas.move(pelota, random.randint(0,300), random.randint(0,300))
    pelotaStatus = canvas.create_text(textoX,textoY, fill = color, text = "pelota "+str(pelotaNo)+" Activa")

    for a in range(500):
        coordinates = canvas.coords(pelota)
        if(coordinates[0]>=(WIDTH-pelota_width) or coordinates[0]<0):
            xVelocity = -xVelocity
        if(coordinates[1]>=(HEIGHT-pelota_height) or coordinates[1]<0):
            yVelocity = -yVelocity
        canvas.move(pelota,xVelocity,yVelocity)
        canvas.update()
        time.sleep(0.01)

    canvas.itemconfig(pelota, state = 'hidden')
    canvas.itemconfig(pelotaStatus,text = "pelota "+str(numero)+" Inactiva")


boton = Button(text="Lanzar", command=lanzarPelota)
boton.place(x=200, y=450)

window.mainloop()